#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** SENTENCE EXTRACTION ************************************/
#  
#  This example shows how to query Gurunudi to extract sentences in a text
#  
#***************************** SENTENCE EXTRACTION ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai=AI()

response = ai.sentences("India is a country in South Asia. It shares land borders with Pakistan to the west. China, Nepal, and Bhutan are to the northeast; and Myanmar (Burma) and Bangladesh to the east.")
print(response)

response = ai.sentences("L'India, ufficialmente Repubblica dell'India, è uno Stato federale dell'Asia meridionale, con capitale Nuova Delhi.",lang.ITALIAN)

#For the latest updated list of languages supported by Gurunudi for sentence extraction visit https://gurulaghu.com/languages/
