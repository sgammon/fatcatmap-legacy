from fatcatmap.models import Model, ndb


class LegislativeCommittee(Model):

	''' Represents a committee with multiple members in a Legislature or LegislativeHouse. '''

	longname = ndb.StringProperty(required=True, indexed=True)
	shortname = ndb.StringProperty(required=True, indexed=True)
	names = ndb.StringProperty(repeated=True, indexed=True)
	chamber = ndb.KeyProperty(repeated=True, indexed=True)
	parent_committee = ndb.KeyProperty(default=None, indexed=True)
	subcommittees = ndb.KeyProperty(repeated=True, indexed=True)
	members = ndb.KeyProperty(repeated=True, indexed=True)
