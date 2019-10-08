#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** DEFINITIONS ************************************/
#  
#  This example shows how to query Gurunudi to get definitions of a word or noun
#  
#***************************** DEFINITIONS ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai = AI()

response = ai.define("Emmanuel Macron")
print(response)

#if language other than English, then specify
response = ai.define("Emmanuel Macron",lang.FRENCH)
print(response)

#For the latest updated list of languages supported by Gurunudi for Definitions visit https://guruyuga.com/languages/

