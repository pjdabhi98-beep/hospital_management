from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    # =========================================================
    # Basic Patient Information
    # =========================================================

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

    # =========================================================
    # Personal Information
    # =========================================================

    date_of_birth = fields.Date(
        string='Date of Birth'
    )

    age = fields.Integer(
        string='Age',
        compute='_compute_age',
        store=True
    )

    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other'),
        ],
        string='Gender'
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

    # =========================================================
    # Patient Status
    # =========================================================

    is_emergency = fields.Boolean(
        string='Emergency Patient',
        default=False
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    # =========================================================
    # Patient → Appointment Relationship
    # =========================================================

    appointment_ids = fields.One2many(
        'hospital.appointment',
        'patient_id',
        string='Appointments'
    )

    # =========================================================
    # Compute Age
    # =========================================================

    @api.depends('date_of_birth')
    def _compute_age(self):

        today = fields.Date.today()

        for record in self:

            if record.date_of_birth:

                record.age = (
                    today.year
                    - record.date_of_birth.year
                    - (
                        (today.month, today.day)
                        <
                        (
                            record.date_of_birth.month,
                            record.date_of_birth.day
                        )
                    )
                )

            else:
                record.age = 0

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        today = fields.Date.today()

        for record in self:
            if record.date_of_birth and record.date_of_birth > today:
                raise ValidationError(
                'Date of birth cannot be in the future.'
            )

    @api.constrains('phone')
    def _check_phone(self):
        for record in self:

            if record.phone:

                phone = record.phone.strip()

                if not re.match(r'^[0-9+\-\s()]+$', phone):
                    raise ValidationError(
                    'Please enter a valid phone number.'
                )

    @api.constrains('email')
    def _check_email(self):
        for record in self:

            if record.email:

                email = record.email.strip()

                pattern = r'^[^@\s]+@[^@\s]+\.[^@\s]+$'

                if not re.match(pattern, email):
                    raise ValidationError(
                    'Please enter a valid email address.'
                )

    # =========================================================
    # Smart Button → Appointments
    # =========================================================

    def action_view_appointments(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'view_mode': 'list,form',
            'domain': [
                ('patient_id', '=', self.id)
            ],
            'context': {
                'default_patient_id': self.id,
            },
        }