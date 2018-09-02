#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** DEPENDENCY ANALYSIS *******************************************/
#  
#  This example shows how to query Gurunudi to analyze the dependency of a given text
#  
#***************************** DEPENDENCY ANALYSIS *********************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai=AI()

response = ai.dependency("Larry Page was doing his Phd at Stanford University in 1996")
print(response)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for French text.
response = ai.dependency("Emmanuel Macron est le président de la France.",lang.FRENCH)
print(response)

#For the latest updated list of languages supported by Gurunudi for dependency analysis visit https://gurulaghu.com/languages/
