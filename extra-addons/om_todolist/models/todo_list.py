from odoo import fields, models


class TodoList(models.Model):
    _name = "todo.list"
    _description = "Todo list"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    is_complete = fields.Boolean(string="Is Complete")
    parent_id = fields.Many2one(comodel_name='todo.lesson')
