from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HospitalPrescription(models.Model):
    _name = 'hospital.prescription'
    _description = 'Hospital Prescription'
    _order = 'date desc'

   
    name = fields.Char(
    string='Prescription Reference',
    default='New',
    readonly=True,
    copy=False
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
        string='Duration (Days)',
        required=True
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        string='Status',
        default='draft',
        required=True
    )
    consultation_id = fields.Many2one(
        'hospital.consultation',
        string='Consultation',
        ondelete='set null'
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'hospital.prescription'
                )       or 'New'

        return super().create(vals_list)

    @api.constrains('name')
    def _check_prescription_name(self):
        for record in self:
            existing = self.search([
                ('name', '=', record.name),
                ('id', '!=', record.id)
            ], limit=1)

            if existing:
                raise ValidationError(
                    'Prescription reference must be unique.'
                )

    @api.constrains('duration')
    def _check_duration(self):
        for record in self:
            if record.duration <= 0:
                raise ValidationError(
                    'Duration must be greater than 0 days.'
                )

    @api.constrains('date')
    def _check_prescription_date(self):
        for record in self:
            if record.date and record.date < fields.Date.today():
                raise ValidationError(
                    'Prescription date cannot be in the past.'
                )

    def action_confirm(self):
        for record in self:
            record.state = 'confirmed'

    def action_complete(self):
        for record in self:
            record.state = 'completed'

    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'

    def action_reset_to_draft(self):
        for record in self:
            record.state = 'draft'