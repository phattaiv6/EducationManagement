from odoo import fields, api, models


class Student_class(models.Model):
    _name = "class.student"
    _description = 'Lớp học'
    name = fields.Char(string='Tên lớp')
    reference = fields.Char(string='Mã lớp hoc', readonly=True, default=0)
    student_ids = fields.Many2many(
        comodel_name='student',
        string='học sinh',
        relation='student_class_rel',
        column1='class_ids',
        column2='student_ids')
    teacher_ids = fields.Many2many(
        comodel_name='teacher.education',
        string='Giáo viên',
        relation='teacher_class_rel',
        column1='teacher_ids',
        column2='class_ids')
    active = fields.Boolean(default=True)
    @api.model
    def create(self, vals):
        if vals.get('class_ids', 0) == 0:
            vals['reference'] = self.env['ir.sequence'].next_by_code('class.student') or 0
            result = super(Student_class, self).create(vals)
            return result
