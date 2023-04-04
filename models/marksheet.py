from odoo import fields, models, api


class Marksheet(models.Model):
    _name = 'marksheet.student'
    _description = 'bảng điểm'


    name_marksheet = fields.Char(string='Tên Bảng Điểm')
    marksheet_id = fields.Char(string='ID Bảng Điểm', readonly = True, default = 0)
    student_ids = fields.Many2one('student', string='Mã học sinh')
    score_15 = fields.Float(string="Điểm 15 phút")
    score_45 = fields.Float(string="Điểm 45 phút")
    score_end = fields.Float(string="Điểm cuối kì")
    #course_ids = fields.Many2one('course',string='ID khóa học')

    Total_score = fields.Float(string='Điểm tổng kết',compute='_compute_score_average')
    @api.depends('score_15','score_45','score_end')
    def _compute_score_average(self):
        for record in self:
            score_sum = record.score_15 + record.score_45 + record.score_end
            score_average = score_sum / 3.0
            record.Total_score = score_average

    @api.model
    def create(self,vals):
        if vals.get('marksheet_id',0) == 0:
            vals['marksheet_id'] = self.env['ir.sequence'].next_by_code('marksheet') or 0
            result = super(Marksheet, self).create(vals)
        return  result
