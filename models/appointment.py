from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'

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

    appointment_date = fields.Datetime(
        string='Appointment Date',
        required=True
    )

    reason = fields.Text(
        string='Reason for Visit'
    )

    status = fields.Selection(
        [
            ('scheduled', 'Scheduled'),
            ('confirmed', 'Confirmed'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        string='Status',
        default='scheduled',
        required=True
    )

    notes = fields.Text(
        string='Notes'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    # =========================================================
    # Appointment Workflow
    # =========================================================

    def action_confirm(self):
        for record in self:
            record.status = 'confirmed'

    def action_complete(self):
        for record in self:
            record.status = 'completed'

    def action_cancel(self):
        for record in self:
            record.status = 'cancelled'

    def action_reset_to_scheduled(self):
        for record in self:
            record.status = 'scheduled'

    # =========================================================
    # Appointment Validation
    # =========================================================

    @api.constrains('appointment_date')
    def _check_appointment_date(self):

        for record in self:

            if record.appointment_date:

                if record.appointment_date < fields.Datetime.now():

                    raise ValidationError(
                        'Appointment date cannot be in the past.'
                    )

    @api.constrains('doctor_id', 'appointment_date')
    def _check_doctor_appointment(self):

        for record in self:

            if not record.doctor_id or not record.appointment_date:
                continue

            existing_appointment = self.search([
                ('id', '!=', record.id),
                ('doctor_id', '=', record.doctor_id.id),
                ('appointment_date', '=', record.appointment_date),
                ('active', '=', True),
            ], limit=1)

            if existing_appointment:

                raise ValidationError(
                    'This doctor already has an appointment at this time.'
                )