from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source\\snippets\\mapper.html'

    def root(context, environment=environment):
        if 0: yield None
        yield u"<script>\n(function (w) { w._buildGraph = function () {\n\n\tvar mapper = document.getElementById('mapper'),\n\t\theight = mapper.scrollHeight,\n\t\twidth = mapper.scrollWidth,\n\t\tcolor = d3.scale.category20(),\n\t\tforce = d3.layout.force()\n\t\t\t.charge(-120)\n\t\t\t.linkDistance(30)\n\t\t\t.size([width, height]),\n\t\tsvg = d3.select('#mapper').append('svg')\n\t\t\t.attr('width', width)\n\t\t\t.attr('height', height);\n\n\t\td3.json('/assets/ext/static/miserables.json', function (json) {\n\t\t\t\n\t\t\tforce\n\t\t\t\t.nodes(json.nodes)\n\t\t\t\t.links(json.links)\n\t\t\t\t.start();\n\t\t\t\n\t\t\tvar link = svg.selectAll('line.link')\n\t\t\t\t.data(json.links)\n\t\t\t\t.enter().append('line')\n\t\t\t\t\t.attr('class', 'link')\n\t\t\t\t\t.style('stroke-width', function (d) { return Math.sqrt(d.value); });\n\n\t\t\tvar node = svg.selectAll('circle.node')\n\t\t\t\t.data(json.nodes)\n\t\t\t\t.enter().append('circle')\n\t\t\t\t\t.attr('class', 'node')\n\t\t\t\t\t.attr('r', 5)\n\t\t\t\t\t.style('fill', function (d) { return color(d.group); })\n\t\t\t\t\t.call(force.drag);\n\n\t\t\t\tnode.append('title').text(function (d) { return d.name; });\n\n\t\t\t\tforce.on('tick', function () {\n\n\t\t\t\t\tlink.attr('x1', function (d) { return d.source.x; })\n\t\t\t\t\t\t.attr('y1', function (d) { return d.source.y; })\n\t\t\t\t\t\t.attr('x2', function (d) { return d.target.x; })\n\t\t\t\t\t\t.attr('y2', function (d) { return d.target.y; });\n\n\t\t\t\t\tnode.attr('cx', function (d) { return d.x; })\n\t\t\t\t\t\t.attr('cy', function (d) { return d.y; });\n\n\t\t\t\t});\n\t\t});\n\n}})(window);\n</script>"

    blocks = {}
    debug_info = ''
    return locals()