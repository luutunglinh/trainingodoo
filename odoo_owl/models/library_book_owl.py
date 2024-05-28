# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryBookOWL(models.Model):
    _name = "library.book.owl"
    _description = 'Library Book OWL'

    _order = 'date_release desc, name'

    name = fields.Char('Title', required=True)
    short_name = fields.Char('Short Title')
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')
    description = fields.Char('Description')

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.name, record.date_release)
            result.append((record.id, rec_name))
        return result
