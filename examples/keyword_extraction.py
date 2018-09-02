#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** KEYWORDS EXTRACTION ************************************/
#  
#  This example shows how to query Gurunudi to extract keywords from a text
#  
#***************************** KEYWORDS EXTRACTION ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai = AI()

response = ai.keywords("India is a country in South Asia. It shares land borders with Pakistan to the west; China, Nepal, and Bhutan to the northeast; and Myanmar (Burma) and Bangladesh to the east.")
print(response)

#if language other than English, then specify
response = ai.keywords("L'India, ufficialmente Repubblica dell'India, è uno Stato federale dell'Asia meridionale, con capitale Nuova Delhi.",lang.ITALIAN)
print(response)

#For the latest updated list of languages supported by Gurunudi for keyword extraction visit https://gurulaghu.com/languages/

