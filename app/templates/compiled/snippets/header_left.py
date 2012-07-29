from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\snippets\\header_left.html'

    def root(context, environment=environment):
        if 0: yield None
        yield u"<div id='fcmlogo'>\n\t<img src='http://cdn.fatcatmap.com/branding/fatcatmap-alpha-v1-25.png' alt='fatcatmap! ^.^' />\n</div>"

    blocks = {}
    debug_info = ''
    return locals()