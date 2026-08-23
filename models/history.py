from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HospitalMedicalHistory(models.Model):
    _name = 'hospital.medical.history'
    _description = 'Medical History'
    _order = 'date desc'

    date = fields.Date(
        string='Date',
        required=True,
        default=fields.Date.today
    )

    diagnosis = fields.Char(
        string='Diagnosis',
        required=True
    )

    symptoms = fields.Text(
        string='Symptoms',
        required=True
    )

    treatment = fields.Text(
        string='Treatment',
        required=True
    )

    notes = fields.Text(
        string='Additional Notes'
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
        ],
        string='Status',
        default='draft',
        required=True
    )

    @api.constrains('date')
    def _check_history_date(self):
        for record in self:
            if record.date and record.date > fields.Date.today():
                raise ValidationError(
                    'Medical history date cannot be in the future.'
                )

    def action_confirm(self):
        for record in self:
            record.state = 'confirmed'

    def action_reset_to_draft(self):
        for record in self:
            record.state = 'draft'