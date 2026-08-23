from odoo import models, fields


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
        string='Symptoms'
    )

    treatment = fields.Text(
        string='Treatment'
    )

    notes = fields.Text(
        string='Additional Notes'
    )