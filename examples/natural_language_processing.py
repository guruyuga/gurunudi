#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** NATURAL LANGUAGE PROCESSING - NLP ************************************/
#  
#  This example shows how to query Gurunudi to extract sentences, pos data, dependency information and named entities in a text
#  
#***************************** NATURAL LANGUAGE PROCESSING - NLP ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai = AI()

#nlp is a combination of the following api calls
#sentences, syntax, dependency, named_entities

response = ai.nlp("Larry Page was doing his Phd at Stanford University in 1996.")
print(response)
 
response = ai.nlp("Emmanuel Macron est le président de la France.",lang.FRENCH)
print(response)

#For the latest updated list of languages supported by Gurunudi for named entities recognition visit https://gurulaghu.com/languages/

