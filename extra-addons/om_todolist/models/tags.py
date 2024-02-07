from odoo import fields, models


class TodoTags(models.Model):
    _name = "todo.tags"
    _description = "Todo tags"

    name = fields.Char(string="name")
