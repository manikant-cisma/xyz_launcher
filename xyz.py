#!/usr/bin/env python3
########################################################################################################################
##  Copyright (C) Belmont Computing, Inc. Aug 2021 -- All Rights Reserved
##
##  NOTICE:  All information contained herein is, and remains the property of Belmont Computing, Inc.  The intellectual
##  and technical concepts contained herein are proprietary to Belmont Computing, Inc. and may be covered by U.S. and
##  Foreign Patents, patents in process, and are protected by trade secret or copyright law.  Dissemination of this
##  information or reproduction of this material is strictly forbidden unless prior written permission is obtained from
##  Belmont Computing, Inc.
########################################################################################################################

import sys

from dagogo.services.tool_launcher import ToolLauncher
from dagogo.sml.persist import persistable


@persistable
class Xyz(ToolLauncher):
    def __init__(self, name=None, cmd=None, rundir='./output', pipedir='./output'):
        """
        """
        print(f'## Executing XYZ launcher from: {__file__} ...', flush=True)

        super().__init__(name, cmd, '1.0', rundir, pipedir)

        version = self.get_xyz_version()

        xyz_root = '$_BCI_TEST_DIR_/bridge_remote/input/vendors/xyz'
        self.set_root_dir(xyz_root)

        xyz_bin = f'{xyz_root}/{version}/bin'
        self.set_bin_dir(xyz_bin)


# Standalone CLI Mode.
if __name__ == '__main__':
    sys.exit(Xyz().execute())

