from fatcatmap.models import Model, PolyModel, ndb


class LegislativeDistrict(PolyModel):

	''' Represents a local area of authority for an elected legislative official. '''

	boundary = ndb.KeyProperty(repeated=True)
	postalcodes = ndb.KeyProperty(repeated=True)


class ExplicitDistrict(LegislativeDistrict):

	''' Represents a numbered, or otherwise catalogued, legislative district. '''

	code = ndb.StringProperty()


class ImplicitDistrict(LegislativeDistrict):

	''' Represents an implicit district, that exists de-facto. '''

	pass
