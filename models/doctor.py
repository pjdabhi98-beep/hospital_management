from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(
        string='Doctor Name',
        required=True
    )

    email = fields.Char(
        string='Email'
    )

    phone = fields.Char(
        string='Phone'
    )

    specialization = fields.Char(
        string='Specialization'
    )

    license_number = fields.Char(
        string='License Number'
    )

    experience = fields.Integer(
        string='Years of Experience'
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
        string='Available for Appointments',
        default=True
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )