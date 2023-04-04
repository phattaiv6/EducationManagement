from odoo import fields, models, api


class Course(models.Model):
    _name = 'course.student'
    _description = 'Khóa học'

    name_course = fields.Char(string='Tên Khóa Học')
    course_ids = fields.Char(string='ID Khóa Học', readonly = True, default = 0)
    start_date = fields.Date(string='Ngày bắt đầu', required=True)
    end_date = fields.Date(string='Ngày kết thúc', required=True)
    active = fields.Boolean(default=True)
    marksheet_id = fields.Many2many(comodel_name='marksheet.student',
        string='Bảng điểm',
        relation='marksheet_course_rel',
        column1='course_ids',
        column2='marksheet_id')
    @api.model
    def create(self,vals):
        if vals.get('course_ids',0) == 0:
            vals['course_ids'] = self.env['ir.sequence'].next_by_code('course')
        result = super(Course, self).create(vals)
        return result
    @property
    def display_name(self):
        return  self.name_course
    display_name = fields.Char(string='tên hiển thị',compute='_compute_display_name', store=True)
    @api.depends('name_course')
    def _compute_display_name(self):
        for record in self:
            record.display_name= record.name_course
