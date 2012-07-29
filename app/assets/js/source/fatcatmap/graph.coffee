## FatCatMap grapher classes & controllers
# core graph classes
class Node extends Model
    model:
        label: String()
        native: String()
        owner: String()
        scope: Array()

class Edge extends Model
    model:
        source: String()
        target: String()
        partner: String()

class EdgeItem extends Model
    model:
        edge: String()
        partner: String()

class Graph extends Model
class ConstructedGraph extends Model

# abstract objects
class GraphObject extends Model
    model:
        label: String()
        nodes: Array()
        primary: String()

class ObjectReference extends Model
class ExternalObjectID extends ObjectReference
    model:
        name: String()
        ext_id: String()
        service: String()

# abstract relations
class GraphRelation extends Model
    model:
        objects: Array()
        score: Number()
        hints: Array()

class RelationReference extends Model
class ExternalRelationID extends RelationReference
    model:
        name: String()
        ext_id: String()
        service: String()

class GraphController extends Controller

    @mount = 'graph'
    @events = []
    @proxies = []

    constructor: (fcm, window) ->

        return


@__fcm_preinit.abstract_base_classes.push Node
@__fcm_preinit.abstract_base_classes.push Edge
@__fcm_preinit.abstract_base_classes.push EdgeItem
@__fcm_preinit.abstract_base_classes.push Graph
@__fcm_preinit.abstract_base_classes.push ConstructedGraph

@__fcm_preinit.abstract_base_classes.push GraphObject
@__fcm_preinit.abstract_base_classes.push ObjectReference
@__fcm_preinit.abstract_base_classes.push ExternalObjectID

@__fcm_preinit.abstract_base_classes.push GraphRelation
@__fcm_preinit.abstract_base_classes.push RelationReference
@__fcm_preinit.abstract_base_classes.push ExternalRelationID

@__fcm_preinit.abstract_base_controllers.push GraphController