#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

import requests
from . import constants
from . import lang
from . import config
import sys

class AI(object):
	"""
	Python class wrapper for Gurunudi AI methods - uses POST method, but GET is also supported by server for testing purposes or quick usage.
	"""


	def __init__(self,api_key=None,version=1):
		"""
		version (int): The API version to be used while querying Gurunudi Server
		api_key (string): The API key to access the Gurunudi platform

		"""
		self.version='v'+str(version)
		
		if api_key:
			config.HEADERS['gnapi']=api_key

	def chat(self,text,language=lang.ENGLISH):
		"""
		text (string): The text to be responded to
		language (string): ISO3 language code of the text
		returns: chat response to the text - ideal for chatbots
		"""
		if language==lang.ENGLISH:
			return self.__call_api(constants.API_CHAT,'{0}={1}'.format(constants.FIELD_TEXT,text))
		else: 			
			return self.__call_api(constants.API_CHAT,'{0}={1}&{2}={3}'.format(constants.FIELD_TEXT,text,constants.FIELD_LANG,language))


	def __call_api(self,api,data):
		"""
		calls given Gurunudi api with given data and returns the result
		api (string): The name of the API to call
		data (string): Data to be sent to the API
		"""


		try:
			if config.DEBUG:
				print("Call API",api)
				print("Request Data",data)

			#call the API
			url = config.API_URL.format(self.version,api)
			response = requests.get('{0}?{1}'.format(url,data), headers=config.HEADERS)
			json=response.json()

			if config.DEBUG:
				print("Request URI",url)
				print("Request data",data)
				print("Response Code",response.status_code)
				print("Response data",json)
				
			if response.status_code==200:#if response OK
				return json
			else:
				raise APIError("status_code_"+str(response.status_code))

		except requests.exceptions.ConnectionError as ex:
			print(ex,file=sys.stderr)
			raise APIError(constants.ERROR_SERVER_INACCESSIBLE)

class APIError(Exception):
	def __init__(self, message):
		super(APIError,self).__init__(message)

