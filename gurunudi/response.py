#!/usr/bin/env python

from .constants import *
from .language import Language

class Response(object):
	"""
	Abstracts the JSON Response data returned by the Gurunudi API Response
	For format of the JSON response see https://gurulaghu.com/api/
	"""

	def __init__(self,response):
		"""
		response (dict): dict of json response returned by the server
		"""
		self.__response = response
		
	@property
	def document(self,id):
		"""
		returns a document in the response by its id, returns None if no document with that ID found in the response
		"""
		if FIELD_DOCUMENTS not in self.__response:
			return None

		#return the document if present in the response
		for document in self.__response:
			if document.get(FIELD_ID)==id:
				return document
		
		return None
			

	@property
	def has_error(self):
		"""
		returns True if the response has one or more errors, else returns False
		"""

		return FIELD_ERRORS in self.__response
