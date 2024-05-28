from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    _sql_constraints = [
        ("check_isbn_no","UNIQUE(isbn_no)","This ISBN number must be unique"),
        ("check_stock_of_copies","CHECK(stock_of_copies > 0)","The copies of available book must be strictly positive"),
        ("check_copies_of_book", "CHECK(copies_of_book >= 0)", "The Available Copies must be strictly positive"),
    ]

    author_id = fields.Many2many("res.partner", string = "Author")
    isbn_no = fields.Char(string="ISBN no", required = True)
    published_year = fields.Char(string="Published Year", size=4)
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
    genre_ids = fields.Many2many('book.genre', string="Genre")
    manager_id = fields.Many2one('res.users', string='Manager', related='genre_ids.manager_id')
    borrow_id = fields.Many2one('book.borrow')

    @api.constrains('copies_of_book', 'stock_of_book')
    def _constraints_check_available_copy(self):
        if self.copies_of_book > self.stock_of_copies:
            raise ValidationError(_('Copies of book cannot greater than Stock '))
