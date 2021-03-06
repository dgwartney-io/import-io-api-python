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
from __future__ import absolute_import

from importio2 import API
from unittest import TestCase


class TestAPI(TestCase):

    def test_get_extractor_api_instance(self):
        api = API()
        self.assertIsNotNone(api.extractor, "api.extractor returned None instance")

    def test_get_crawl_run_api_instance(self):
        api = API()
        self.assertIsNone(api.crawl_run, "api.crawl_run returned not None instance")



