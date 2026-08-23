from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(
        string='Doctor Name',
        required=True
    )

    specialization = fields.Char(
        string='Specialization'
    )

    phone = fields.Char(
        string='Phone'
    )

    email = fields.Char(
        string='Email'
    )

    license_number = fields.Char(
        string='License Number'
    )

    experience = fields.Integer(
        string='Experience'
    )

    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other'),
        ],
        string='Gender'
    )

    joining_date = fields.Date(
        string='Joining Date'
    )

    is_available = fields.Boolean(
        string='Available',
        default=True
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    appointment_ids = fields.One2many(
        'hospital.appointment',
        'doctor_id',
        string='Appointments'
    )