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


class City(Model):

	''' Represents a small locality within a state or province within a nation. '''

	fullname = ndb.StringProperty(indexed=True)
	shortname = ndb.StringProperty(indexed=True)
	names = ndb.StringProperty(repeated=True, indexed=True)
	latlong = ndb.GeoPtProperty(indexed=True)
