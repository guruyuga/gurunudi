#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** CO-REFERENCE RESOLUTION ************************************/
#  
#  This example shows how to query Gurunudi to resolve coreferences in a text
#  
#***************************** COREFERENCE RESOLUTION ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai = AI()

response = ai.coref("The women stopped taking pills because they were pregnant.")
print(response)

#if language other than English, then specify
response = ai.coref("Les femmes ont cessé de prendre des pilules parce qu'elles étaient enceintes.",lang.FRENCH)
print(response)

#For the latest updated list of languages supported by Gurunudi for Coref Resolution visit https://guruyuga.com/languages/

