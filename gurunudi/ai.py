#!/usr/bin/env python

from .gurunudi import client,APIError
from . import constants

class AI(object):
	"""
	Python class wrapper for Gurunudi AI methods
	"""

	def __init__(self,text,language_code=None):
		"""
		text (string): document text 
		language_code (string): ISO 639-3 or ISO 639-2 language code of the document text if already known, else language detection call will be used to guess the language
		"""
		self.__id=None
		self.__text=text

		self.__latest_error=None

		#if language code contains hyphen then the text after hyphen is considered to be its locale, ex: en-US or eng-US or zh-TW
		if language_code and '-' in language_code:
			arr=language_code.split[1]
			self.__language_code=arr[0]
			self.__locale=arr[1]
		else:
			self.__language_code=language_code
			self.__locale=None

		if self.__language_code and self.__language_code not in languages:
			raise APIError(ERROR_INVALID_LANGUAGE_CODE+" "+self.__language_code)

		#stores the responses to different Gurunudi AI API queries by this text document
		self.__responses={}
	
		#setting this to True disables api call cache.
		self.__disable_cache=False

	@property
	def disable_cache(self):
		"""
		returns: True if api call cache has been disabled, else False
		"""
		return self.__disable_cache


	@disable_cache.setter
	def disable_cache(self, disable):
		"""
		disable (boolean): disables api call cache if True, else enables it
		"""
		self.__disable_cache=disable_cache


	def clear_cache(self):
		"""
			clears api call cache. useful to call in case of large memory usage
		"""
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
		self.__call_api(constants.API_DETECT_LANGUAGE)

		api_response=self.__responses.get(constants.API_DETECT_LANGUAGE)
		if api_response:
			languages=api_response.get(constants.FIELD_LANGUAGES)
			if languages and len(languages)>0:#return most probable language's code
				return languages[0].get(constants.FIELD_ISO3)

		return None

	@property
	def sentences(self):
		"""
		returns: sentences in the text document
		"""

		#call Gurunudi API if not called already to extract sentences
		self.__call_api(constants.API_SENTENCE_EXTRACTION)

		api_response=self.__responses.get(constants.API_SENTENCE_EXTRACTION)
		if api_response:	
			return api_response.get(constants.FIELD_SENTENCES)

		return None

	@property
	def sentiment(self):
		"""
		returns: sentiment of the text document
		"""

		#call Gurunudi API if not called already to analyze sentiment
		self.__call_api(constants.API_SENTIMENT_ANALYSIS)

		api_response=self.__responses.get(constants.API_SENTIMENT_ANALYSIS)
		if api_response:	
			return api_response.get(constants.FIELD_SENTIMENT)

		return None

	@property
	def chat(self):
		"""
		returns: chat response to the text document - ideal for chatbots
		"""

		#call Gurunudi API
		self.__call_api(constants.API_CHAT)

		api_response=self.__responses.get(constants.API_CHAT)
		if api_response:	
			return api_response.get(constants.FIELD_TEXT)

		return None

	@property
	def intents(self):
		"""
		returns: intents of the text document
		"""

		#call Gurunudi API if not called already to extract intent
		self.__call_api(constants.API_INTENT)

		api_response=self.__responses.get(constants.API_INTENT)
		if api_response:	
			return api_response.get(constants.FIELD_INTENTS)

		return None

	@property
	def title(self):
		"""
		returns: an appropriate title for a large text document like a news article or blog
		"""

		#call Gurunudi API if not called already to extract title
		self.__call_api(constants.API_TITLE)

		api_response=self.__responses.get(constants.API_TITLE)
		if api_response:	
			return api_response.get(constants.FIELD_TEXT)

		return None

	@property
	def fix_case(self):
		"""
		returns: text after fixing any incorrect case issues in it
		"""

		#call Gurunudi API if not called already to fix case
		self.__call_api(constants.API_FIX_CASE)

		api_response=self.__responses.get(constants.API_FIX_CASE)
		if api_response:	
			return api_response.get(constants.FIELD_TEXT)

		return None


	@property
	def summary(self):
		"""
		returns: short summary of a large text document like a news article or blog
		"""

		#call Gurunudi API if not called already to extract summary
		self.__call_api(constants.API_SUMMARY)

		api_response=self.__responses.get(constants.API_SUMMARY)
		if api_response:	
			return api_response.get(constants.FIELD_TEXT)

		return None

	@property
	def coreferences(self):
		"""
		returns: a list of dictionaries where dict is of the form
		{"text":<text_in_document>,"start":<co-reference_start_index>,"mainref":<main_reference_text>}
		
		"""

		#call Gurunudi API if not called already to analyze sentiment
		self.__call_api(constants.API_COREF_RESOLUTION)

		api_response=self.__responses.get(constants.API_COREF_RESOLUTION)
		if api_response:	
			return api_response.get(constants.FIELD_COREFS)

		return None
 
	@property
	def definition(self):
		"""
		returns: most popular definition of given word or noun
		
		"""

		definitions = self.definitions

		if definitions and len(definitions)>0:
			return definitions[0].get(constants.FIELD_TEXT)

		return None

	@property
	def definitions(self):
		"""
		returns: all definitions of given word or noun
		
		"""

		self.__call_api(constants.API_DEFINE)

		api_response=self.__responses.get(constants.API_DEFINE)
		if api_response:	
			return api_response.get(constants.FIELD_DEFINITIONS)

		return None

	@property
	def summary(self):
		"""
		returns: short summary of a given large text
		
		"""

		self.__call_api(constants.API_SUMMARY)

		api_response=self.__responses.get(constants.API_SUMMARY)
		if api_response:	
			return api_response.get(constants.FIELD_TEXT)

		return None

	@property
	def syntax(self):
		"""
		returns: parts of speech of each token in the given text
		
		"""

		self.__call_api(constants.API_SYNTAX_ANALYSIS)

		api_response=self.__responses.get(constants.API_SYNTAX_ANALYSIS)
		if api_response:	
			return api_response.get(constants.FIELD_SYNTAX)

		return None

	@property
	def syntax_tree(self):
		"""
		returns: dependecy parsing tree of each sentence in the text
		
		"""

		self.__call_api(constants.API_SYNTACTIC_DEPENDENCY)

		api_response=self.__responses.get(constants.API_SYNTACTIC_DEPENDENCY)
		if api_response:	
			return api_response.get(constants.FIELD_SENTENCES)

		return None



	def translate(self,target_language_code):
		"""
		target_language_code: destination language code to translate given text.. see language_codes.py for supported language codes
		returns: translated text if translation was successful, else returns None
		
		"""

		self.__call_api(constants.API_TRANSLATE,constants.FIELD_TARGET_LANGUAGE_CODE,target_language_code)

		api_response=self.__responses.get(constants.API_TRANSLATE)
		if api_response:
			api_response_for_target_language_code=api_response.get(target_language_code)
			if api_response_for_target_language_code:
				return api_response_for_target_language_code.get(constants.FIELD_TEXT)

		return None


	def replace(self,replacements,target_field):
		"""
		replacements: list of dictionaries of the form [{"start":<start_index_of_text_to_replace>,"text":"<text_being_replaced>","<target_field>":"<replacement_text>"},...]
		target_field: name of the field in each replacements dictionary that contains the replacement text
		returns: text after replacing given replacements with text in target_field
		
		"""

		text=self.text
		inx=0		
		lst=[]
		for replacement in replacements:#for each piece of text to be replaced

			#get start index of replacement text
			pos=replacement[constants.FIELD_START]			

			#add any pending text before text being replaced
			if pos>0: 
				lst.append(text[inx:pos])	

			#add replacement text		
			lst.append(replacement[target_field]) 

			#move index to next char after replaced text
			inx=replacement[constants.FIELD_START]+len(replacement[constants.FIELD_TEXT]) 
		#add any pending last bit
		if inx<len(text):
			lst.append(text[inx:])
		return ''.join(lst)

	@property
	def coreferenced_text(self):
		"""
		returns: text after resolving coreferences
		
		"""

		#call Gurunudi API if not called already to resolve coreferences
		corefs=self.coreferences
		
		#return coreferenced text by replacing coreferences with corresponding nouns
		if corefs:
			return self.replace(corefs,constants.FIELD_MAIN_REF)

		return None

	@property
	def topics(self):
		"""
		returns: sentiment of the text document
		"""

		#call Gurunudi API if not called already to list topics
		self.__call_api(constants.API_TOPIC_MODELING)

		api_response=self.__responses.get(constants.API_TOPIC_MODELING)
		if api_response:	
			return api_response.get(constants.FIELD_TOPICS)

		return None


	@property
	def named_entities(self):
		"""
		returns: a list of dictionaries where dict is of the form
		{"text":<entity_text>,"start":<entity_start_index>,"label":<entity_label>}
		"""

		#call Gurunudi API if not called already to extract named entities
		self.__call_api(constants.API_NAMED_ENTITIES)

		api_response=self.__responses.get(constants.API_NAMED_ENTITIES)
		if api_response:	
			return api_response.get(constants.FIELD_ENTITIES)

		return None

	@property
	def spell_check(self):
		"""
		returns: a list of dictionaries where dict is of the form
		{"text":<text_in_document>,"start":<error_start_index>,"suggestion":<suggested_replacement_for_text>}
		
		"""

		#call Gurunudi API if not called already to check spellings
		self.__call_api(constants.API_SPELL_CHECK)

		api_response=self.__responses.get(constants.API_SPELL_CHECK)
		if api_response:	
			return api_response.get(constants.FIELD_SUGGESTIONS)

		return None	

	@property
	def spell_checked_text(self):
		"""
		returns: text after fixing any spelling errors
		
		"""

		#call Gurunudi API if not called already to check spellings
		spell_checks=self.spell_check
		
		#return spell checked text by replacing spelling mistakes with suggestions
		if spell_checks:
			return self.replace(spell_checks,constants.FIELD_SUGGESTION)

		return None		

	@property
	def keywords(self):
		"""
		returns: a list of keywords in the document			

		"""

		#call Gurunudi API if not called already to extract keywords
		self.__call_api(constants.API_KEYWORD_EXTRACTION)

		api_response=self.__responses.get(constants.API_KEYWORD_EXTRACTION)
		if api_response:	
			key_count = api_response.get(constants.FIELD_KEYWORDS)
			if key_count:				
				return list(key_count.keys())

		return None

	@property
	def latest_error(self):			
		return self.__latest_error

	@property
	def keywords_with_count(self):
		"""
		returns: a dictionary {<keyword>:<keyword_count>} where keyword_count is the number of times the keyword has appeared in the document			

		"""

		#call Gurunudi API if not called already to extract keywords
		self.__call_api(constants.API_KEYWORD_EXTRACTION)

		api_response=self.__responses.get(constants.API_KEYWORD_EXTRACTION)
		if api_response:	
			return api_response.get(constants.FIELD_KEYWORDS)

		return None			

	@property
	def language_code_if_known(self):
		"""
		returns: will return the language code of this document, only if it is manually set or already guessed. Will not call api unlike the property language_code
		"""
		if self.__language_code:#language has been set explicitly
			return self.__language_code

		if constants.API_DETECT_LANGUAGE in self.__responses:#if language has been guessed
			languages=self.__responses.get(constants.FIELD_LANGUAGES)
			if languages:#return most probable language's code
				return languages[0][constants.FIELD_ISO3]

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

	def __call_api(self,api,addtional_key=None,additional_value=None):
		"""
		calls given api if not already called for this document
		"""
		if api==constants.API_CHAT or api not in self.__responses:#call API if not called already or if this is a chat
			client.call_api(api,[self],addtional_key,additional_value)
		else: #if API already called
			if addtional_key is not None:#if we have additional info for this API
				if addtional_key not in self.__responses[api]:#if API not called for additional info ex: target language code
					client.call_api(api,[self],addtional_key,additional_value)

	def set_response(self,api,response,additional_key):
		"""
		sets the given response JSON dict to given api name
		"""
		if constants.FIELD_ERRORS in response:
			self.__latest_error = ' '.join(response[constants.FIELD_ERRORS])
		else:
			self.__latest_error=None #if successful call, reset latest error to None

			if additional_key:#if api uses additional info, like translation api that needs a target language.. then cache the response at additional info level under the api name..
				key_specific_responses=self.__responses.setdefault(api,{})
				key_specific_responses[additional_key]=response
			else:
				self.__responses[api]=response


