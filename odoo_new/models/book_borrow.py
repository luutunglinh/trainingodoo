from odoo import api, fields, models, _
from datetime import datetime, timedelta
from odoo.exceptions import *
from dateutil.relativedelta import relativedelta

class BookBorrow(models.Model):
    _name = "book.borrow"
    _description = "Book borrow"
    _rec_name = "id"

    _sql_constraints = [
        ("check_validity", "CHECK(validity>0)","Validity must be more than 1 day")
    ]

    name = fields.Char(string = "Borrow Data ID", copy=False, readonly=True)
    reader_id = fields.Many2one("res.partner", string="Reader")
    book_id = fields.Many2many('book.details', string='Book',ondelete='cascade',
                               domain=[('book_state', '!=', 'not_available')])
    date_of_borrow = fields.Date(string="Borrowing Date", default=datetime.today() )
    currency_id = fields.Many2one(
        'res.currency', 'Currency')
    test = fields.Monetary("Test")
    fine = fields.Monetary(string='penalty(per book)', currency_field='currency_id')
    validity = fields.Integer(required=True, default=1, string='Validity')
    deadline = fields.Date(compute='_compute_deadline', readonly=True)
    return_date = fields.Date(string='Return date', readonly=True)
    current_date = fields.Date(default=datetime.today())
    borrow_state = fields.Selection(
        selection=[
            ('new', 'New'),
            ("taken", "Taken"),
            ('returned', 'Returned')
        ],
        string="Status",
        copy=False,
        default='new'
    )






    @api.depends('validity','date_of_borrow')
    def _compute_deadline(self):
        for record in self:
            record.deadline = record.date_of_borrow + timedelta(days = record.validity)


    @api.constrains('validity')
    def _contrains_check_validaty(self):
        max_day = self.env['ir.config_parameter'].sudo().get_param('odoo_new.max_day')
        if self.validity > int(max_day):
            raise ValidationError(_("Max of validity is less than provide data"))


    @api.constrains('current_date','date_of_borrow')
    def _contrains_check_date_of_borrow(self):
        if self.date_of_borrow > self.current_date:
            raise ValidationError(_('You can not enter the date of borrow from future.'))

    def action_borrow(self):
        for record in self.book_id:
            domain = []
            for item in record:
                domain += [('name','=',item.name)]
            book_stock = self.env['book.details'].sudo().search(domain)
            for rec in book_stock:
                if rec.copies_of_book > 0:
                    rec.copies_of_book -= 1
                else:
                    raise ValidationError(_('Books are not available.'))

        self.write({
            'borrow_state':'taken'
        })

    def action_return(self):
        fine = self.env['ir.config_parameter'].sudo().get_param('odoo_new.penalty_amount')
        for record in self.book_id:
            domain = []
            for item in record:
                domain += [('name','=',item.name)]
            book_stock = self.env['book.details'].sudo().search(domain)
            for rec in self:
                rec.return_date = datetime.today()
                if rec.return_date > rec.deadline:
                    max_days = int(self.env['ir.config_parameter'].sudo().get_param('odoo_new.max_day'))
                    fine_add = rec.date_of_borrow + relativedelta(days=max_days)
                    print('finr',fine_add)
                    print((rec.return_date))
                    if rec.return_date > fine_add:
                        print(((rec.return_date - fine_add).days))
                        rec.fine = int((rec.return_date - fine_add).days) * float(fine)
                for r in book_stock:
                    r.copies_of_book += 1
        self.write({
            'borrow_state':'returned'
        })




