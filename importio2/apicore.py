#
# Copyright 2016 Import.io
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import requests

"""
Low-level REST API calls that specify the inputs and invoke a REST call. Callers
have the responsibility of handling the Requests libraries response object which can be None

"""


def extractor_get(api_key, guid):
    """
    Fetches the contents of an Extractor object from an account

    :param api_key: Import.io user API key
    :param guid: Extractor identifier
    :return: returns response object from requests library
    """

    url = "https://store.import.io/store/extractor/{0}".format(guid)

    querystring = {
        "_apikey": api_key
    }

    headers = {
        'cache-control': "no-cache",
    }

    return requests.request("GET", url, headers=headers, params=querystring)


def extractor_list(api_key, page):
    """
    Fetches the list of Extractors associated to an account

    :param api_key: Import.io user API key
    :param page: which page of the list to display
    :return: returns response object from requests library

    """

    url = "https://store.import.io/store/extractor/_search"

    querystring = {"_sort": "_meta.creationTimestamp",
                   "_mine": "true",
                   "q": "_missing_%3Aarchived%20OR%20archived%3Afalse",
                   "_page": page,
                   "_apikey": api_key
                   }

    headers = {
        'cache-control': "no-cache",
    }

    return requests.request("GET", url, headers=headers, params=querystring)


def extractor_get_crawl_runs(api_key, guid, page, per_page):
    """

    :param api_key: Import.io user API key
    :param guid: Extractor identifier
    :param page: Specific crawl run page to display
    :param per_page: Number of crawl runs per page
    :return: returns response object from requests library
    """

    url = "https://store.import.io/store/crawlrun/_search"

    querystring = {"_sort": "_meta.creationTimestamp",
                   "_page": page,
                   "_perPage": per_page,
                   "extractorId": guid,
                   "_apikey": api_key
                   }
    headers = {
        'cache-control': "no-cache",
    }

    return requests.request("GET", url, headers=headers, params=querystring)


def extractor_start(api_key, guid):
    """
    Initiates an crawl run of an extractor

    :param api_key: Import.io user API key
    :param guid: Extractor identifier
    :return: Response object from requests REST call
    """

    url = "https://run.import.io/{0}/start".format(guid)

    querystring = {
        "_apikey": api_key
    }

    headers = {
        'cache-control': "no-cache",
    }

    return requests.request("POST", url, headers=headers, params=querystring)

