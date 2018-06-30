#!/usr/bin/env python

import requests
from . import constants
from . import lang
from . import config

class Gurunudi(object):
	"""Gurunudi API Client - calls Gurunudi AI API Service
	"""

	def __init__(self):
		"""Initialize with API Key to Empty

		"""
		self.__key=''


	@property
	def key(self):
		"""Getter for API Key

		Returns
		-------
		The Gurunudi API Key set


		"""
		return self.__key

	@key.setter
	def key(self, key):
		"""Setter for API Key

		Parameters
		-------

		key : string
			Your Gurunudi API Key

		"""
		self.__key=key


	def call_api(self,api_name,documents,additional_key,additional_value):
		"""
		calls given api for each document in the documents list and sets the api response to corresponding document object in the document list
		api_name (string): The name of the API to call
		documents (list): List of gurunudi.ai objects
		additional_key (string): any additional info, like target language code for translation and dictionary api calls
		additional_value (string or int): if additional key present, then its value
		"""

		if self.key=='':#no API Key set?
			raise APIError(constants.ERROR_MISSING_API_KEY)

		try:
			if config.DEBUG:
				print("Call API",api_name)

			#create the JSON post data for the API call
			data=[]
			for document in documents:
				document_data={constants.FIELD_TEXT:document.text}
				if api_name!=constants.API_DETECT_LANGUAGE: #add language code if present for calls other than detect_language
					lang_code=document.language_code_if_known
					if lang_code:
						document_data[constants.FIELD_LANGUAGE_CODE]=lang_code
					else: #if language code not set, then it defaults to english
						document_data[constants.FIELD_LANGUAGE_CODE]=lang.ENGLISH
				if additional_key:
					document_data[additional_key]=additional_value
				data.append(document_data)

			if config.DEBUG:
				print("Request Data",data)

			#call the API
			url = config.API_URL.format(api_name)
			response = requests.post(url, json={constants.FIELD_DOCUMENTS:data,constants.FIELD_API_KEY:self.key}, headers=config.HEADERS)
			json=response.json()


			if config.DEBUG:
				print("Response Code",response.status_code)
				print("Response data",json)

			#if api returned error
			if constants.FIELD_ERRORS in json:
				raise APIError(' '.join(json[constants.FIELD_ERRORS]))
			elif constants.FIELD_DOCUMENTS in json:
				if len(json[constants.FIELD_DOCUMENTS])==1:#if single document.. check if it has any error
					doc=json[constants.FIELD_DOCUMENTS][0]
					if api_name in doc:#some response for this api from server
						if constants.FIELD_ERRORS in doc[api_name]:
							raise APIError(' '.join(doc[api_name][constants.FIELD_ERRORS]))
					else:#if no response found for this api
						raise APIError(constants.ERROR_NO_RESPONSE)

			

			if response.status_code==200:#if response OK
				if constants.FIELD_DOCUMENTS in json:#set response to each document
					for doc_response,document in zip(json[constants.FIELD_DOCUMENTS],documents):
						for api_in_response,json_in_response in doc_response.items(): 
							document.set_response(api_in_response,json_in_response,additional_key)
			else:
				raise APIError("status_code_"+str(response.status_code))

		except requests.exceptions.ConnectionError as ex:
			raise APIError(constants.ERROR_SERVER_INACCESSIBLE)

		
class APIError(Exception):
	def __init__(self, message):
		super(APIError,self).__init__(message)
client=Gurunudi()
