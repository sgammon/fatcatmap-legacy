from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\core\\__south.html'

    def root(context, environment=environment):
        l_asset = context.resolve('asset')
        l_page = context.resolve('page')
        if 0: yield None
        yield u'<script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>\n<script>window.jQuery || document.write(\'<script src="%s"><\\/script>\')</script>\n\n<!-- Core Scripts -->\n<script src="%s"></script>\n<script src="%s"></script>\n\n<!-- Base Scripts -->\n<script src="/_ah/channel/jsapi"></script>\n<script src="%s"></script>\n\n' % (
            context.call(environment.getattr(l_asset, 'script'), 'jquery', 'core'), 
            context.call(environment.getattr(l_asset, 'script'), 'modernizr', 'core'), 
            context.call(environment.getattr(l_asset, 'script'), 'underscore', 'core'), 
            context.call(environment.getattr(l_asset, 'script'), 'base', 'apptools'), 
        )
        if (environment.getattr(l_page, 'services') or environment.getattr(l_page, 'analytics')):
            if 0: yield None
            yield u'<script>\n'
            for event in context.blocks['page_services'][0](context):
                yield event
            yield u'\n\n'
            for event in context.blocks['page_analytics'][0](context):
                yield event
            yield u'\n</script>'

    def block_page_services(context, environment=environment):
        l_build_page_object = context.resolve('build_page_object')
        l_page = context.resolve('page')
        if 0: yield None
        if environment.getattr(l_page, 'services'):
            if 0: yield None
            included_template = environment.get_template('macros/page_object.js', '/source\\core\\__south.html').module
            l_build_page_object = getattr(included_template, 'build_page_object', missing)
            if l_build_page_object is missing:
                l_build_page_object = environment.undefined("the template %r (imported on line 17 in '/source\\\\core\\\\__south.html') does not export the requested name 'build_page_object'" % included_template.__name__, name='build_page_object')
            yield u'\n\t'
            yield to_string(context.call(l_build_page_object, environment.getattr(environment.getattr(l_page, 'services'), 'services_manifest'), environment.getattr(environment.getattr(l_page, 'services'), 'config'), l_page))

    def block_page_analytics(context, environment=environment):
        l_util = context.resolve('util')
        l_google_analytics_async = context.resolve('google_analytics_async')
        l_page = context.resolve('page')
        if 0: yield None
        if (not environment.getattr(environment.getattr(l_util, 'config'), 'debug')):
            if 0: yield None
            if environment.getattr(l_page, 'analytics'):
                if 0: yield None
                included_template = environment.get_template('macros/page_analytics.js', '/source\\core\\__south.html').module
                l_google_analytics_async = getattr(included_template, 'google_analytics_async', missing)
                if l_google_analytics_async is missing:
                    l_google_analytics_async = environment.undefined("the template %r (imported on line 25 in '/source\\\\core\\\\__south.html') does not export the requested name 'google_analytics_async'" % included_template.__name__, name='google_analytics_async')
                yield u'\n\t\t'
                yield to_string(context.call(l_google_analytics_async, environment.getattr(l_page, 'analytics')))

    blocks = {'page_services': block_page_services, 'page_analytics': block_page_analytics}
    debug_info = '2=11&5=12&6=13&10=14&13=16&15=19&22=22&15=26&16=30&17=32&18=37&22=39&23=44&24=46&25=48&26=53'
    return locals()