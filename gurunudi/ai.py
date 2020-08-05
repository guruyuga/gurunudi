#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

import requests
from . import constants
from . import lang
from . import config


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
			config.HEADERS['GNAPI']=api_key

	def autocorrect(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text that has to be autocorrected
		lang (string): ISO3 language code of the text
		returns: spell checked autocorrected text

		"""

		return self.__call_api(constants.API_AUTOCORRECT,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang})

	def autocomplete(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text that has to be autocompleted
		lang (string): ISO3 language code of the text
		returns: autocompleted text

		"""

		return self.__call_api(constants.API_AUTOCOMPLETE,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang})


	def chat(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text to be responded to
		lang (string): ISO3 language code of the text
		returns: chat response to the text - ideal for chatbots
		"""
 
		return self.__call_api(constants.API_CHAT,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang})

 
	def classify(self,text,model,lang=lang.ENGLISH):
		"""
		text (string): The text that has to be answered in given context
		model (string): The classification model to be used
		lang (string): ISO3 language code of context and text
		returns: response to text based on given context

		"""

		return self.__call_api(constants.API_CLASSIFY,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang,constants.FIELD_MODEL:model})


	def coref(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text whose coreferences have to be resolved
		lang (string): ISO3 language code of the text
		returns: text after resolving coreferences
		
		"""

		return self.__call_api(constants.API_COREF,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang})

	def define(self,text,lang=lang.ENGLISH):
		"""
		text (string): The word or noun to be defined
		lang (string): ISO3 language code of the text
		returns: definition of given word or noun
		
		"""

		return self.__call_api(constants.API_DEFINE,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang})
 

	def fix_case(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text to be case fixed
		lang (string): ISO3 language code of the text
		returns: text after fixing any incorrect case issues in it
		"""

		return self.__call_api(constants.API_FIX_CASE,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang})

	def intent(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text whose intent has to be found
		lang (string): ISO3 language code of the text
		returns: intent of the text
		"""
 
		return self.__call_api(constants.API_INTENT,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang})
 

	def keywords(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text to find keywords
		lang (string): ISO3 language code of the text
		returns: a list of keywords in the text			

		"""

		return self.__call_api(constants.API_KEYWORDS,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang})


	def language(self,text):
		"""
		text (string): The text whose language has to be found
		returns dict containing language name, ISO1 and ISO3 codes of the language
		"""
		return self.__call_api(constants.API_LANGUAGE,{constants.FIELD_TEXT:text})

  
	def lang_name(self,text):
		"""
		text (string): The text whose language has to be found
		returns language name
		"""
		lang_data = self.language(text)
		return lang_data.get("language","")

  
	def generate(self,intent,lang=lang.ENGLISH):
		"""
		intent (dict): The intent for which natural language text has to be generated
		lang (string): ISO3 language code of the language in which the text has to be generated
		returns: natural language text
		"""

		return self.__call_api(constants.API_NLG,{constants.FIELD_TEXT:intent,constants.FIELD_LANG:lang})

	def graph_query(self,data,lang=lang.ENGLISH):
		"""
		data (string): The structured info to query the Gurunudi Knowledge Graph
		lang (string): ISO3 language code of the query data
		returns: answer from Gurunudi Knowledge Graph
		"""
 
		return self.__call_api(constants.API_GRAPH_QUERY,{constants.FIELD_TEXT:data,constants.FIELD_LANG:lang})

	def inferences(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text to be infered
		lang (string): ISO3 language code of the language in which the text has to be infered
		returns: list of inferences
		"""

		return self.__call_api(constants.API_NLI,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang})

	def named_entities(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text to find named entities in
		lang (string): ISO3 language code of the text
		returns: a list of dictionaries where dict is of the form
		{"text":<entity_text>,"start":<entity_start_index>,"label":<entity_label>}
		"""

		return self.__call_api(constants.API_NAMED_ENTITIES,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang})

	def query(self,text,lang=lang.ENGLISH):
		"""
		text (string): The natural language query whose answer has to be fetched
		lang (string): ISO3 language code of the text
		returns: answer from Gurunudi Knowledge Graph
		"""
 
		return self.__call_api(constants.API_QUERY,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang})

	def sentiment(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text whose sentiment has to be found
		lang (string): ISO3 language code of the text
		returns: sentiment of the text
		"""
 
		return self.__call_api(constants.API_SENTIMENT,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang})


	def summary(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text to be summarized
		lang (string): ISO3 language code of the text
		returns: short summary of a large text like a news article or blog
		"""

		#call Gurunudi API to extract summary
		return self.__call_api(constants.API_SUMMARY,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang})
 
 
	def title(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text whose title has to be generated
		lang (string): ISO3 language code of the text
		returns: an appropriate title for a large text like a news article or blog
		"""
 
		return self.__call_api(constants.API_TITLE,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang})


	def topics(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text whose topics have to be guessed
		lang (string): ISO3 language code of the text
		returns: list of topics of the text
		"""

		return self.__call_api(constants.API_TOPICS,{constants.FIELD_TEXT:text,constants.FIELD_LANG:lang})


	def translate(self,text,target_lang,src_lang):
		"""
		text (string): The text that has to be translated
		target_language (string): ISO3 language code of the target language to which text has to be translated 
		src_lang (string): ISO3 language code of the text
		returns: translated text if translation was successful, else returns empty text
		
		"""

		return self.__call_api(constants.API_TRANSLATE,{constants.FIELD_TEXT:text,constants.FIELD_LANG:src_lang,constants.FIELD_TARGET_LANG:target_lang})

 
	def __call_api(self,api,data):
		"""
		calls given Gurunudi api with given data and returns the result
		api (string): The name of the API to call
		data (dict): Data to be sent to the API
		"""
 

		try:
			if config.DEBUG:
				print("Call API",api)
				print("Request Data",data)

			#call the API
			url = config.API_URL.format(self.version,api)
			response = requests.post(url, json=data, headers=config.HEADERS)
			json=response.json()

			if config.DEBUG:
				print("Response Code",response.status_code)
				print("Response data",json)
				
			#if api returned error
			if constants.FIELD_ERROR in json:
				raise APIError(json[constants.FIELD_ERROR])

			if response.status_code==200:#if response OK
				#if raw json response is requested	
				if raw_response=True:	
					return json

				if constants.FIELD_TEXT in json:#if response is plain text
					return json[constants.FIELD_TEXT]
				if constants.FIELD_LIST in json:#if response is a list
					return json[constants.FIELD_LIST]
					
				#neither text response nor list response, indicating this is a dict response. So return it as is
				return json
			else:
				raise APIError("status_code_"+str(response.status_code))

		except requests.exceptions.ConnectionError as ex:
			raise APIError(constants.ERROR_SERVER_INACCESSIBLE)

 

		
class APIError(Exception):
	def __init__(self, message):
		super(APIError,self).__init__(message)


