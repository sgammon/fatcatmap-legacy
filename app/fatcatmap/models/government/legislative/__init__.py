from fatcatmap.models import Model, PolyModel, ndb


class Legislature(Model):

	''' Represents a body that makes governmental policy decisions. '''

	shortname = ndb.StringProperty()
	longname = ndb.StringProperty()
	names = ndb.StringProperty(repeated=True)
	boundary = ndb.KeyProperty()


class LegislativeChamber(PolyModel):

	''' Represents a house of members within a legislature. '''

	shortname = ndb.StringProperty()
	longname = ndb.StringProperty()
	legislature = ndb.KeyProperty()
	term_limit = ndb.IntegerProperty()
	term_length = ndb.IntegerProperty()
	seat_count = ndb.IntegerProperty()


class SuperiorChamber(LegislativeChamber):

	''' Represents an upper legislative chamber, such as a Senate or a House of Lords. '''

	pass


class InferiorChamber(LegislativeChamber):

	''' Represents a lower legislative chamber, such as a House of Representatives or Assembly. '''

	pass


class LegislativeSeat(Model):

	''' Represents a seat that can be held by a voting member in a legislative house. '''

	chamber = ndb.KeyProperty()
	district = ndb.KeyProperty()
	empty = ndb.BooleanProperty(default=True)
	terms = ndb.KeyProperty(repeated=True)
