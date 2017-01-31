from fatcatmap.models import Model, ndb
from fatcatmap.models.social import Role, LimitedTerm


class Legislator(Role):

	''' Represents a voting '''

	party = ndb.KeyProperty()
	in_office = ndb.KeyProperty()
	current_term = ndb.KeyProperty()
	terms = ndb.KeyProperty(repeated=True)


class LegislativeTerm(LimitedTerm):

	''' Represents a term that sits in an legislative capacity. '''

	phone = ndb.StringProperty()
	fax = ndb.StringProperty()
	website = ndb.StringProperty()
	webform = ndb.StringProperty()
	email = ndb.StringProperty()
	address = ndb.StringProperty()
	seat = ndb.KeyProperty()
	legislator = ndb.KeyProperty()
	senate_class = ndb.IntegerProperty(choices=[1, 2, 3])
