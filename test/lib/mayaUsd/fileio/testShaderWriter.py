#!/usr/bin/env mayapy
#
# Copyright 2021 Autodesk
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

import mayaUsd.lib as mayaUsdLib

from pxr import Gf
from pxr import Sdf
from pxr import Tf
from pxr import Vt
from pxr import UsdGeom

from maya import cmds
import maya.api.OpenMaya as OpenMaya
from maya import standalone

import fixturesUtils, os

import unittest

class shaderWriterTest(mayaUsdLib.ShaderWriter):
    def Write(self, usdTime):
         print("shaderWriterTest.Write called")

    def PostExport(self):
         print("shaderWriterTest.PostExport called")
         return False

class testShaderWriter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixturesUtils.setUpClass(__file__)

    @classmethod
    def tearDownClass(cls):
        standalone.uninitialize()

    def setUp(self):
        cmds.file(new=True, force=True)

    def testSimpleShaderWriter(self):
        mayaUsdLib.ShaderWriter.Register(shaderWriterTest, "test")


if __name__ == '__main__':
    unittest.main(verbosity=2)