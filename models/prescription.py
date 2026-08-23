from odoo import models, fields


class HospitalPrescription(models.Model):
    _name = 'hospital.prescription'
    _description = 'Hospital Prescription'
    _order = 'date desc'

    name = fields.Char(
        string='Prescription Reference',
        required=True
    )

    date = fields.Date(
        string='Date',
        required=True,
        default=fields.Date.today
    )

    medicine = fields.Text(
        string='Medicines',
        required=True
    )

    instructions = fields.Text(
        string='Instructions'
    )

    duration = fields.Integer(
        string='Duration (Days)'
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('completed', 'Completed'),
        ],
        string='Status',
        default='draft',
        required=True
    )

    def action_confirm(self):
        for record in self:
            record.state = 'confirmed'

    def action_complete(self):
        for record in self:
            record.state = 'completed'

    def action_reset_to_draft(self):
        for record in self:
            record.state = 'draft'