from odoo import models, fields


class HospitalDepartment(models.Model):
    _name = 'hospital.department'
    _description = 'Hospital Department'
    _order = 'name'

    name = fields.Char(
        string='Department Name',
        required=True
    )

    code = fields.Char(
        string='Department Code',
        required=True
    )

    description = fields.Text(
        string='Description'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('active', 'Active'),
            ('inactive', 'Inactive'),
        ],
        string='Status',
        default='draft',
        required=True
    )

    def action_activate(self):
        for record in self:
            record.state = 'active'
            record.active = True

    def action_deactivate(self):
        for record in self:
            record.state = 'inactive'
            record.active = False

    def action_reset_to_draft(self):
        for record in self:
            record.state = 'draft'