from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\snippets\\header_right.html'

    def root(context, environment=environment):
        l_util = context.resolve('util')
        l_gravatarify = context.resolve('gravatarify')
        l_link = context.resolve('link')
        t_1 = environment.tests['none']
        if 0: yield None
        if (not t_1(context.call(environment.getattr(environment.getattr(environment.getattr(l_util, 'api'), 'users'), 'get_current_user')))):
            if 0: yield None
            yield u'\n<div id=\'authbox\'>\n\t<div id=\'userbox\' data-user-nickname=\'%s\'>\n\t\t<b><a href=\'#\'>Welcome back, %s!</a></b>\n\t\t<img src="%s" alt=\'you!\' />\n\t</div>\n</div>\n' % (
                context.call(environment.getattr(context.call(environment.getattr(environment.getattr(environment.getattr(l_util, 'api'), 'users'), 'get_current_user')), 'nickname')), 
                context.call(environment.getattr(context.call(environment.getattr(environment.getattr(environment.getattr(l_util, 'api'), 'users'), 'get_current_user')), 'nickname')), 
                context.call(l_gravatarify, context.call(environment.getattr(context.call(environment.getattr(environment.getattr(environment.getattr(l_util, 'api'), 'users'), 'get_current_user')), 'email')), 'jpg', 32), 
            )
        else:
            if 0: yield None
            yield u'\n<div id=\'authbox\'>\n\t<b><a href=\'%s\' title="log in!">log in!</a></b>\n\t<b><a href=\'%s\'>about fatcatmap</a></b>\n</div>\n' % (
                context.call(l_link, 'auth/login'), 
                context.call(l_link, 'about'), 
            )

    blocks = {}
    debug_info = '1=12&3=15&4=16&5=17&10=22&11=23'
    return locals()