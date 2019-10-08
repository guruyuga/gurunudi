#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** NAMED ENTITIES RECOGNITION ************************************/
#  
#  This example shows how to query Gurunudi to extract named entities in a text
#  
#***************************** NAMED ENTITIES RECOGNITION ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai = AI()

response = ai.named_entities("Larry Page was doing his Phd at Stanford University in 1996.")
print(response)
 
response = ai.named_entities("Emmanuel Macron est le président de la France.",lang.FRENCH)
print(response)

#For the latest updated list of languages supported by Gurunudi for named entities recognition visit https://guruyuga.com/languages/

