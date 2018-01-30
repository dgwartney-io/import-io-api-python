#!/usr/bin/env python
#
# Copyright 2018 Import.io
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
from importio2.commands import AdBase
from importio2 import ExtractorAPI
import logging
import json

logging.basicConfig(level=logging.ERROR)


class AccountStats(AdBase):

    def __init__(self):
        self._command = None
        self._count = None
        self._dump = None
        self._list = None
        self._monitor = None
        super(AccountStats, self).__init__()

    def cli_description(self):
        """
        Provides the description of what operation this CLI performs
        :return: Description of the CLI's operation
        """
        return 'Extracts data about the Extractors/Crawl Runs in an account'

    def get_arguments(self):
        """
        Returns the required arguments after they are processed by handle_arguments
        :return:
        """
        self._count = self._args.count
        self._dump = self._args.dump
        self._list = self._args.list
        self._monitor = self._args.monitor
        super(AccountStats, self).get_arguments()

    def handle_arguments(self):
        group = self._parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-c', '--count', action='store_true',dest='count', default=False,
                           help='Provide a count of the extractors in the account')
        group.add_argument('-d', '--dump', action='store_true',dest='dump', default=False,
                           help='Export all Extractor/Crawl Run information account')
        group.add_argument('-l', '--list', action='store_true', dest='list', default=False,
                           help='Provide a list of the extractors in the account')
        group.add_argument('-m', '--monitor', action='store_true', dest='monitor', default=False,
                           help='Monitors each extractor and looks at each of the crawl runs')
        super(AccountStats, self).handle_arguments()

    def run(self, api_key=None):
        """
        Executes the CLIs operation which is to get the statistics of all Extractors/Crawl Runs
        :param api_key: Import.io API Key from the account that has the extractor to download from
        :return: None
        """
        if api_key is not None:
            self._api_key = api_key

    def do_list_extractors(self):
        api = ExtractorAPI()
        logging.basicConfig(level=logging.ERROR)
        extractor_list = api.list()
        count = 0

        for extractor in extractor_list:
            count += 1
#           if 'parentExtractorGuid' in extractor:
            extractor_data = json.dumps(extractor)
            print(extractor_data)
            name = extractor['fields']['name']
            print(name)
        print("extractor_count: {0}".format(count))

    def get_crawl_runs(self, guid):
        api = ExtractorAPI()
        extractor_name = api.get(guid)['name']
        logging.basicConfig(level=logging.ERROR)
        crawl_run_list = api.get_crawl_runs(guid)
        for crawl_run in crawl_run_list:
            print("extractor_name: {0}, id: {1}".format(extractor_name, crawl_run['_id']))

    def do_dump(self):
        api = ExtractorAPI()
        extractor_list = api.list()
        for extractor in extractor_list:
            extractor_data = json.dumps(extractor)
            guid = extractor['_id']
            self.get_crawl_runs(guid)

    def execute(self):
        """
        Main entry point for the CLI
        :return: None
        """
        super(AccountStats, self).execute()
        logging.basicConfig(level=logging.ERROR)

        if self._list:
            self.do_list_extractors()
        if self._dump:
            self.do_dump()


def main():
    cli = AccountStats()
    cli.execute()


if __name__ == '__main__':
    main()
