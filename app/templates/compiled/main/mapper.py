from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\main\\mapper.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layout/map.html', '/source\\main\\mapper.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_mapper(context, environment=environment):
        if 0: yield None
        yield u'\n\t'
        template = environment.get_template('snippets/mapper.html', '/source\\main\\mapper.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n'

    def block_postsouth(context, environment=environment):
        if 0: yield None
        yield u'\n<script>\n$(document).ready(function () {\n\twindow._buildGraph();\n});\n</script>\n'

    blocks = {'mapper': block_mapper, 'postsouth': block_postsouth}
    debug_info = '1=9&3=15&4=18&7=23'
    return locals()