# -*- coding: utf-8 -*

from odoo.addons.bus.controllers.main import BusController
from odoo.http import request


class VoipBusController(BusController):
    # --------------------------
    # Extends BUS Controller Poll
    # --------------------------
    def _poll(self, dbname, channels, last, options):
        if request.session.uid:
            channels.append((request.db, 'voip.room', request.env.user.partner_id.id))
        return super(VoipBusController, self)._poll(dbname, channels, last, options)