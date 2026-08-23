from odoo import models, fields


class HospitalMedicalHistory(models.Model):
    _name = 'hospital.medical.history'
    _description = 'Hospital Medical History'

    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
        required=True
    )

    doctor_id = fields.Many2one(
        'hospital.doctor',
        string='Doctor'
    )

    diagnosis = fields.Char(
        string='Diagnosis',
        required=True
    )

    description = fields.Text(
        string='Description'
    )

    treatment = fields.Text(
        string='Treatment'
    )

    date = fields.Date(
        string='Date',
        default=fields.Date.today
    )

    is_current = fields.Boolean(
        string='Current Condition',
        default=True
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )