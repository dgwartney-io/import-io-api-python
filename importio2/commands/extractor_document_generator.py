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
import argparse
import logging
import sys
import os
from importio2 import ExtractorAPI
from importio2 import CrawlRunAPI


logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


class CrawlRunMetadata(object):

    def __init__(self):
        pass


class ExtractorMetadata(object):

    def __init__(self):
        self.crawl_runs = []


class ExtractorDocumentGenerator(object):

    def __init__(self):
        self._filter = None

    def handle_arguments(self):
        parser = argparse.ArgumentParser(description="Generates Extractor Documentation")
        parser.add_argument('-f', '--filter', action='store', dest='filter', metavar='regexp',
                            help="Filter Extractors based on Regular Expression")
        args = parser.parse_args()

        if args.filter is not None:
            self._filter = args.filter

    def get_extractor_ids(self):
        api = ExtractorAPI()
        extractor_list = api.list()
        print(extractor_list)

        for extractor in extractor_list:
            print(extractor)

    def generate_documentation(self):
        self.get_extractor_ids()

    def execute(self):
        self.handle_arguments()
        self.generate_documentation()


def main():
    cli = ExtractorDocumentGenerator()
    cli.execute()


if __name__ == '__main__':
    main()
