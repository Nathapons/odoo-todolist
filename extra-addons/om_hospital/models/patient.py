from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = 'mail.thread'

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    is_child = fields.Boolean(string="Is Child ?", tracking=True)
    notes = fields.Text(string="Notes")
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('other', 'Others')],
        string="Gender",
        tracking=True,
    )
    capitalized_name = fields.Char(
        string='Capitalized Name',
        compute='_compute_capitalized_name',
        store=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['gender'] = 'female'
        return super().create(vals_list)

    @api.constrains('is_child', 'age')
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_("Age has to be recorded !"))

    @api.depends('name')
    def _compute_capitalized_name(self):
        if self.name:
            self.capitalized_name = self.name.upper()
        else:
            self.capitalized_name = ''

    @api.onchange('age')
    def _onchange_age(self):
        self.is_child = self.age <= 10
