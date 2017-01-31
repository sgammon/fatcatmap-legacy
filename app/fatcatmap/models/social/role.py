from fatcatmap.models import Model, ndb


class Role(Model):

	''' Represents a social role that a person is playing or has played. '''

	person = ndb.KeyProperty()


class UnlimitedTerm(Role):

	''' Represents a role that has no limits (like a seat on the Supreme Court). '''

	start = ndb.DateProperty()


class LimitedTerm(Role):

	''' Represents a term that is limited by time (like a Senator's term). '''

	start = ndb.DateProperty()
	end = ndb.DateProperty()
	partial = ndb.BooleanProperty()


class ExecutiveTerm(LimitedTerm):

	''' Represents a term that sits in an executive capacity. '''

	agency = ndb.KeyProperty()
	appointed = ndb.BooleanProperty()
	elected = ndb.BooleanProperty()
	appointer = ndb.KeyProperty()
