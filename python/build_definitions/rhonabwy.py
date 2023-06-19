#
# Copyright (c) YugaByte, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations
# under the License.
#

from yugabyte_db_thirdparty.build_definition_helpers import *  # noqa


class RhonabwyDependency(Dependency):
    """
    rhonabwy is one of the dependencies of TODO.
    """
    def __init__(self) -> None:
        super(RhonabwyDependency, self).__init__(
            'rhonabwy',
            '1.1.11',
            'https://github.com/babelouest/rhonabwy/archive/refs/tags/v{0}.tar.gz',
            BUILD_GROUP_COMMON)
        self.patches = ['rhonabwy_fix_cmake.patch']
        self.copy_sources = True

    def build(self, builder: BuilderInterface) -> None:
        builder.build_with_cmake(self, ['-DWITH_JOURNALD=OFF', '-DBUILD_RNBYC=OFF'])
