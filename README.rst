Gurunudi AI API: Python client
******************************

**Gurunudi** is a Python library by `GuruLaghu Technologies <https://gurulaghu.com/>`_ for accessing the `Gurunudi Artificial Intelligence API <https://www.gurunudi.com/>`_.
Gurunudi (**AI as a Service**) provides a wide range of **Artificial Intelligence based API solutions** (See below). This client library for Gurunudi AI API is commercial open-source software, released under the MIT license.

💫 **Version 1.3.7 out now!**

.. image:: https://img.shields.io/pypi/v/gurunudi.svg?style=flat-square
    :target: https://pypi.python.org/pypi/gurunudi
    :alt: pypi Version

.. image:: https://badges.gitter.im/gurulaghu/gurunudi.svg
    :target: https://gitter.im/gurulaghu/gurunudi
    :alt: Gurunudi on Gitter 

.. image:: https://img.shields.io/twitter/follow/gurunudi.svg?style=social&label=Follow
    :target: https://twitter.com/gurunudi
    :alt: gurunudi on Twitter

📖 Installation
================

==================== ===
**Operating system** macOS / OS X, Linux, Windows
**Python version**   2+
**Package managers** `pip <https://pypi.python.org/pypi/gurunudi>`_
==================== ===

via pip
-------

.. code:: bash

    pip install gurunudi

When using pip it is generally recommended to install packages in a virtual environment to avoid modifying system state:

.. code:: bash

    venv .env
    source .env/bin/activate
    pip install gurunudi

Updating
--------

.. code:: bash

    pip install gurunudi --upgrade

💬 Where to ask questions
==========================

The Gurunudi project is maintained by `@gurudevrao <https://github.com/gurudevrao>`_. Please use the below listed forums for any support requests.

====================== ===
**Bug Reports**        `GitHub Issue Tracker`_
**Usage Questions**    `StackOverflow`_, `Gitter Chat`_
**General Discussion** `Gitter Chat`_
====================== ===

.. _GitHub Issue Tracker: https://github.com/gurulaghu/gurunudi/issues
.. _StackOverflow: http://stackoverflow.com/questions/tagged/gurunudi
.. _Gitter Chat: https://gitter.im/gurulaghu/gurunudi

Features of Gurunudi
====================

* Not just English, support exists for an ever growing list of **100+** `languages <https://gurulaghu.com/languages/>`
* Pre-trained models that are continuously updated for better accuracy and to support more languages.
* Text Classification - Language Detection, Sentiment Analysis, Topic Modeling, Text Classification and more 
* Text Analysis - NLP tasks like Named Entities, Keyword Extraction, Intent Extraction
* Text Generation - Chatbot, Summarization, Title Generation, Translation, Natural Language Generation (NLG) and more
* Text Transformation - Co-reference Resolution, Fix Case (True Case), Spell Check and more
* Knowledge Graph - Definition, Natural Language Query (NLQ), Natural Language Inference (NLI)
* Custom Trained Bots - Domain Experts, Customer Support, FAQ and more
* More cutting edge AI features are being added continuously


📖 Documentation
================

Basics
------

.. code:: python

    from gurunudi import AI,lang

    ai=AI()

AI is a class that abstracts API calls to Gurunudi AI System. Create an AI object as shown above. Except for language detection API call, all other text based API calls take an additional optional argument as the language code which if not present, defaults to English (except for language detection call). The language code is a 3-letter `ISO 639-3 code <https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes>`_. For language codes and features currently supported by each language, see `supported languages <https://gurulaghu.com/languages/>`_.

.. code:: python

    from gurunudi import lang
    definition=ai.define("ಕನ್ನಡ",lang.KANNADA) #Specify the language if non-English text

Autocorrect / Spell Check
-------------------------

Attempts to automatically fix any spelling errors which includes misspelled words, mixed up words.

.. code:: python

    corrected_text = ai.autocorrect("who is the primem inister of idnia")
    #now corrected_text = "who is the prime minister of india"

    #English is the default language for all API calls (except langauge detection API that has no language parameter as input). 
    #So, if your input text is in a language other than english, you can specify the language as the second argument. See example below. This applies to all AI API calls.
    corrected_text = ai.autocorrect("Les femes ont cessé de prndre des piluls parce qu'elles étaient encintes.",lang.FRENCH)
    #now corrected_text = "Les femmes ont cessé de prendre des pilules parce qu'elles étaient enceintes."

