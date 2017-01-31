from fatcatmap.models import Model


class Nation(Model):

	''' Represents a sovereign world nation. '''

	fullname = ndb.StringProperty(indexed=True)
	shortname = ndb.StringProperty(indexed=True)
	names = ndb.StringProperty(repeated=True, indexed=True)


class State(Model):

	''' Represents a state or province within a nation. '''

	fullname = ndb.StringProperty(indexed=True)
	shortname = ndb.StringProperty(indexed=True)
	names = ndb.StringProperty(repeated=True, indexed=True)
	nation = ndb.KeyProperty()


class City(Model):

	''' Represents a small locality within a state or province within a nation. '''

	fullname = ndb.StringProperty(indexed=True)
	shortname = ndb.StringProperty(indexed=True)
	names = ndb.StringProperty(repeated=True, indexed=True)
	latlong = ndb.GeoPtProperty(indexed=True)
	state = ndb.KeyProperty()


class PostalCode(Model):

	''' Represents an area for postal delivery. '''

	code = ndb.StringProperty()
	neighbors = ndb.KeyProperty(repeated=True)
	cities = ndb.KeyProperty()
