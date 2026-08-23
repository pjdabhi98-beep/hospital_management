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

    doctor_ids = fields.One2many(
        'hospital.doctor',
        'department_id',
        string='Doctors'
    )

    doctor_count = fields.Integer(
        string='Doctor Count',
        compute='_compute_doctor_count'
    )

    def _compute_doctor_count(self):
        for department in self:
            department.doctor_count = len(department.doctor_ids)