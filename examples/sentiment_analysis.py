#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** SENTIMENT ANALYSIS ************************************/
#  
#  This example shows how to query Gurunudi to analyze the sentiment of a given piece of text
#  
#***************************** SENTIMENT ANALYSIS ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai=AI()

response = ai.sentiment("I really did not like that movie")
print(response)

response = ai.sentiment("she is very beautiful")
print(response)

response = ai.sentiment("The ambience was good, but the food was bad")
print(response)

response = ai.sentiment("roses are red, violets are blue")
print(response)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for German text.
response = ai.sentiment("Aller Anfang ist schwer",lang.GERMAN)
print(response)

#For the latest updated list of languages supported by Gurunudi for sentiment analysis visit https://gurulaghu.com/languages/
