#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

#***************************** NATURAL LANGUAGE GENERATION - NLG ************************************/
#  
#  This example shows how to query Gurunudi to generate natural language text using given intent data.
#  
#***************************** NATURAL LANGUAGE GENERATION - NLG ************************************/

from gurunudi import AI,lang

#AI is the wrapper class to call Gurunudi AI API
ai = AI()

response = ai.generate({"theme":"Delhi","attribute":"location","value":"India"})
print(response)

#For the latest updated list of languages supported by Gurunudi for natural language generation visit https://guruyuga.com/languages/

