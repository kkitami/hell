from odoo import api,fields, models
from ..send import notify_employee, create_lead_message

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    employee_id = fields.Many2one('hr.employee', string='Employee')

    def create(self, vals):
        lead = super(CrmLead, self).create(vals)
        if lead.employee_id.telegram_id:
            try:
                message = create_lead_message('Назначен новый исполнитель', lead)
                notify_employee(lead.employee_id.telegram_id, message)
            except Exception as e:
                print(e)
        return lead
    def write(self, vals):
        res = super(CrmLead, self).write(vals)
        if 'employee_id' in vals:
            old_employee_id = self.env['hr.employee'].browse(self.employee_id.id)
            new_employee_id = self.env['hr.employee'].browse(vals['employee_id'])

            if new_employee_id.telegram_id and old_employee_id.id != new_employee_id.id:
                message_new = create_lead_message('Вы назначены новым исполнителем', self)
                notify_employee(new_employee_id.telegram_id, message=message_new)
                if old_employee_id.telegram_id:
                    message_old = create_lead_message('Изменен исполнитель', self)
                    notify_employee(old_employee_id.telegram_id, message=message_old)

        if any(field_name in vals for field_name in ['street', 'street2', 'city', 'zip', 'state_id', 'country_id']):
            employee_id = self.employee_id
            if employee_id.telegram_id:
                message = create_lead_message('Изменен адрес', self)
                notify_employee(employee_id.telegram_id, message=message)

        return res

