#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

import requests
from . import constants
from . import lang
from . import config


class AI(object):
	"""
	Python class wrapper for Gurunudi AI methods
	"""

	def autocorrect(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text that has to be autocorrected
		lang (string): ISO3 language code of the text
		returns: spell checked autocorrected text

		"""

		return self.__call_api(constants.API_AUTOCORRECT,{FIELD_TEXT:text})

	def autocomplete(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text that has to be autocompleted
		lang (string): ISO3 language code of the text
		returns: attempts to autocomplete text

		"""

		return self.__call_api(constants.API_AUTOCOMPLETE,{FIELD_TEXT:text})


	def chat(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text to be responded to
		lang (string): ISO3 language code of the text
		returns: chat response to the text - ideal for chatbots
		"""
 
		return self.__call_api(constants.API_CHAT,{FIELD_TEXT:text})

 
	def contextqa(self,context,text,lang=lang.ENGLISH):
		"""
		context (string): The context in which the text has to be answered
		text (string): The text that has to be answered in given context
		lang (string): ISO3 language code of context and text
		returns: response to text based on given context

		"""

		return self.__call_api(constants.API_KEYWORDS,{FIELD_TEXT:text})


	def coref(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text whose coreferences have to be resolved
		lang (string): ISO3 language code of the text
		returns: text after resolving coreferences
		
		"""

		return self.__call_api(constants.API_COREF,{FIELD_TEXT:text})

	def define(self,text,lang=lang.ENGLISH):
		"""
		text (string): The word or noun to be defined
		lang (string): ISO3 language code of the text
		returns: definition of given word or noun
		
		"""

		return self.__call_api(constants.API_DEFINE,{FIELD_TEXT:text})
 

	def dependency(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text whose dependency parse tree has to be created
		lang (string): ISO3 language code of the text
		returns: dependecy parsing tree of each sentence in the text
		
		"""

		return self.__call_api(constants.API_DEPENDENCY,{FIELD_TEXT:text})


	def fix_case(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text to be case fixed
		lang (string): ISO3 language code of the text
		returns: text after fixing any incorrect case issues in it
		"""

		return self.__call_api(constants.API_FIX_CASE,{FIELD_TEXT:text})

	def intent(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text whose intent has to be found
		lang (string): ISO3 language code of the text
		returns: intent of the text
		"""
 
		return self.__call_api(constants.API_INTENT,{FIELD_TEXT:text})
 

	def keywords(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text that has to be answered in given context
		lang (string): ISO3 language code of context and text
		returns: a list of keywords in the text			

		"""

		return self.__call_api(constants.API_KEYWORDS,{FIELD_TEXT:text})


	def knowledge(self,text,lang=lang.ENGLISH):
		"""
		text (string): The knowledge query whose answer has to be fetched
		lang (string): ISO3 language code of the text
		returns: answer from Gurunudi Knowledge Graph
		"""
 
		return self.__call_api(constants.API_KNOWLEDGE,{FIELD_TEXT:text})
 

	def language(self,text):
		"""
		text (string): The text whose language has to be found
		returns dict containing language name, ISO1 and ISO3 codes of the language
		"""
		return self.__call_api(constants.API_LANGUAGE,{FIELD_TEXT:text})

  
	def named_entities(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text to find named entities in
		lang (string): ISO3 language code of the text
		returns: a list of dictionaries where dict is of the form
		{"text":<entity_text>,"start":<entity_start_index>,"label":<entity_label>}
		"""

		return self.__call_api(constants.API_NAMED_ENTITIES,{FIELD_TEXT:text})


	def sentences(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text whose sentences have to be extracted
		lang (string): ISO3 language code of the text
		returns: sentences in the text
		"""
 
		return self.__call_api(constants.API_SENTENCE_EXTRACTION,{FIELD_TEXT:text})


	def sentiment(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text whose sentiment has to be found
		lang (string): ISO3 language code of the text
		returns: sentiment of the text
		"""
 
		return self.__call_api(constants.API_SENTIMENT_ANALYSIS,{FIELD_TEXT:text})


	def summary(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text to be summarized
		lang (string): ISO3 language code of the text
		returns: short summary of a large text like a news article or blog
		"""

		#call Gurunudi API to extract summary
		return self.__call_api(constants.API_SUMMARY,{FIELD_TEXT:text})
 
 
	def syntax(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text to be processed for syntax analysis
		lang (string): ISO3 language code of the text
		returns: parts of speech of each token in the given text

		
		"""

		return self.__call_api(constants.API_SYNTAX,{FIELD_TEXT:text})

	def title(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text whose title has to be generated
		lang (string): ISO3 language code of the text
		returns: an appropriate title for a large text like a news article or blog
		"""
 
		return self.__call_api(constants.API_TITLE,{FIELD_TEXT:text})


	def topics(self,text,lang=lang.ENGLISH):
		"""
		text (string): The text whose topics have to be guessed
		lang (string): ISO3 language code of the text
		returns: list of topics of the text
		"""

		return self.__call_api(constants.API_TOPICS,{FIELD_TEXT:text})
		

	def translate(self,text,src_lang,target_lang):
		"""
		text (string): The text that has to be translated
		src_lang (string): ISO3 language code of the text
		target_language: ISO3 language code of the target language to which text has to be translated 
		returns: translated text if translation was successful, else returns None
		
		"""

		return self.__call_api(constants.API_COREF,{FIELD_TEXT:text})

 
	def __call_api(self,api,data):
		"""
		calls given Gurunudi api with given data and returns the result
		api (string): The name of the API to call
		data (dict): Data to be sent to the API
		"""
 

		try:
			if config.DEBUG:
				print("Call API",api_name)
		 		print("Request Data",data)

			#call the API
			url = config.API_URL.format(api_name)
			response = requests.post(url, json=data, headers=config.HEADERS)
			json=response.json()

			if config.DEBUG:
				print("Response Code",response.status_code)
				print("Response data",json)

			#if api returned error
			if constants.FIELD_ERROR in json:
				raise APIError(json[constants.FIELD_ERROR])

			if response.status_code==200:#if response OK
				if len(json)==1:#if response has only one field, then it is a "text" field or a list field. Return it as is
					for value in json.values():
						return value
				else:#if response has multiple fields, then return the entire dict
					return json
			else:
				raise APIError("status_code_"+str(response.status_code))

		except requests.exceptions.ConnectionError as ex:
			raise APIError(constants.ERROR_SERVER_INACCESSIBLE)

 

		
class APIError(Exception):
	def __init__(self, message):
		super(APIError,self).__init__(message)

