from fatcatmap.models import Model


class Node(Model):

	''' Represents an object in a certain context. '''

	label = ndb.StringProperty()
	native = ndb.KeyProperty()
	owner = ndb.KeyProperty()
	scope = ndb.StringProperty(repeated=True)
