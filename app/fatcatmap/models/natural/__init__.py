from fatcatmap.models import Model, ndb


class Person(Model):

	''' Represents a human being. '''

	firstname = ndb.StringProperty(indexed=True)
	lastname = ndb.StringProperty(indexed=True)
	names = ndb.StringProperty(repeated=True, indexed=True)
	birthdate = ndb.DateProperty(indexed=True)
	deathdate = ndb.DateProperty(indexed=True)
	nationality = ndb.StringProperty(indexed=False)
	religion = ndb.StringProperty(indexed=True)
