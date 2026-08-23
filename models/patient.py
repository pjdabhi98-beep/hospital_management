from odoo import models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(
        string='Patient Name',
        required=True
    )

    email = fields.Char(
        string='Email'
    )

    phone = fields.Char(
        string='Phone'
    )

    age = fields.Integer(
        string='Age'
    )

    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other'),
        ],
        string='Gender'
    )

    date_of_birth = fields.Date(
        string='Date of Birth'
    )

    blood_group = fields.Selection(
        [
            ('a+', 'A+'),
            ('a-', 'A-'),
            ('b+', 'B+'),
            ('b-', 'B-'),
            ('ab+', 'AB+'),
            ('ab-', 'AB-'),
            ('o+', 'O+'),
            ('o-', 'O-'),
        ],
        string='Blood Group'
    )

    is_emergency = fields.Boolean(
        string='Emergency Patient'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    appointment_ids = fields.One2many(
        'hospital.appointment',
        'patient_id',
        string='Appointments'
    )