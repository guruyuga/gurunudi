#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** AUTOCOMPLETE *******************************************/
#  
#  This example shows how to query Gurunudi to autocomplete a given text
#  
#***************************** AUTOCOMPLETE *********************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai=AI()

response = ai.autocomplete("which is the fastest")
print(response)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for French text.
response = ai.autocomplete("Emmanuel Macron est le président de la.",lang.FRENCH)
print(response)

#For the latest updated list of languages supported by Gurunudi for autocomplete visit https://guruyuga.com/languages/
