Gurunudi AI API: Python client
******************************

**Gurunudi** is a Python library by `GuruLaghu Technologies <https://gurulaghu.com/>`_ for accessing the `Gurunudi Artificial Intelligence API <https://www.gurunudi.com/>`_.
Gurunudi (**AI as a Service**) provides a wide range of **Artificial Intelligence based API solutions** (See below). This client library for Gurunudi AI API is commercial open-source software, released under the MIT license.

💫 **Version 1.2.1 out now!**

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
* Text Classification - Language Detection, Sentiment Analysis, Text Classification and more 
* Text Analysis - Named Entities, Sentence Extraction, Syntax Analysis, Dependency Parse Tree, Intent Extraction and more 
* Text Generation - Chatbot, Topic Modeling, Definitions, Summarization, Title Generation, Keyword Extraction, Topic Modeling, Translation and more
* Text Transformation - Co-reference Resolution, Fix Case (True Case), Spell Check and more
* Knowledge Graph - available via chatbot (Definition, Attributes, Events, Lists and more)
* Custom Trained Bots - Domain Experts, Customer Support, FAQ and more
* More cutting edge AI features are being added continuously


📖 Documentation
================

Basics
------

.. code:: python

    from gurunudi import AI,api

    api.key='<YOUR_API_KEY>' #Set your Gurunudi API Key
    ai=AI("sample text")

API key needs to be setup at the beginning only once in an application. Visit `https://gurulaghu.com <https://gurulaghu.com>` to get an API key.

AI is a class with simple yet intelligent attributes. Create an AI object by passing your text as the argument. AI takes a second optional argument as the language code which if not present, defaults to English (except for language detection call). The language code is a 3-letter `ISO 639-3 code <https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes>`_. For language codes and features currently supported by each language, see `supported languages <https://gurulaghu.com/languages/>`_.

.. code:: python

    from gurunudi import lang
    ai=AI("ಕರ್ನಾಟಕ ಕನ್ನಡ",lang.KANNADA) #Specify the language if non-English text

Chatbot
-------

.. code:: python

    response = AI("how are you?").chat #returns a string ex: "I am fine"
    response = AI("where is Badami").chat #returns a string ex: "in Karnataka, India"
    response = AI("do you eat cakes?").chat #returns a string ex: "software do not eat"
    response = AI("solve 3x-12=0").chat #returns a string ex: "4"


Co-reference Resolution
-----------------------

.. code:: python

    coreferenced_text = AI("Einstein was a brillian scientist. He was born in Germany.").coreferenced_text
    #now coreferenced_text = "Einstein was a brillian scientist. Einstein was born in Germany."

    coreferenced_text = AI("The women stopped taking pills because they were pregnant.").coreferenced_text
    #now coreferenced_text = "The women stopped taking pills because the women were pregnant"


Definition
----------

.. code:: python

    definition = AI("sun").definition 
    #now definition = "the star that is the source of light and heat for the planets in the solar system"


Fix Case
--------

.. code:: python

    case_fixed_text = AI("delhi is the capital of iNdia").fix_case
    #now case_fixed_text = "Delhi is the capital of India"


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


Keyword Extraction
------------------

.. code:: python

    keywords = AI("Delhi is in India").keywords
    #now keywords = ['India', 'Delhi']


Language Detection
------------------

.. code:: python

    language = AI("lorem ipsum").language
    #now language = "Latin"

    language = AI("ನನ್ನ ಹೆಸರು ಗುರು").language
    #now language = "Kannada"


Named Entities
--------------

.. code:: python

    named_entities = AI("India is in Asia").named_entities #returns a list of named entities, their labels and position in the text
    #now named_entities = [{"label": "GPE", "end": 5, "start": 0, "name": "India"}, {"label": "LOC", "end": 16, "start": 12, "name": "Asia"}]


Sentence Extraction
-------------------

.. code:: python

    sentences = AI("Mr. India was a great movie. It was directed by Shekhar Kapur.").sentences
    #now sentences = ["Mr. India was a great movie.", "It was directed by Shekhar Kapur."]


Sentiment Analysis
------------------

.. code:: python

    sentiment = AI("I really did not like that movie").sentiment 
    #now sentiment = "negative"

    sentiment = AI("she is very beautiful").sentiment #returns "positive"
    #now sentiment = "positive"

    sentiment = AI("The ambience was good, but the food was bad").sentiment #returns "mixed"
    #now sentiment = "mixed"

    sentiment = AI("roses are red, violets are blue").sentiment #returns "neutral"
    #now sentiment = "neutral"


Spell Check
-----------

.. code:: python

    corrected_text = AI("whois cming tmorrow").spell_checked_text
    #now corrected_text = "who is coming tomorrow"


Summary Generation
------------------

.. code:: python

    summary = AI("<SOME_LONG_TEXT>").summary
    #now summary = <summary_of_the_long_text>


Syntax Analysis
---------------

.. code:: python

    syntax = AI("Moon creates waves").syntax
    #now syntax = [{'pos': 'PROPN', 'lemma': 'moon', 'text': 'Moon'}, {'pos': 'VERB', 'lemma': 'create', 'text': 'creates'}, {'pos': 'NOUN', 'lemma': 'wave', 'text': 'waves'}]


Syntax Dependency Tree
----------------------

.. code:: python

    syntax_tree = AI("Moon creates waves").syntax_tree
    #now syntax_tree = [{'head': 1, 'dep': 'nsubj', 'text': 'Moon'}, {'head': 1, 'dep': 'ROOT', 'text': 'creates'}, {'head': 1, 'dep': 'dobj', 'text': 'waves'}]


Title Generation
----------------

.. code:: python

    from gurunudi import lang

    title = AI("<SOME_LONG_TEXT>").title
    #now title = "<TITLE_SUGGESTED_BY_GURUNUDI_AI>"


Topics
--------

.. code:: python

    topics = AI("Can Trump and Kim end the Korean War?").topics
    #now topics = ["Politics"]

    topics = AI("Planning To Buy A House? There Is Good News For You").topics
    #now topics = ["Business"]


Translate
---------

.. code:: python

    from gurunudi import lang

    translation = AI("India").translate(lang.GERMAN)
    #now translation = "Indien"
