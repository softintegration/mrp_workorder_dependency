# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_mrp_workorder_dependencies = fields.Boolean("Work Order Dependencies", implied_group="mrp_workorder_dependency.group_mrp_workorder_dependencies")