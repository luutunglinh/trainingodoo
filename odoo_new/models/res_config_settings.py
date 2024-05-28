from odoo import fields, models, api, _



class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    penalty_amount = fields.Float(config_parameter='odoo_new.penalty_amount')
    max_day = fields.Integer(config_parameter='odoo_new.max_day')