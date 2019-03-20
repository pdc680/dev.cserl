# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class HrExpenseSheet(models.Model):
    _inherit = "hr.expense.sheet"

    expense_line_ids = fields.One2many('hr.expense', 'sheet_id', string='Expense Lines',
                                       states={'done': [('readonly', True)], 'post': [('readonly', True)]}, copy=False)
