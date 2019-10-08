#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** LANGUAGE DETECTION ************************************/
#  
#  This example shows how to query Gurunudi to identify language of a text
#  
#***************************** LANGUAGE IDENTIFICATION ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai = AI()

response = ai.language("lorem ipsum")
print(response)
 
response = ai.language_name("lorem ipsum")
print(response)
 
response = ai.language("matter tells space how to curve and space tells matter how to move")
print(response)

response = ai.language("ನನ್ನ ಹೆಸರು ಗುರು")
print(response)

#For the latest updated list of languages supported by Gurunudi for language detection visit https://guruyuga.com/languages/




 
