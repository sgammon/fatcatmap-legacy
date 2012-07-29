from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\snippets\\dev_warning.html'

    def root(context, environment=environment):
        if 0: yield None
        yield u'<div id=\'dev_warning\'>\n\t<b>TECHNOLOGY PREVIEW</b> - copyright (&copy;) 2012, <a href="http://momentum.io">momentum labs</a>\n</div>'

    blocks = {}
    debug_info = ''
    return locals()