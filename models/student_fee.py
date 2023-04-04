from odoo import fields, models, api


class Student_fee(models.Model):
    _name = 'student.fee'
    _description = 'Học phí'

    fee_ids = fields.Char(string='ID',readonly = True, default = 0)
    student_ids = fields.Many2many('student',string='Mã học sinh')
    description = fields.Char(string='Mô tả')
    date = fields.Date(string='Ngày thanh toán',required=True,default=fields.Date.today())
    # amount = fields.Float(string='Tiền')
    currency_id = fields.Many2one('res.currency', string='Currency')
    amount_paid = fields.Monetary('Amount Paid')

    @api.model
    def create(self, vals):
        if vals.get('fee_ids', 0) == 0:  # kiểm tra ids ,nếu không tồn tại thì ids = 0
            # thực hiện sequence đã setting
            vals['fee_ids'] = self.env['ir.sequence'].next_by_code('student.fee') or 0
        result = super(Student_fee, self).create(vals)  # gọi create ở lớp cha và gán = result
        return result  # trả về