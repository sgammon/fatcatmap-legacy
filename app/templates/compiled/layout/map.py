from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\layout\\map.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/appstage.html', '/source\\layout\\map.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_mapper(context, environment=environment):
        if 0: yield None

    def block_frame(context, environment=environment):
        if 0: yield None
        yield u"\n\t<!-- Data/View Context -->\n\t<div id='context'>\n\t\t"
        for event in context.blocks['context'][0](context):
            yield event
        yield u"\n\t</div><!-- end #context -->\n\n\t<!-- Controls/Visualizer Navigation -->\n\t<div id='controls'>\n\t\t"
        for event in context.blocks['controls'][0](context):
            yield event
        yield u'\n\t</div><!-- end #controls -->\n'

    def block_controls(context, environment=environment):
        if 0: yield None

    def block_context(context, environment=environment):
        if 0: yield None

    def block_stage(context, environment=environment):
        if 0: yield None
        yield u"\n\t<div id='mapper' data-role='visualizer' data-type='graph'>\n\t\t"
        for event in context.blocks['mapper'][0](context):
            yield event
        yield u'\n\t</div><!-- close #mapper -->\n'

    blocks = {'mapper': block_mapper, 'frame': block_frame, 'controls': block_controls, 'context': block_context, 'stage': block_stage}
    debug_info = '1=9&5=15&9=18&12=21&17=24&12=31&3=34&5=37'
    return locals()