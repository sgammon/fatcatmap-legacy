# -*- coding: utf-8 -*-

'''

Project Handlers

This module is where you put your project's RequestHandlers. WebHandler and MobileHandler
are designed to be extended by your app's handlers. This gives you a chance to inject custom
logic / request handling stuff across your entire app, by putting it here.

-sam (<sam@momentum.io>)

'''

## AppTools Imports
import config
import hashlib
import webapp2
from apptools.core import BaseHandler


class WebHandler(BaseHandler):

    ''' Handler for desktop web requests. '''

    @webapp2.cached_property
    def _webHandlerConfig(self):

        ''' Cached access to this handler's config. '''

        return config.config.get('fatcatmap.classes.WebHandler')

    @webapp2.cached_property
    def _integrationConfig(self):

        ''' Cached access to this handler's integration config. '''

        return self._webHandlerConfig.get('integrations')

    def head(self):

        ''' Run GET, if defined, and return the headers only. '''

        if hasattr(self, 'get'):
            self.get()
        return

    def _bindRuntimeTemplateContext(self, context):

        ''' Bind a bunch of utils-n-stuff at runtime. '''

        context.update({

            'gravatarify': lambda email, ext, size: ''.join([
                    ':'.join([self.request.environ.get('wsgi.url_scheme', 'http'), '//']),
                    '/'.join([self._integrationConfig.get('gravatar').get('endpoints').get((self.force_https_assets == True and 'https' or self.request.environ.get('wsgi.url_scheme', 'http').lower())),
                        'avatar',
                        hashlib.md5(email).hexdigest()]),
                    '.%s' % ext,
                    '?s=%s&d=%s://lyr9.net/img/default-profile.png?s=%s' % (size, (self.force_https_assets == True and 'https' or self.request.environ.get('wsgi.url_scheme', 'http').lower()), size)
            ]),

        })

        return super(WebHandler, self)._bindRuntimeTemplateContext(context)


class MobileHandler(BaseHandler):

    ''' Handler for mobile web requests. '''
