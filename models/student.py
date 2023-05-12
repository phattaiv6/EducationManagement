from datetime import date

from odoo import fields, models, api
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
from odoo import _


class Student(models.Model):
    #thông tin học sinh
    _name = "student"
    _description = "quản lý học sinh"
    name = fields.Char("Họ và tên")
    dob = fields.Date('Ngày sinh')
    student_image = fields.Image(string="Ảnh")
    gender = fields.Selection([
        ('nam', 'Nam'),
        ('nữ', 'Nữ')
    ], string='Giới tính')
    description = fields.Text('Ghi chú')
    age = fields.Integer(string='Tuổi', compute='_compute_age', inverse='_inverse_age',
                         store=False, compute_sodu=True)
    reference = fields.Char(string='Mã học sinh', readonly=True, default=0)
    active = fields.Boolean(default=True)
    class_ids = fields.Many2many(
        comodel_name='class.student',
        string='Lớp học',
        relation='student_class_rel',
        column1='student_ids',
        column2='class_ids'
    )
    marksheet_id = fields.One2many('marksheet.student', 'student_ids', string='Bảng điểm')
    course_ids = fields.One2many('course.student', 'student_ids', string='Khóa học')
    fee_ids = fields.One2many('student.fee', 'student_ids', string='Học Phí')
    state = fields.Selection(string='Trạng thái', selection=[('new', 'New'), ('studying', 'Studying'), ('off', 'Off'),
                                                             ], default='new')
    #thông tin phụ huynh
    parent_name = fields.Char(string="Họ và tên phụ huynh")
    gender_parent = fields.Char( string='Quan hệ với học sinh')
    text = fields.Text("Ghi chú")
    phone = fields.Char(string='Số điện thoại', required=True, size=10)
    fee_count = fields.Integer(string="Số lượng học phí", compute='_get_fee_count',store=True)
    @api.depends('fee_ids')
    def _get_fee_count(self):
        for record in self:
            record.fee_count = len(record.fee_ids)

    _sql_constraints = [
        ('phone_unique', 'unique(phone)', "The phone code must be unique!"),
    ]
    @api.model
    def create(self, vals):
        if vals.get('reference', 0) == 0:  # kiểm tra ids ,nếu không tồn tại thì ids = 0
            # thực hiện sequence đã setting
            vals['reference'] = self.env['ir.sequence'].next_by_code('student') or 0
        result = super(Student, self).create(vals)  # gọi create ở lớp cha và gán = result
        return result  # trả về

    @api.constrains('dob')
    def _check_dob(self):  # hàm ràng buộc ngày sinh
        for record in self:
            if record.dob > fields.Date.today():
                raise ValidationError('Date of Birth must be in the past')

    @api.depends('dob')
    def _compute_age(self):  # hàm tính toán field age
        curent_year = fields.Date.today().year
        for record in self:
            if record.dob:
                record.age = curent_year - record.dob.year
            else:
                record.age = 0

    def _inverse_age(self):  # hàm nghịch đảo khi sửa fields age sẽ làm thay đổi giá trị fields dob
        for r in self:
            if r.age and r.dob:
                curent_year = fields.Date.today().year
                dob_year = curent_year - r.age
                dob_month = r.dob.month
                dob_day = r.dob.day
                dob = date(dob_year, dob_month, dob_day)
                r.dob = dob

    @api.model
    def is_allowed_state(self, curent_state, new_state):
        allowed_state = [('new', 'studying'), ('studying', 'off'), ('off', "studying"), ('new', 'off')]
        return (curent_state, new_state) in allowed_state

    def change_student_state(self, state):
        for student in self:
            if student.is_allowed_state(student.state, state):
                student.state = state
            else:
                raise UserError(_("Changing student status from %s to %s is not allowed.") % (student.state, state))

    def change_to_new(self):
        self.change_student_state('new')

    def change_to_studying(self):
        self.change_student_state('studying')

    def change_to_off(self):
        self.change_student_state('off')
    