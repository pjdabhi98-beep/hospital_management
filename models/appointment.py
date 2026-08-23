from odoo import models, fields


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

    def action_confirm(self):
        """Confirm the appointment."""
        for record in self:
            record.status = 'confirmed'

    def action_complete(self):
        """Mark the appointment as completed."""
        for record in self:
            record.status = 'completed'

    def action_cancel(self):
        """Cancel the appointment."""
        for record in self:
            record.status = 'cancelled'

    def action_reset_to_scheduled(self):
        """Reset the appointment to scheduled."""
        for record in self:
            record.status = 'scheduled'