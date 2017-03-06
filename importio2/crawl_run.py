#
# Copyright 2017 Import.io
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
import os
import importio2.apicore as apicore
import requests


class CrawlRunAPI(object):

    def __init__(self):
        self._api_key = os.environ['IMPORT_IO_API_KEY']

    def create(self,
               extractor_id,
               failed_url_count,
               success_url_count,
               total_url_count,
               row_count,
               started_at,
               stopped_at,
               state='FINISHED'):
        """
        Creates a Crawl Run in an extractor
        :param extractor_id: Extractor to create the crawl run
        :param failed_url_count: Number of failed URLs in the run
        :param success_url_count: Number of Success URLs in the run
        :param total_url_count: Total number of URLs in the run
        :param row_count: Total rows returned by the run
        :param started_at: Time when run began
        :param stopped_at: Time when run finished
        :param state: Final state
        :return: crawl run id
        """
        data = {
            'extractorId': extractor_id,
            'failedUrlCount': failed_url_count,
            'successUrlCount': success_url_count,
            'totalUrlCount': total_url_count,
            'rowCount': row_count,
            'startedAt': started_at,
            'stoppedAt': stopped_at,
            'state': state
        }
        response = apicore.object_store_create(self._api_key, 'crawlRun', data)
        response.raise_for_status()
        crawl_run_id = None
        if response.status_code == requests.codes.created:
            result = response.json()
            crawl_run_id = result['guid']

        return crawl_run_id




