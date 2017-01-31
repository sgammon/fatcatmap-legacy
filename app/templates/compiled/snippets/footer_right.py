from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\snippets\\footer_right.html'

    def root(context, environment=environment):
        if 0: yield None
        yield u'<div id=\'mm\'>\n\t<img src="/assets/img/static/branding/momentum-small-ddd-v1.png" alt=\'made with momentum :)\' />\n</div>'

    blocks = {}
    debug_info = ''
    return locals()