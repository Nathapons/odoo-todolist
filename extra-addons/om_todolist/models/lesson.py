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

    def action_click_progress(self):
        self.track_status = 'in_progress'

    @api.model_create_multi
    def create(self, record_list):
        for record in record_list:
            todo_records = []
            for todo_rows in record['todo_list']:
                data = todo_rows[-1]
                if isinstance(data, dict):
                    todo_records.append(data.get('is_complete'))

            if todo_records and all(todo_records):
                record['track_status'] = 'complete'

        return super().create(record_list)

    def write(self, record_list):
        print(self.track_status)
        if self.track_status != 'complete':
            return super().write(record_list)
        else:
            raise ValidationError(_("Cannot edit complete document"))
