==================================
JSON API and Django Rest Framework
==================================

--------
Overview
--------

**JSON API support for Django REST Framework**

* Documentation: https://django-rest-framework-json-api.readthedocs.org/
* Format specification: http://jsonapi.org/format/


By default, Django REST Framework will produce a response like::

    {
        "count": 20,
        "next": "http://example.com/api/1.0/identities/?page=3",
        "previous": "http://example.com/api/1.0/identities/?page=1",
        "results": [{
            "id": 3,
            "username": "john",
            "full_name": "John Coltrane"
        }]
    }


However, for an ``identity`` model in JSON API format the response should look
like the following::

    {
        "links": {
            "prev": "http://example.com/api/1.0/identities",
            "self": "http://example.com/api/1.0/identities?page=2",
            "next": "http://example.com/api/1.0/identities?page=3",
        },
        "data": [{
            "type": "identities",
            "id": "3",
            "attributes": {
                "username": "john",
                "full-name": "John Coltrane"
            }
        }],
        "meta": {
            "pagination": {
              "count": 20
            }
        }
    }


-----
Goals
-----

As a Django REST Framework JSON API (short DJA) we are trying to address following goals:

1. Support the `JSON API`_ spec to compliance

2. Be as compatible with `Django REST Framework`_ as possible

   e.g. issues in Django REST Framework should be fixed upstream and not worked around in DJA

3. Have sane defaults to be as easy to pick up as possible

4. Be solid and tested with good coverage

5. Be performant

.. _JSON API: http://jsonapi.org
.. _Django REST Framework: https://www.django-rest-framework.org/

------------
Requirements
------------

1. Python (3.5, 3.6, 3.7, 3.8)
2. Django (2.2, 3.0, 3.1)
3. Django REST Framework (3.12)


Settings
^^^^^^^^

For doing this we can either add ``rest_framework_json_api.parsers.JSONParser`` and
``rest_framework_json_api.renderers.JSONRenderer`` to each ``ViewSet`` class, or
override ``settings.REST_FRAMEWORK``

::

    REST_FRAMEWORK = {
        'PAGE_SIZE': 10,
        'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
        'DEFAULT_PAGINATION_CLASS':
            'rest_framework_json_api.pagination.JsonApiPageNumberPagination',
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework_json_api.parsers.JSONParser',
            'rest_framework.parsers.FormParser',
            'rest_framework.parsers.MultiPartParser'
        ),
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework_json_api.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ),
        'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
        'DEFAULT_FILTER_BACKENDS': (
            'rest_framework_json_api.filters.QueryParameterValidationFilter',
            'rest_framework_json_api.filters.OrderingFilter',
            'rest_framework_json_api.django_filters.DjangoFilterBackend',
            'rest_framework.filters.SearchFilter',
        ),
        'SEARCH_PARAM': 'filter[search]',
        'TEST_REQUEST_RENDERER_CLASSES': (
            'rest_framework_json_api.renderers.JSONRenderer',
        ),
        'TEST_REQUEST_DEFAULT_FORMAT': 'vnd.api+json'
    }

This package provides much more including automatic inflection of JSON keys, extra top level data (using nested
serializers), relationships, links, paginators, filters, and handy shortcuts.
