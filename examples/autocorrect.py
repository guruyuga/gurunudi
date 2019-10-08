#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** AUTOCORRECTION *******************************************/
#  
#  This example shows how to query Gurunudi to spell check and automatically correct a text
#  
#***************************** SPELL CHECK *********************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API

ai=AI()

response = ai.autocorrect("whois cming")
print(response)

response = ai.autocorrect("whchi is the captal of idnia")
print(response)

#By default the text is assumed to be in English language. If the text is in a different language, you can pass the corresponding language code. See example below for French text.
response = ai.autocorrect("Les femes ont cessé de prndre des piluls parce qu'elles étaient encintes.",lang.FRENCH)
print(response)

#For the latest updated list of languages supported by Gurunudi for autocorrection visit https://guruyuga.com/languages/
