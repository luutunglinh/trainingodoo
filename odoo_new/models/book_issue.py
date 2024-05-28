# -*- coding: utf-8 -*-
from odoo import models, fields

class LibraryBookIssue(models.Model):
    _name = "book.issue"
    _inherit = ['utm.mixin']

    book_id = fields.Many2one('book.details', string='Book', required = True)
    submitted_by = fields.Many2one('res.users')
    issue_description = fields.Char(string='Description Issue')





