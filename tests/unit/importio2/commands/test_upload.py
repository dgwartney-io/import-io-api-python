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

from unittest import TestCase
import tempfile
import os
from ebayio import DataUpload


class TestUpload(TestCase):

    def setUp(self):
        # Make temporary directory with sub directories
        dir = tempfile.mkdtemp()
        os.path.

































































    def tearDown(self):
        pass

    def test_constructor(self):
        upload = DataUpload()
        self.assertIsNotNone(upload)

    def test

