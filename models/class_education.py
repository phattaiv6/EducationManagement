from odoo import fields, api, models


class Student_class(models.Model):
    _name = "class.student"
    _description = 'Lớp học'
    name = fields.Char(string='Tên lớp')
    class_ids = fields.Char(string='Mã lớp hoc', readonly=True, default=0)
    start_date = fields.Date(string='Ngày bắt đầu', required=True)
    end_date = fields.Date(string='Ngày kết thúc', required=True)
    student_ids = fields.Many2many(
        comodel_name='student',
        string='học sinh',
        relation='student_class_rel',
        column1='class_ids',
        column2='student_ids')
    teacher_ids = fields.Many2one('teacher.education',string='Mã giáo viên')
    active = fields.Boolean(default=True)
    @api.model
    def create(self, vals):
        if vals.get('class_ids', 0) == 0:
            vals['class_ids'] = self.env['ir.sequence'].next_by_code('class.student') or 0
            result = super(Student_class, self).create(vals)
            return result
