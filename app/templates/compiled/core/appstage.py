from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\core\\appstage.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/base_web.html', '/source\\core\\appstage.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_frame(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t'

    def block_main(context, environment=environment):
        if 0: yield None
        yield u"\n<div id='stage' class='fixed app'>\n\t"
        for event in context.blocks['stage'][0](context):
            yield event
        yield u"\n\n\t<div id='panes'>\n\t\t"
        for event in context.blocks['frame'][0](context):
            yield event
        yield u"\n\t</div><!-- end #panes -->\n</div><!-- end #stage -->'\n"

    def block_stage(context, environment=environment):
        if 0: yield None
        yield u'\n\t'

    blocks = {'frame': block_frame, 'main': block_main, 'stage': block_stage}
    debug_info = '1=9&9=15&3=19&5=22&9=25&5=29'
    return locals()