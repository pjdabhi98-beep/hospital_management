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