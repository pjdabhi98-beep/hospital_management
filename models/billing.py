from odoo import models, fields, api


class HospitalBilling(models.Model):
    _name = 'hospital.billing'
    _description = 'Hospital Billing'
    _order = 'billing_date desc'

    name = fields.Char(
        string='Bill Number',
        required=True,
        default='New'
    )

    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
        required=True,
        ondelete='restrict'
    )

    billing_date = fields.Date(
        string='Billing Date',
        required=True,
        default=fields.Date.today
    )

    description = fields.Text(
        string='Description'
    )

    amount = fields.Float(
        string='Amount',
        required=True
    )

    payment_method = fields.Selection(
        [
            ('cash', 'Cash'),
            ('card', 'Card'),
            ('upi', 'UPI'),
            ('bank', 'Bank Transfer'),
        ],
        string='Payment Method',
        required=True,
        default='cash'
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('paid', 'Paid'),
            ('cancelled', 'Cancelled'),
        ],
        string='Status',
        default='draft',
        required=True
    )

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'hospital.billing'
            ) or 'New'
        return super().create(vals)

    def action_confirm(self):
        for record in self:
            record.state = 'paid'

    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'

    def action_reset_to_draft(self):
        for record in self:
            record.state = 'draft'