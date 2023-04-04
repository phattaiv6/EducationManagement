from odoo import fields, models, api


class Teacher(models.Model):
    _name = 'teacher.education'
    _description = 'thông tin  giáo viên'

    name = fields.Char(string='Họ và tên', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Số điện thoại', required=True,size =10)
    address = fields.Char(string='địa chỉ', required=True)
    teacher_ids = fields.Char(string='Mã giáo viên', readonly=True, default=0)
    age = fields.Integer(string='Tuổi')

    active = fields.Boolean(default=True)
    gender = fields.Selection([('nam', 'Nam'), ('nữ', 'Nữ')], string='Giới tính')
    class_ids = fields.One2many('class.student', 'teacher_ids', string='Mã lớp')
    _sql_constraints = [('phone_unique', 'UNIQUE(phone)', 'Số điện thoại đã tồn tại!')]

    @api.model
    def create(self, vals):
        if vals.get('teacher_ids', 0) == 0:  # kiểm tra ids ,nếu không tồn tại thì ids = 0
            # thực hiện sequence đã setting
            vals['teacher_ids'] = self.env['ir.sequence'].next_by_code('teacher.education') or 0
        result = super(Teacher, self).create(vals)  # gọi create ở lớp cha và gán = result
        return result  # trả về
