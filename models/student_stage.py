from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'student.stage'
    _description = 'trạng thái'
    _order = 'sequence,name'
    name = fields.Char(string='Tên')
    sequence = fields.Integer(string='Sequence')
    fold = fields.Boolean(string='Fold')
    stage = fields.Char(string='Trang thái')

