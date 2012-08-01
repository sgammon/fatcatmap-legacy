# -*- coding: utf-8 -*-
from fatcatmap.handlers import WebHandler


class Login(WebHandler):

    ''' Default login handler - redirect using App Engine's users API, if available. '''

    def get(self):

        if hasattr(self, 'force_hostname') and getattr(self, 'force_hostname'):
            hostname = self.force_hostname
        else:
            hostname = self.request.host
        if hasattr(self, 'force_https_assets') and getattr(self, 'force_https_assets'):
            protocol = 'https'
        else:
            protocol = self.request.environ.get('HTTP_SCHEME', 'http')

        referrer = self.request.environ.get('HTTP_REFERRER', '/')
        if referrer != '/':
            referrer_path = '/'.join(str(referrer.split('//')[1:][0]).split('/')[1:])
        else:
            referrer_path = ''
        redirect_path = '/'.join(['://'.join([protocol, hostname]), referrer_path])

        try:
            login_url = self.api.users.create_login_url(redirect_path)
            if login_url is not None:
                return self.redirect(login_url)

        except:
            self.error(404)
            return


class Logout(WebHandler):

    ''' Default logout handler - redirect using App Engine's users API, if available. '''

    def get(self):

        try:
            logout_url = self.api.users.create_logout_url(self.request.environ.get('HTTP_REFERRER', '/'))
            if logout_url is not None:
                return self.redirect(logout_url)

        except:
            self.error(404)
            return


class Signup(WebHandler):

    ''' Default signup handler - return 404 by default. '''

    def get(self):
        pass
