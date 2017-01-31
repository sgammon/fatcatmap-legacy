from fatcatmap.models import Model, PolyModel, ndb


class Edge(Model):

	''' Represents a relationship between two graph nodes. '''

	source = ndb.KeyProperty()
	target = ndb.KeyProperty()
	partner = ndb.KeyProperty()


class EdgeItem(PolyModel):

	''' Represents an aspect of a relationship between two graph nodes. '''

	edge = ndb.KeyProperty()
	partner = ndb.KeyProperty()
