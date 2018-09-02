#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** TOPIC MODELING *******************************************/
#  
#  This example shows how to query Gurunudi to suggest topics for a given text
#  
#***************************** TOPIC MODELING *********************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai=AI()

response = ai.topics("Oil prices fall on expected output rise")
print(response)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for Italian text.
response = ai.topics("L'India, ufficialmente Repubblica dell'India, è uno Stato federale dell'Asia meridionale, con capitale Nuova Delhi.",lang.ITALIAN)
print(response)

#For the latest updated list of languages supported by Gurunudi for topic modeling visit https://gurulaghu.com/languages/
