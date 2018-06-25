Gurunudi AI API: Python client
******************************

**Gurunudi** is a Python library by `GuruLaghu Technologies <https://gurulaghu.com/>`_ for accessing the `Gurunudi Artificial Intelligence API <https://www.gurunudi.com/>`_.
Gurunudi (**AI as a Service**) provides a wide range of **Artificial Intelligence based API solutions** (See below). This client library for Gurunudi AI API is commercial open-source software, released under the MIT license.

💫 **Version 0.21 out now!**

.. image:: https://img.shields.io/pypi/v/gurunudi.svg?style=flat-square
    :target: https://pypi.python.org/pypi/gurunudi
    :alt: pypi Version

.. image:: https://img.shields.io/badge/chat-join%20%E2%86%92-09a3d5.svg?style=flat-square&logo=gitter-white
    :target: https://gitter.im/gurulaghu/gurunudi
    :alt: Gurunudi on Gitter 

.. image:: https://img.shields.io/twitter/follow/gurunudi.svg?style=social&label=Follow
    :target: https://twitter.com/gurunudi
    :alt: gurunudi on Twitter

📖 Installation
================

===================  ===
**Operating system** macOS / OS X, Linux, Windows
**Python version**   2+
**Package managers** `pip`_ (source packages only)
===================  ===

.. _pip: https://pypi.python.org/pypi/gurunudi

pip
---

Using pip, gurunudi releases are currently only available as source packages.

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

    pip install -U gurunudi

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
* Text Analysis - Chatbot, Language Detection, Sentiment Analysis, Named Entities, Co-reference Resolution, Topic Modeling, Spell Check, and more
* Knowledge Graph - available via chatbot
* Translation
* More cutting edge AI features are being added continuously


📖 Documentation
================

Basics
------

.. code:: python

    from gurunudi import AI,api

    api.key='<YOUR_API_KEY>' #Set your Gurunudi API Key
    AI("sample text")

API key needs to be setup at the beginning only once in an application. Visit `https://gurulaghu.com <https://gurulaghu.com>` to get an API key.

AI is a class with simple yet intelligent attributes. Create an AI object by passing your text as the argument. AI takes a second optional argument as the language code which if not present, defaults to English (except for language detection call). The language code is a 3-letter `ISO 639-3 code <https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes>`_. For language codes and features currently supported by each language, see `supported languages <https://gurulaghu.com/languages/>`_.

Chatbot
-------

.. code:: python

    response = AI("how are you?").chat #returns a string ex: "I am fine"
    response = AI("where is Badami").chat #returns a string ex: "in Karnataka, India"
    response = AI("do you eat cakes?").chat #returns a string ex: "softwares do not eat"
    response = AI("solve 3x-12=0").chat #returns a string ex: "4"


Intent
------

.. code:: python

    intent = AI("hi").intent
    #returns "[{"intent":"greeting"}]"

    intent = AI("Delhi is in India").language 
    #returns [{"intent":"statement","theme":"Delhi","attribute":"location","value",:"India","tense":"present"}]

    intent = AI("John went to Chicago").language 
    #returns [{"intent":"statement","agent":"John","action":"go","destination",:"Chicago","tense":"past"}]

    intent = AI("book a flight to mumbai").language
    #returns [{"intent":"command","action":"book","theme":"flight","destination":"Mumbai","tense":"present"}]

    intent = AI("where is berlin?").intent
    #returns [{"intent":"query","theme":"Berlin","query_type":"attribute_value","attribute":"location","tense":"present"}]


Language Detection
------------------

.. code:: python

    language = AI("lorem ipsum").language #returns "Latin"
    language = AI("ನನ್ನ ಹೆಸರು ಗುರು").language #returns "Kannada"

Sentiment Analysis
------------------

.. code:: python

    sentiment = AI("I really did not like that movie").sentiment #returns "negative"
    sentiment = AI("she is very beautiful").sentiment #returns "positive"
    sentiment = AI("The ambience was good, but the food was bad").sentiment #returns "mixed"
    sentiment = AI("roses are red, violets are blue").sentiment #returns "neutral"


