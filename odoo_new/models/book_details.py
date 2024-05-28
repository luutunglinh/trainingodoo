from odoo import api, fields, models, _
from odoo.exceptions import *


class BookDetail(models.Model):
    _name = "book.details"
    _description = "Book Detail"
    _order = "name"

    _inherit = [ 'website.published.mixin']

    name = fields.Char("Name of book", required=True)
    author_id = fields.Many2many("res.partner", string="Author")
    isbn_no = fields.Char(string="ISBN", required=True)
    published_year = fields.Char(string='Published Year', size=4)
    book_state = fields.Selection(selection=[
        ("available", "Available"),
        ("not_available", "Not Available"),
    ],
        string="Status",
        required=True,
        copy=False,
        default="available"
    )
    copies_of_book = fields.Integer(string='Available Copies ')
    stock_of_copies = fields.Integer(string='Stock')
    # borrow_ids = fields.One2many('book.borrow', 'book_id', string="Borrow ")
    genre_ids = fields.Many2many('book.genre', string="Genre")
    manager_id = fields.Many2one('res.users', string='Manager', related='genre_ids.manager_id')
    image = fields.Binary(attachment=True)

    book_issue_ids = fields.One2many('book.issue', 'book_id', string='Issues')

    restrict_country_ids = fields.Many2many('res.country')


    def redirect_homepage(self):
        url = "http://localhost:8069"
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': url
        }

    # @api.depends('copies_of_book', 'book_state')
    # def _compute_book_state(self):
    #     for record in self:
    #         if record.copies_of_book == 0:
    #             return record.write({'book_state': 'not_available'})
    #         else:
    #             return record.write({'book_state': 'available'})

    @api.constrains('copies_of_book', 'stock_of_copies')
    def _check_stock_of_copies(self):
        if self.copies_of_book > self.stock_of_copies:
            raise ValidationError(_("Available Copies cannot be more than Stock."))

