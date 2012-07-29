from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\snippets\\footer_left.html'

    def root(context, environment=environment):
        if 0: yield None
        template = environment.get_template('snippets/dev_warning.html', '/source\\snippets\\footer_left.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event

    blocks = {}
    debug_info = '1=8'
    return locals()