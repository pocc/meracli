# -*- coding: utf-8 -*-
# Copyright 2018 Ross Jacobs All Rights Reserved.
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
"""[email] /org name~  In a specific organization"""
import cmd2

from .dicts import priv_mode_string


class OrganizationMode(cmd2.Cmd):
    """Router#    Priviliged shell for device configuration."""
    prompt = 'meraCLI#'

    def __init__(self):
        super(OrganizationMode, self).__init__()

    def do_help(self, *args):
        """Overwrite existing do_help/? command."""
        print("Exec commands:", priv_mode_string)

    def do_config_terminal(self, *args):
        """Go to Global Config mode"""
        pass

    def do_exit(self, *args):
        """quit to User EXEC mode."""
        self.do_quit('quit')
        return True

    def do_logout(self, *args):
        """quit to User EXEC mode."""
        self.do_quit('quit')
        return True
