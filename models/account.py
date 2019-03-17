# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class AccountAccount(models.Model):
    _inherit = 'account.account'

    name = fields.Char(translate=True)
