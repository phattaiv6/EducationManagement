from odoo import fields, models, api


class Parent(models.Model):
    _name = 'parent'
    _description = 'thông tin  phụ huynh'

    name = fields.Char(string='Họ và tên', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Số điện thoại', required=True,size =10)
    address = fields.Char(string='địa chỉ', required=True)
    parent_ids = fields.Char(string='Mã phụ huynh', readonly=True, default=0)
    age = fields.Integer(string='Tuổi')
    student_ids = fields.One2many('student', 'parent_ids', string='Học sinh')
    active = fields.Boolean(default=True)
    gender = fields.Selection([('nam', 'Nam'), ('nữ', 'Nữ')], string='Giới tính')

    _sql_constraints = [('phone_unique', 'UNIQUE(phone)', 'Số điện thoại đã tồn tại!')]

    @api.model
    def create(self, vals):
        if vals.get('parent_ids', 0) == 0:  # kiểm tra ids ,nếu không tồn tại thì ids = 0
            # thực hiện sequence đã setting
            vals['parent_ids'] = self.env['ir.sequence'].next_by_code('parent') or 0
        result = super(Parent, self).create(vals)  # gọi create ở lớp cha và gán = result
        return result  # trả về
