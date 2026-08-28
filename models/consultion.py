from odoo import models, fields


class HospitalConsultation(models.Model):
    _name = 'hospital.consultation'
    _description = 'Hospital Consultation'
    _order = 'consultation_date desc'

    name = fields.Char(
        string='Consultation Reference',
        required=True
    )

    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
        required=True
    )

    doctor_id = fields.Many2one(
        'hospital.doctor',
        string='Doctor',
        required=True
    )

    appointment_id = fields.Many2one(
        'hospital.appointment',
        string='Appointment'
    )

    consultation_date = fields.Datetime(
        string='Consultation Date',
        default=fields.Datetime.now,
        required=True
    )
    prescription_ids = fields.One2many(
    'hospital.prescription',
    'consultation_id',
    string='Prescriptions'
)

    symptoms = fields.Text(
        string='Symptoms'
    )

    diagnosis = fields.Text(
        string='Diagnosis'
    )

    notes = fields.Text(
        string='Doctor Notes'
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
        ],
        string='Status',
        default='draft',
        required=True
    )