from fatcatmap.models import PolyModel


class Organization(PolyModel):

	''' Abstract model representing some kind of organization. '''

	pass


class Nonprofit(Organization):

	''' A 501(c)3 registered non-profit organization. '''

	pass


class Corporation(Organization):

	''' C-Corp/S-Corp/L3C/LLC registered organization. '''

	pass


class NGO(Organization):

	''' Non-Governmental-Organization (think NATO/UN). '''

	pass


class InterestGroup(Organization):

	''' Think Tea Party/Occupy groups. '''

	pass
