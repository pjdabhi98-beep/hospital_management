from odoo import models, fields, api
from odoo.exceptions import ValidationError


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

    @api.constrains('name')
    def _check_department_name(self):
        for record in self:
            existing = self.search([
                ('name', '=', record.name),
                ('id', '!=', record.id)
            ], limit=1)

            if existing:
                raise ValidationError(
                    'Department name must be unique.'
                )

    @api.constrains('code')
    def _check_department_code(self):
        for record in self:
            existing = self.search([
                ('code', '=', record.code),
                ('id', '!=', record.id)
            ], limit=1)

            if existing:
                raise ValidationError(
                    'Department code must be unique.'
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