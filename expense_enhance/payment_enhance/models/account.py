# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class HrExpenseSheet(models.Model):
    _inherit = "account.payment"

    destination_account_id = fields.Many2one('account.account', domain=[('company_id', '=', 'company_id'), ('internal_type', '=', 'payable'), ('deprecated', '=', False)], readonly=False)
