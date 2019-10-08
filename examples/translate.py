#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** TRANSLATION *******************************************/
#  
#  This example shows how to query Gurunudi to translate a given text from one language to another
#  
#***************************** TRANSLATION *********************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai=AI()

#translation requires target language and source language to be specified
response = ai.translate("India is the only country to have an ocean named after it.",lang.SPANISH,lang.ENGLISH)
print(response)

response = ai.translate("Emmanuel Macron est le président de la France.",lang.ENGLISH,lang.FRENCH)
print(response)

#For the latest updated list of languages supported by Gurunudi for translation visit https://guruyuga.com/languages/
