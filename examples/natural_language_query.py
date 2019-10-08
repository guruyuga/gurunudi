#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** NATURAL LANGUAGE QUERY - NLQ ************************************/
#  
#  This example shows how to query Gurunudi Knowledge Graph
#  
#***************************** NATURAL LANGUAGE QUERY - NLQ ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API

ai = AI()

#default language is English
response=ai.query('capital of India')
print(response)

#if language other than English, then specify
response=ai.query("capitale de l'Inde",lang.FRENCH)
print(response)


#For the latest updated list of languages supported by Gurunudi for knowledge graph query visit https://guruyuga.com/languages/
