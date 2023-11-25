# -*- coding: utf-8 -*- 

import datetime

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
from odoo.tools import float_compare, float_round, float_is_zero
from odoo.tools import format_datetime


class MrpRoutingWorkcenter(models.Model):
    _inherit = 'mrp.routing.workcenter'

    allow_operation_dependencies = fields.Boolean(related='bom_id.allow_operation_dependencies')
    blocked_by_operation_ids = fields.Many2many('mrp.routing.workcenter',
                                                relation="mrp_routing_workcenter_dependencies_rel",
                                                column1="operation_id", column2="blocked_by_id",
                                                string="Blocked By",
                                                help="Operations that need to be completed before this operation can start.",
                                                domain="[('allow_operation_dependencies', '=', True), ('id', '!=', id), ('bom_id', '=', bom_id)]",
                                                copy=False)
