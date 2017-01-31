from fatcatmap.models import PolyModel, ndb


class Descriptor(PolyModel):

	''' A piece of data that describes something about a node or edge. '''

	pass


class ValueDescriptor(Descriptor):

	''' A descriptor that holds a named value that can be placed on a node or edge. '''

	pass


class RangeDescriptor(Descriptor):

	''' A descriptor that holds a named, bounded value that can be placed on a node or edge. '''

	pass


class CheckpointDescriptor(Descriptor):

	''' A descriptor that holds a named, bounded value that occurs between ranges, that can be placed on a node or edge. '''

	pass
