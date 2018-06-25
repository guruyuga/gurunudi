#!/usr/bin/env python

"""
List of APIs supported by Gurunudi
"""
API_DETECT_LANGUAGE	='detect_language'		#detects the language of a text document
API_SENTIMENT_ANALYSIS	='sentiment_analysis'		#analyzes the sentiment of a text document
API_KEYWORD_EXTRACTION	='keyword_extraction'		#extracts keywords from a text document
API_SENTENCE_EXTRACTION	='sentence_extraction'		#extracts sentences in a text document
API_COREF_RESOLUTION	='coreference_resolution'	#resolves co-references in a text document
API_NAMED_ENTITIES	='named_entities'		#extracts named-entities in a text document
API_INTENT		='intent_extraction'		#extracts intent of a text document
API_SYNTAX_ANALYSIS	='syntax_analysis'		#analyzes syntax of a text document
API_SYNTACTIC_DEPENDENCY='syntactic_dependency'		#creates syntactic dependency tree of a text document
API_TOPIC_MODELING	='topic_modeling'		#returns a list of topics associated with the document
API_SPELL_CHECK		='spell_check'			#checks any spelling mistakes in a text document
API_CHAT		='chat'				#real time conversation and knowledge q&a - ideal for chatbots
API_SUMMARY		='summary'			#returns short summary of a large text document
API_DEFINE		='define'			#returns definition of word or noun or phrase
API_TRANSLATE		='translate'			#translates from source language to destination language
API_TITLE		='title'			#returns title for a large text
API_FIX_CASE		='fix_case'			#returns text after fixing any incorrect case issues

"""
Fields returned in response JSON by Gurunudi API calls and Fields sent in request JSON to Gurunudi API calls
"""
FIELD_LANGUAGES='languages'
FIELD_LANGUAGE_CODE='language_code'
FIELD_TARGET_LANGUAGE_CODE='target_language_code'
FIELD_ISO1='iso639_1'
FIELD_ISO3='iso639_3'
FIELD_SENTIMENT='sentiment'
FIELD_SYNTAX='syntax'
FIELD_ERRORS='errors'
FIELD_ENTITIES='entities'
FIELD_DEPENDENCIES='dependencies'
FIELD_TEXT="text"
FIELD_DOCUMENTS="documents"
FIELD_API_KEY="key"
FIELD_SENTENCES="sentences"
FIELD_KEYWORDS="keywords"
FIELD_TOPCS="topics"
FIELD_NAME="name"
FIELD_LABEL="label"
FIELD_SUGGESTION='suggestion'
FIELD_SUGGESTIONS='suggestions'
FIELD_POS='pos'
FIELD_LEMMA='lemma'
FIELD_DEP='dependency'
FIELD_MAIN_REF='mainref'
FIELD_START='start'
FIELD_ENTRIES='entries'
FIELD_COREFS='corefs'


ERROR_SERVER_INACCESSIBLE="server_inaccessible"
ERROR_INVALID_LANGUAGE_CODE="invalid_language_code"

