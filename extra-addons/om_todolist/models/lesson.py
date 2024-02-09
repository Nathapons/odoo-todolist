from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class TodoLesson(models.Model):
    _name = "todo.lesson"
    _description = "Todo lesson"

    title = fields.Char(string="Title")
    tags = fields.Many2many('todo.tags', string="Tags")
    track_status = fields.Selection(
        [
            ('draft', 'Draft'),
            ('in_progress', 'In Progress'),
            ('complete', 'Complete'),
        ],
        string="Track Status",
        default='draft',
    )
    todo_list = fields.One2many(
        string="List", comodel_name='todo.list', inverse_name='parent_id'
    )
    users = fields.Many2many('res.users', string="Attendee")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    is_complete = fields.Boolean(string="Is Complete?")

    def action_click_progress(self):
        self.track_status = 'in_progress'

    def action_click_done(self):
        self.track_status = 'complete'

    @api.constrains('start_date', 'end_date')
    def _check_date(self):
        if self.start_date > self.end_date:
            raise ValidationError(_("Start date is less than end date"))

    @api.onchange('todo_list')
    def _onchange_todo_list(self):
        data = [todo.is_complete for todo in self.todo_list]
        self.is_complete = data and all(data)

    def write(self, record_list):
        if self.track_status != 'complete':
            return super().write(record_list)
        else:
            raise ValidationError(_("Cannot edit complete document"))
