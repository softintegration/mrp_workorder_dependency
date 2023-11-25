# -*- coding: utf-8 -*- 

import datetime

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
from odoo.tools import float_compare, float_round, float_is_zero
from odoo.tools import format_datetime


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    allow_operation_dependencies = fields.Boolean('Operation Dependencies',
                                                  help="Create operation level dependencies that will influence both planning and the status of work orders upon MO confirmation. If this feature is ticked, and nothing is specified, Odoo will assume that no dependency block the starting of operations."
                                                  )
