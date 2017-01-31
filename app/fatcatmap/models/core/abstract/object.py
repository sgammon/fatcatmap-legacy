from fatcatmap.models import Model, PolyModel, ndb


class GraphObject(Model):

	''' Represents a known datapoint on the graph. '''

	label = ndb.StringProperty()
	nodes = ndb.KeyProperty(repeated=True)
	primary = ndb.KeyProperty()


class ObjectReference(PolyModel):

	''' Represents an edge from a graph object to another object, external or internal. '''

	name = ndb.StringProperty()


class ExternalID(ObjectReference):

	''' Represents an external version of this same datapoint in another system. '''

	ext_id = ndb.StringProperty()
	service = ndb.StringProperty()
