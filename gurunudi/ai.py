#!/usr/bin/env python

from .gurunudi import client,APIError
from .constants import *
from .language_codes import *

class ai(object):
	"""
	Python class wrapper for Gurunudi AI methods
	"""

#	def __new__(cls, value, *args, **kwargs):
#		# explicitly only pass value to the str constructor
#		return super(string, cls).__new__(cls, value)

	def __init__(self,text,language_code="eng",locale=None):
		"""
		text (string): document text 
		language_code (string): ISO 639-3 or ISO 639-2 language code of the document text, defaults to english (not applicable for language detection calls)
		"""
		self.__id=None
		self.__text=text
		self.__language_code=language_code

		#if language code contains hyphen then the text after hyphen is considered to be its locale, ex: en-US or eng-US or zh-TW
		self.__locale=language_code.split[1] if '-' in language_code and language_code[-1]!='-' else None

		#stores the responses to different Gurunudi AI API queries by this text document
		self.__responses={}
	
	@property
	def text(self):
		"""
			returns: the text of this document
		"""
		return self.__text

	@property
	def id(self):
		"""
			returns: if set, returns the ID of this text document, else None
		"""
		return self.__id

	@id.setter
	def id(self, id):
		"""
		id (string): set an ID for this string
		"""
		self.__id=id

	@property
	def responses(self):
		return self.__responses


	@property
	def language(self):
		"""
		returns the language name for this string. If unknown, returns None
		"""
		return languages.get(self.language_code)

	@property
	def language_code(self):
		"""
		returns: the 3 letter language code of this document. If language code is set manually returns it as is, else tries to guess the language by calling Gurunudi Language Detection API, if api call fails to detect language then returns None
		"""
		if self.__language_code:#language has been set explicitly
			return self.__language_code

		#call Gurunudi API if not called already to guess language
		self.__call_api(API_DETECT_LANGUAGE)

		api_response=self.__responses.get(API_DETECT_LANGUAGE)
		if api_response:
			languages=api_response.get(FIELD_LANGUAGES)
			if languages and len(languages)>0:#return most probable language's code
				return languages[0].get(FIELD_ISO3)

		return None

	@property
	def sentences(self):
		"""
		returns: sentences in the text document
		"""

		#call Gurunudi API if not called already to extract sentences
		self.__call_api(API_SENTENCE_EXTRACTION)

		api_response=self.__responses.get(API_SENTENCE_EXTRACTION)
		if api_response:	
			return api_response.get(FIELD_SENTENCES)

		return None

	@property
	def sentiment(self):
		"""
		returns: sentiment of the text document
		"""

		#call Gurunudi API if not called already to analyze sentiment
		self.__call_api(API_SENTIMENT_ANALYSIS)

		api_response=self.__responses.get(API_SENTIMENT_ANALYSIS)
		if api_response:	
			return api_response.get(FIELD_SENTIMENT)

		return None

	@property
	def sentiment(self):
		"""
		returns: returns response to the text document - ideal for chatbots
		"""

		#call Gurunudi API if not called already to analyze sentiment
		self.__call_api(API_CHAT)

		api_response=self.__responses.get(API_CHAT)
		if api_response:	
			return api_response.get(FIELD_RESPONSE)

		return None

	@property
	def topics(self):
		"""
		returns: sentiment of the text document
		"""

		#call Gurunudi API if not called already to list topics
		self.__call_api(API_TOPIC_MODELING)

		api_response=self.__responses.get(API_TOPIC_MODELING)
		if api_response:	
			return api_response.get(FIELD_TOPICS)

		return None


	@property
	def named_entities(self):
		"""
		returns: a list of dictionaries where dict is of the form
		{"name":<entity_name>,"label":<entity_label>,"start":<entity_start_index_in_document>,"LABEL":<entity_end_index_plus_1_in_document>}
		"""

		#call Gurunudi API if not called already to extract named entities
		self.__call_api(API_NAMED_ENTITIES)

		api_response=self.__responses.get(API_NAMED_ENTITIES)
		if api_response:	
			return api_response.get(FIELD_ENTITIES)

		return None

	@property
	def spell_check(self):
		"""
		returns: a list of dictionaries where dict is of the form
		{"offset":<start_index>,"text":<text_in_document>,"suggestion":<suggested_replacement_for_text>}
		
		"""

		#call Gurunudi API if not called already to check spellings
		self.__call_api(API_SPELL_CHECK)

		api_response=self.__responses.get(API_SPELL_CHECK)
		if api_response:	
			return api_response.get(FIELD_SUGGESTIONS)

		return None			

	@property
	def keywords(self):
		"""
		returns: a dictionary {<keyword>:<keyword_count>} where keyword_count is the number of times the keyword has appeared in the document			

		"""

		#call Gurunudi API if not called already to extract keywords
		self.__call_api(API_KEYWORD_EXTRACTION)

		api_response=self.__responses.get(API_KEYWORD_EXTRACTION)
		if api_response:	
			return api_response.get(FIELD_KEYWORDS)

		return None			

	@property
	def language_code_if_known(self):
		"""
		returns: will return the language code of this document, only if it is manually set or already guessed. Will not call api unlike the property language_code
		"""
		if self.__language_code:#language has been set explicitly
			return self.__language_code

		if API_DETECT_LANGUAGE in self.__responses:#if language has been guessed
			languages=self.__responses.get(FIELD_LANGUAGES)
			if languages:#return most probable language's code
				return languages[0][FIELD_ISO3]

		return None

	@language_code.setter
	def language_code(self, language_code):
		"""
		language_code (string): set language code for this string
		"""
		self.__language_code=language_code


	def clear(self):
		"""
		clears all api calls made for this document so far 
		"""
		self.__responses={}

	def __call_api(self,api):
		"""
		calls given api if not already called for this document
		"""
		if api not in self.__responses:#call API if not called already
			client.call_api(api,[self])

	def set_response(self,api,response):
		"""
		sets the given response JSON dict to given api name
		"""
		if FIELD_ERRORS in response:
			raise APIError(' '.join(response[FIELD_ERRORS]))
		else:
			self.__responses[api]=response


