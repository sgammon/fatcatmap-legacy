from fatcatmap import Model, ndb


class PoliticalParty(Model):

	''' Represents a major, organized political party. '''

	mascot = ndb.StringProperty()
	nickname = ndb.StringProperty()
	shortname = ndb.StringProperty()
	longname = ndb.StringProperty()
	singular = ndb.StringProperty()
	plural = ndb.StringProperty()
