from odoo import models, fields, api, _
from odoo.exceptions import UserError

class RegistrasiMaterial(models.Model):
    _name = 'registrasi.material'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Registrasi Material'

    name = fields.Char(string='Name')
    material_code = fields.Char(string='Material Code', required=True)
    material_name = fields.Char(string='Material Name', required=True)
    material_type = fields.Selection([('fabric','Fabric'),('jeans','Jeans'),('cotton','Cotton')], string='Material Type', required=True)
    material_buy_price = fields.Float(string='Material Buy Price', required=True)
    supplier_id = fields.Many2one('res.partner', string='Related Supplier', required=True)

    @api.constrains('material_buy_price')
    def constrains_material_buy_price(self):
        for rec in self:
            if rec.material_buy_price and rec.material_buy_price < 100:
                raise UserError('Mohon maaf material buy price tidak boleh < 100')
    