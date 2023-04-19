from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)

class UpdateWizard(models.TransientModel):
    _name = 'wizard.student'
    _description = 'Update state'

    state = fields.Char(string="Trạng thái",readonly=True, default='off')
    description = fields.Text('Ghi chú')

    def multi_update(self):
        ids = self.env.context['active_ids']  # selected record ids
        student = self.env["student"].browse(ids)
        new_data = {}

        if self.state:
            new_data["state"] = self.state

        if self.description:
            new_data["description"] = self.description

        student.write(new_data)
