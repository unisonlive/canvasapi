class CanvasObject(object):
	"""
	Base class for all classes representing objects returned by the API.
	"""

	def __init__(self, requester, headers, attributes):
		"""
		:param requester: Requester
		:param headers: dict
		"""
		self._requester = requester
		self._headers = headers
		
		# Initialize object attributes
		for attribute, value in attributes.iteritems():
			self.__setattr__(attribute, value)