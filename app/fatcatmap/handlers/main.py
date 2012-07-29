# -*- coding: utf-8 -*-
from fatcatmap.handlers import WebHandler


class Landing(WebHandler):

    ''' Returns the age-old, enigmatic success response. '''

    def get(self):

        ''' Render the template at "app/templates/main/mapper.html". '''

        self.render('main/mapper.html')
        return