Co-reference Resolution
-----------------------

.. code:: python

    coreferenced_text = AI("Einstein was a brillian scientist. He was born in Germany.").coreferenced_text
    #now coreferenced_text = "Einstein was a brillian scientist. Einstein was born in Germany."

    coreferenced_text = AI("The women stopped taking pills because they were pregnant.").coreferenced_text
    #now coreferenced_text = "The women stopped taking pills because the women were pregnant"


Spell Check
-----------

.. code:: python

    corrected_text = AI("whois that") #fixes any spelling errors and returns the corrected text
    #now corrected_text = "who is that"


Definition
----------

.. code:: python

    definition = AI("New Delhi").defintion #returns the definition of given word. The word can be a noun or a lexical item or a phrase
    #now definition = "capital of India"


Translate
---------

.. code:: python

    translation = AI("India").translate(gurunudi.GERMAN) #currently only word to word translations are supported
    #now translation = ""


Named Entities
--------------

.. code:: python

    named_entities = AI("India is in Asia").named_entities #returns a list of named entities, their labels and position in the text
    #now named_entities = [{"label": "GPE", "end": 5, "start": 0, "name": "India"}, {"label": "LOC", "end": 16, "start": 12, "name": "Asia"}]


Topics
--------

.. code:: python

    topics = AI("Can Trump and Kim end the Korean War?").topics
    #now topics = ["Politics"]

    topics = AI("Planning To Buy A House? There Is Good News For You").topics
    #now topics = ["Business"]


Summary
--------

.. code:: python

    summary = AI("<SOME_LARGE_TEXT>").summary
    #now summary contains a short summary text


Title
--------

.. code:: python

    title = AI("<SOME_LARGE_TEXT>").title
    #now title contains an appropriate title for the text


Keywords
--------

.. code:: python

    keywords = AI("India is a country in South Asia. It shares land borders with Pakistan to the west; China, Nepal, and Bhutan to the northeast; and Myanmar (Burma) and Bangladesh to the east.").keywords
    #now keywords = ["Pakistan", "Nepal", "India", "country", "Bhutan", "South Asia", "Myanmar", "northeast", "land borders", "Burma", "east", "Bangladesh", "west", "China"]


Sentence Extraction
-------------------

.. code:: python

    sentences = AI("Mr. India was a great movie. It was directed by Shekhar Kapur.").sentences
    #now sentences = ["Mr. India was a great movie.", "It was directed by Shekhar Kapur."]


Syntax Analysis (Part-of-speech tagging)
----------------------------------------

.. code:: python

    syntax = AI("Indian scientists discover new planet").syntax
    #now syntax =  [{'pos': 'ADJ', 'lemma': 'indian', 'text': 'Indian', 'index': 1}, {'pos': 'NOUN', 'lemma': 'scientist', 'text': 'scientists', 'index': 2}, {'pos': 'VERB', 'lemma': 'discover', 'text': 'discover', 'index': 3}, {'pos': 'ADJ', 'lemma': 'new', 'text': 'new', 'index': 4}, {'pos': 'NOUN', 'lemma': 'planet', 'text': 'planet', 'index': 5}]


Dependency Parse Tree
---------------------

.. code:: python

    dependency = AI("Indian scientists discover new planet").dependency
    #now dependency =  [{'text': 'Indian scientists discover new planet', 'dependencies': [{'dependency': 'amod', 'head': 2, 'text': 'Indian', 'index': 1}, {'dependency': 'nsubj', 'head': 3, 'text': 'scientists', 'index': 2}, {'dependency': 'ROOT', 'head': 3, 'text': 'discover', 'index': 3}, {'dependency': 'amod', 'head': 5, 'text': 'new', 'index': 4}, {'dependency': 'dobj', 'head': 3, 'text': 'planet', 'index': 5}]


Sentence Extraction
-------------------

.. code:: python

    sentences = AI("Mr. India was a great movie. It was directed by Shekhar Kapur.").sentences
    #now sentences = ["Mr. India was a great movie.", "It was directed by Shekhar Kapur."]
