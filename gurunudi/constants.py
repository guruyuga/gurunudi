#!/usr/bin/env python

"""
List of APIs supported by Gurunudi
"""
API_AUTOCORRECT		='autocorrect'			#checks any spelling mistakes in a text document
API_AUTOCOMPLETE	='autocomplete'			#tries to autocomplete given text
API_LANGUAGE		='language'			#detects the language of a text document
API_SENTIMENT		='sentiment'			#analyzes the sentiment of a text document
API_COREF		='coref'			#resolves co-references in a text document
API_NAMED_ENTITIES	='named_entities'		#extracts named-entities in a text document
API_CHAT		='chat'				#real time conversation and knowledge q&a - ideal for chatbots
API_CLASSIFY		='classify'			#returns classification labels for given text using given model
API_DEFINE		='define'			#returns definition of word or noun or phrase
API_CONTEXTQA		='contextqa'			#answers based on given context
API_FIX_CASE		='fixcase'			#returns text after fixing any incorrect case issues
API_GRAPH_QUERY		='graph_query'			#queries gurunudi knowledge graph in a structured way
API_NLG			='nlg'				#generates natural language text from given intent
API_NLI			='inferences'			#generates inferences based on given text
API_NLP			='nlp'				#sentence extraction + pos + dep + ner
API_QUERY		='query'			#answers natural language query using gurunudi knowledge graph
API_KEYWORDS		='keywords'			#extracts keywords from a text document
API_SENTENCES		='sentences'			#extracts sentences in a text document
API_INTENT		='intent'			#extracts intent of a text document
API_SYNTAX		='syntax'			#analyzes syntax of a text document
API_DEPENDENCY		='dependency'			#creates syntactic dependency tree of a text document
API_TOPICS		='topics'			#returns a list of topics associated with the document
API_SUMMARY		='summary'			#returns short summary of a large text document
API_TRANSLATE		='translate'			#translates from source language to destination language
API_TITLE		='title'			#returns title for a large text

"""
Fields returned in response JSON by Gurunudi API calls and Fields sent in request JSON to Gurunudi API calls
"""
FIELD_LANG='lang'
FIELD_TARGET_LANG='target'
FIELD_CONTEXT='context'
FIELD_TEXT="text"
FIELD_ERROR="error"
FIELD_LIST="list"
FIELD_MODEL="model"

ERROR_SERVER_INACCESSIBLE="server_inaccessible"
ERROR_INVALID_LANGUAGE_CODE="invalid_language_code" 
ERROR_NO_RESPONSE="no_response_for_api"

