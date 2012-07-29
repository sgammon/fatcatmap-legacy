class Node extends Model

class Graph extends Model

class GraphController extends Controller

    @mount = 'graph'
    @events = []
    @proxies = []

    constructor: (fcm, window) ->

        return


@__fcm_preinit.abstract_base_classes.push Node
@__fcm_preinit.abstract_base_classes.push Graph
@__fcm_preinit.abstract_base_controllers.push GraphController