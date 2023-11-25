# -*- coding: utf-8 -*- 

import datetime

from odoo import models, fields, api, _
from odoo.exceptions import UserError

NON_START_STATES = ('pending','waiting','ready')

class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    allow_operation_dependencies = fields.Boolean('Operation Dependencies',related='production_bom_id.allow_operation_dependencies')


    def button_start(self):
        if not self._can_start():
            raise UserError(_("The work order depends on one or more work orders that have not yet started"))
        return super(MrpWorkorder,self).button_start()


    def _depends_on_other_operations(self):
        self.ensure_one()
        if self.allow_operation_dependencies:
            bom_operation = self.production_bom_id.operation_ids.filtered(lambda op:op.id == self.operation_id.id)
            return len(bom_operation.blocked_by_operation_ids) > 0
        return False


    def _can_start(self):
        if not self._depends_on_other_operations():
            return True
        if self.allow_operation_dependencies:
            dep_operations = self.production_bom_id.operation_ids.filtered(lambda op:op.id == self.operation_id.id).blocked_by_operation_ids
            workorders_states = dep_operations.mapped("workorder_ids").filtered(lambda wo:wo.production_id.id == self.production_id.id).mapped("state")
            if set(workorders_states).intersection(set(NON_START_STATES)):
                return False
        return True