Autocomplete
-------------------------

Attempts to automatically complete the given sentence to the nearest meaningful sentence.

.. code:: python

    completed_text = ai.autocomplete("which is the fas")
    #now completed_text = "which is the fastest car"


Chatbot
-------

General purpose chatbot which makes use of all other Gurunudi AI apis to have general conversation as well as answer knowledge based queries

.. code:: python

    response = ai.chat("how are you?") #returns a string ex: "I am fine"
    response = ai.chat("where is Badami") #returns a string ex: "in Karnataka, India"
    response = ai.chat("do you eat cakes?") #returns a string ex: "software do not eat"
    response = ai.chat("solve 3x-12=0") #returns a string ex: "4"


Co-reference Resolution
-----------------------

Attempts to resolve co-referenes in a text (like pronouns) to their corresponding nouns.

.. code:: python

    coreferenced_text = ai.coref("Einstein was a brillian scientist. He was born in Germany.")
    #now coreferenced_text = "Einstein was a brillian scientist. Einstein was born in Germany."

    coreferenced_text = ai.coref("The women stopped taking pills because they were pregnant.")
    #now coreferenced_text = "The women stopped taking pills because the women were pregnant"


Definition
----------

Given a word or a noun, provides its definition.

.. code:: python

    definition = ai.define("sun")
    #now definition = "the star that is the source of light and heat for the planets in the solar system"


Fix Case (True Case)
--------------------

Attempts to fix the case for case sensitive language scripts like English to generate true cased sentencete.

.. code:: python

    case_fixed_text = ai.fix_case("delhi is the capital of iNdia")
    #now case_fixed_text = "Delhi is the capital of India"


Intent Extraction
-----------------

Attempts to extract Structured Intent from a natural language sentence. The intent can be then processed by your app to take further actions. Helpful for custom chatbots.
This is the exact opposite process of natural language generation (NLG) API listed below. This takes natural language text as input and gives intent as output.

The Structured Intent format is the same for output of Intent Extraction API, input of Knowledge Graph Query API and input of Natural Language Generation API.

.. code:: python

    intent = ai.intent("hi")
    #returns "[{"intent":"greeting"}]"

    intent = ai.intent("Delhi is in India")
    #returns [{"intent":"statement","theme":"Delhi","attribute":"location","value":"India","tense":"present"}]

    intent = ai.intent("John went to Chicago")
    #returns [{"intent":"statement","agent":"John","action":"go","destination",:"Chicago","tense":"past"}]

    intent = ai.intent("book a flight to mumbai")
    #returns [{"intent":"command","action":"book","theme":"flight","destination":"Mumbai","tense":"present"}]

    intent = ai.intent("where is berlin?")
    #returns [{"intent":"query","theme":"Berlin","query_type":"attribute_value","attribute":"location","tense":"present"}]


Keyword Extraction
------------------

Extracts important keywords from given text. The keywords are ordered in the descending order of significance in relation to the given text.

.. code:: python

    keywords = ai.keywords("Delhi is in India")
    #now keywords = ['India', 'Delhi']


Knowledge Graph Query
---------------------

Query the Gurunudi Knowledge Graph using Structured Intent. 
The Structured Intent format is the same for output of Intent Extraction API, input of Knowledge Graph Query API and input of Natural Language Generation API.

.. code:: python

    answer = ai.graph_query({"theme":"India","attribute":"capital","value":"?"})
    #now answer = {"theme":"India","attribute":"capital","value":"New Delhi"}

    #if language other than English, then specify
    answer = ai.graph_query({"theme":"Inde","attribute":"capitale","value":"?"},lang.FRENCH)
    #now answer = {"theme":"Inde","attribute":"capitale","value":"New Delhi"}


Language Detection
------------------

Identifies the language of a given text. Can also differentiate between Chinese, Korean and Japanese texts.

