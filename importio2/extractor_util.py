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
from datetime import datetime
from time import sleep
import logging
from importio2 import ExtractorAPI

logger = logging.getLogger(__name__)


ACTIVE_TIMEOUT = 5


class ExtractorUtilities(object):

    def __init__(self):
        self.api = ExtractorAPI()
        self._crawl_run_active_timeout = ACTIVE_TIMEOUT

    def crawl_run_active(self, extractor_id, crawl_run_id):
        """
        Determine if a crawl run is in progress for the given extractor id and crawl run id
        :param extractor_id:
        :param crawl_run_id:
        :return: True if the crawl run is not found or is running. False if found and state is FINISHED
        """
        active = True
        extractor = self.api.get(extractor_id)
        name = extractor['name']
        crawl_runs = self.api.get_crawl_runs(extractor_id)

        for run in crawl_runs:
            if run['_id'] == crawl_run_id:
                state = run['fields']['state']
                if state == 'FINISHED':
                    logger.info("FINISHED => name: {0}, id: {1}, crawl_run_id: {2}".format(
                        name, extractor_id, crawl_run_id))
                    active = False
                    break
        return active

    def report_crawl_run_stats(self, extractor_id, crawl_run_id):
        """
        Outputs the some of the metrics of a crawl run
        :param extractor_id: specifices the extractor
        :param crawl_run_id: specifies the crawl run
        :return:
        """
        api = ExtractorAPI()
        extractor = self.api.get(extractor_id)
        name = extractor['name']
        crawl_runs = self.api.get_crawl_runs(extractor_id)
        for run in crawl_runs:
            if run['_id'] == crawl_run_id:
                started_at = datetime.fromtimestamp(int(run['fields']['startedAt'] / 1000))
                total = int(run['fields']['totalUrlCount'])
                failed = int(run['fields']['failedUrlCount'])
                success = int(run['fields']['successUrlCount'])
                rows = int(run['fields']['rowCount'])
                logger.info("name: {0}, started: {1}, total: {2}, success: {3}, failed: {4}, rows: {5}".format(
                    name, started_at, total, success, failed, rows))

    def extractor_run_and_wait(self, extractor_id, report=12):
        """
        Executes a Crawl Run and waits for it to complete

        :param extractor_id:
        :param report: How often to report on crawl run
        :return: None
        """
        extractor = self.api.get(extractor_id)
        name = extractor['name']
        crawl_run_id = self.api.start(extractor_id)
        logger.info("STARTED => name: {0}, id: {1}, crawl_run_id: {2}".format(
            name, extractor_id, crawl_run_id))
        crawl_run_active = True
        count = 1
        while crawl_run_active:
            if not bool(count % report):
                self.report_crawl_run_stats(extractor_id, crawl_run_id)
            sleep(self._crawl_run_active_timeout)
            crawl_run_active = self.crawl_run_active(extractor_id, crawl_run_id)
            count += 1