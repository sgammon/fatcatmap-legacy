from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\core\\base_web.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/__base.html', '/source\\core\\base_web.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_body(context, environment=environment):
        if 0: yield None
        yield u"\n\n<!-- App DOM Resources -->\n<div id='resources' class='hidden resource root'>\n\n\t<div id='templates' class='hidden template root'>\n\n\t</div><!-- end #templates -->\n\n</div><!-- end #resources -->\n\n<!-- App Container -->\n<div id='main' class='fatcatmap-app fcm-light'>\n\t"
        for event in context.blocks['header'][0](context):
            yield event
        yield u'\n\n\t'
        for event in context.blocks['main'][0](context):
            yield event
        yield u'\n\n\t'
        for event in context.blocks['footer'][0](context):
            yield event
        yield u'\n</div><!-- close #main -->\n\n'

    def block_footer_right(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t\t\t\t'
        template = environment.get_template('snippets/footer_right.html', '/source\\core\\base_web.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n\t\t\t\t'

    def block_footer(context, environment=environment):
        if 0: yield None
        yield u"\n\t\t<footer><!-- app footer -->\n\t\t\t<div class='footer-region left'>\n\t\t\t\t"
        for event in context.blocks['footer_left'][0](context):
            yield event
        yield u"\n\t\t\t</div><!-- close .footer-region.left -->\n\n\t\t\t<div class='footer-region right'>\n\t\t\t\t"
        for event in context.blocks['footer_right'][0](context):
            yield event
        yield u'\n\t\t\t</div><!-- close .footer-region.right -->\n\t\t</footer><!-- end footer -->\n\t'

    def block_header_right(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t\t\t\t'
        template = environment.get_template('snippets/header_right.html', '/source\\core\\base_web.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n\t\t\t\t'

    def block_header(context, environment=environment):
        if 0: yield None
        yield u"\n\t\t<header><!-- app header -->\n\t\t\t<div class='header-region left'>\n\t\t\t\t"
        for event in context.blocks['header_left'][0](context):
            yield event
        yield u"\n\t\t\t</div><!-- close .header-region.left -->\n\n\t\t\t<div class='header-region right'>\n\t\t\t\t"
        for event in context.blocks['header_right'][0](context):
            yield event
        yield u'\n\t\t\t</div><!-- close .header-region.right -->\n\t\t</header><!-- close header -->\n\t'

    def block_header_left(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t\t\t\t'
        template = environment.get_template('snippets/header_left.html', '/source\\core\\base_web.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n\t\t\t\t'

    def block_main(context, environment=environment):
        if 0: yield None
        yield u'\n\t'

    def block_footer_left(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t\t\t\t'
        template = environment.get_template('snippets/footer_left.html', '/source\\core\\base_web.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n\t\t\t\t'

    blocks = {'body': block_body, 'footer_right': block_footer_right, 'footer': block_footer, 'header_right': block_header_right, 'header': block_header, 'header_left': block_header_left, 'main': block_main, 'footer_left': block_footer_left}
    debug_info = '1=9&3=15&16=18&32=21&35=24&44=28&45=31&35=36&38=39&44=42&25=46&26=49&16=54&19=57&25=60&19=64&20=67&32=72&38=76&39=79'
    return locals()