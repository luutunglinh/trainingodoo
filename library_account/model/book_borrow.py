from odoo import models, Command, fields


class BookBorrow(models.Model):
    _inherit = "book.borrow"

    move_id = fields.Many2one("account.move")
