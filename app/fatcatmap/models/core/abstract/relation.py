from fatcatmap.models import Model, PolyModel, ndb


class GraphRelation(Model):

	''' Represents a computed, non-directional relationship between two points on the graph. '''

	objects = ndb.KeyProperty(repeated=True)
	score = ndb.FloatProperty(default=0.1)
	hints = ndb.KeyProperty(repeated=True)


class RelationReference(PolyModel):

	''' Represents an edge from a graph relation to another object, external or internal. '''

	name = ndb.StringProprety(indexed=True)


class ExternalID(RelationReference):

	''' Represents an external version of this same relation in another system. '''

	ext_id = ndb.StringProperty(indexed=True)
	service = ndb.StringProperty()