.. code:: python

    language = ai.language("lorem ipsum")
    #now language = {"iso1":"la","iso3":"lat","language":"Latin"}

    language = ai.language("ನನ್ನ ಹೆಸರು ಗುರು")
    #now language = {"iso1":"kn","iso3":"kan","language":"Kannada"}

    language = ai.lang_name("ನನ್ನ ಹೆಸರು ಗುರು")
    #now language = "Kannada"


Named Entities Extraction
-------------------------

Extracts named entities from a given text.

.. code:: python

    named_entities = ai.named_entities("India is in Asia") #returns a list of named entities, their labels and position in the text
    #now named_entities = [{"label": "GPE", "end": 5, "start": 0, "name": "India"}, {"label": "LOC", "end": 16, "start": 12, "name": "Asia"}]


Natural Language Generation (NLG)
---------------------------------

This API takes Structured Intent as input and gives natural language text as output. This is the exact opposite process of intent extraction API described above. 
The Structured Intent format is the same for output of Intent Extraction API, input of Knowledge Graph Query API and input of Natural Language Generation API.

.. code:: python

    text = ai.generate({"theme":"Delhi","attribute":"location","value":"India"}) 
    #now text = "Delhi is in India."

    text = ai.generate({"theme":"Delhi","attribute":"location","value":"India","intent":"query"}) 
    #now text = "Is Delhi in India?"

    text = ai.generate({"theme":"Delhi","attribute":"location","value":"India","intent":"query","tense":"past"}) 
    #now text = "Was Delhi in India?"


Natural Language Inference (NLI)
--------------------------------

Attempts to find all possible inferences that can be drawn from a given natural language text.

.. code:: python

    list = ai.inferences("New Delhi is the capital city of India") 
    #now list = ["New Delhi is a city.","New Delhi is in India.","India has a capital city.","New Delhi is a location.","New Delhi is an administrative territory.","India is a location.","India is an administrative territory.","New Delhi is a capital city."]

Natural Language Query (NLQ)
----------------------------

Attempts to answer simple queries in natural language using Gurunudi Knowledge Graph.

.. code:: python

    answer = ai.query("what is Tiramisu")
    #now answer = "coffee-flavoured Italian dessert"

Sentiment Analysis
------------------

Analyzes the sentiment of a given text.

.. code:: python

    sentiment = ai.sentiment("I really did not like that movie")
    #now sentiment = "negative"

    sentiment = ai.sentiment ("she is very beautiful")
    #now sentiment = "positive"

    sentiment = ai.sentiment ("The ambience was good, but the food was bad")
    #now sentiment = "mixed"

    sentiment = ai.sentiment ("roses are red, violets are blue")
    #now sentiment = "neutral"


Summary Generation (Summarization)
----------------------------------

Generates a short summary of a long text.

.. code:: python

    summary = ai.summary("<SOME_LONG_TEXT>")
    #now summary = <summary_of_the_long_text>

Text Classification
-------------------

Classifies a text using given classification model

.. code:: python

    from gurunudi import lang

    labels = ai.classify("The apple fell on Newton","tense")
    #now labels = ["past"]

    labels = ai.classify("when did that happen?","mood")
    #now labels = ["interrogative"]

    labels = ai.classify("You have won 1 million dollars","email")
    #now labels = ["spam"]

    labels = ai.classify("India won the ICC world cup","news")
    #now labels = ["sports","cricket"]


Title Generation
----------------

Attempts to suggest a title for a given long text like an article or a document.

.. code:: python

    from gurunudi import lang

    title = ai.title("<SOME_LONG_TEXT>")
    #now title = "<TITLE_SUGGESTED_BY_GURUNUDI_AI>"


Topic Modeling
--------------

Attempts to identify a list of topics that can be associated with a given text

.. code:: python

    topics = ai.topics("Can Trump and Kim end the Korean War?")
    #now topics = ["Politics"]

    topics = ai.topics("Planning To Buy A House? There Is Good News For You")
    #now topics = ["Business"]


Translation
-----------

Attempts to translate text from one language to another.

.. code:: python

    from gurunudi import lang

    #arguments are source text to be translated, target language, source language
    translation = ai.translate("New Delhi is the capital of India",lang.GERMAN,lang.ENGLISH)
    #now translation = "Neu-Delhi ist die Hauptstadt von Indien"
