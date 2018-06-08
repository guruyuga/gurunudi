#!/usr/bin/env python

import requests
from .constants import *
from .config import *

class Gurunudi(object):
	"""Gurunudi API Client - calls Gurunudi AI API Service
	"""

	def __init__(self):
		"""Initialize with API Key to Empty

		"""
		self.__api_key=''


	@property
	def api_key(self):
		"""Getter for API Key

		Returns
		-------
		The Gurunudi API Key set


		"""
		return self.__api_key

	@api_key.setter
	def api_key(self, api_key):
		"""Setter for API Key

		Parameters
		-------

		api_key : string
			Your Gurunudi API Key

		"""
		self.__api_key=api_key


	def call_api(self,api_name,documents):
		"""
		calls given api for each document in the documents list and sets the api response to corresponding document object in the document list
		api_name (string): The name of the API to call
		documents (list): List of gurunudi.string objects
		"""

		try:
			if DEBUG:
				print("Call API",api_name)

			#create the JSON post data for the API call
			data=[]
			for document in documents:
				document_data={FIELD_TEXT:document.text}
				if api_name!=API_DETECT_LANGUAGE: #add language code if present for calls other than detect_language
					lang_code=document.language_code_if_known
					if lang_code:
						document_data[FIELD_LANGUAGE_CODE]=lang_code
				data.append(document_data)

			#call the API
			if DEBUG:
				print("Request Data",data)
			url = API_URL.format(api_name)		
			response = requests.post(url, json={FIELD_DOCUMENTS:data,FIELD_API_KEY:self.__api_key}, headers=HEADERS)

			#if api returned error
			if FIELD_ERRORS in response:
				raise APIError(' '.join(response[FIELD_ERRORS]))

			json=response.json()

			if DEBUG:
				print("Response Code",response.status_code)
				print("Response data",json)

			if response.status_code==200:#if response OK
				if FIELD_DOCUMENTS in json:#set response to each document
					for doc_response,document in zip(json[FIELD_DOCUMENTS],documents):
						for api_in_response,json_in_response in doc_response.items(): 
							document.set_response(api_in_response,json_in_response)
			else:
				raise APIError("status_code_"+str(response.status_code))

		except requests.exceptions.ConnectionError as ex:
			raise APIError(ERROR_SERVER_INACCESSIBLE)
		except Exception as ex: #exception means unable to reach the server, unless server has returned invalid json in response			
			raise APIError(str(ex))

		
class APIError(Exception):
	def __init__(self, message):
		super().__init__(message)

client=Gurunudi()
