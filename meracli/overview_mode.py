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
"""Basic access (not logged in)."""
import cmd2
import cowsay
import random

from .dicts import user_mode_string
from .organization_mode import OrganizationMode


class OverviewMode(cmd2.Cmd):
    """[email]>    Logged in. Access to MSP Portal/List of organizations.

    Skip this mode if user has only one organization.
    """
    # Run a shell command if a cmd2/cmd command doesn't exist
    default_to_shell = True
    with open("meracli/protolol.txt") as file:
        joke_number = random.randrange(40)  # 40 jokes in file
        joke = file.readlines()[joke_number]
        file.close()

    intro = cowsay.tux(joke)
    prompt = 'meraCLI>'

    def __init__(self, username, password, cookies):
        super(OverviewMode, self).__init__()
        self.multiline_commands = ['orate']
        self.maxrepeats = 3
        self.agent_vars = {
            'user': username,
            'pass': password,
            'cookies': cookies,
        }

    def do_help(self, *args):
        """Overwrite existing do_help/? command."""
        print("Exec commands:", user_mode_string)

    def do_enable(self, *args):
        """Enter Privileged EXEC mode."""
        self.do_quit('priv')
        cli = OrganizationMode()
        cli.cmdloop("Welcome to Organization mode!")

    def do_exit(self, *args):
        """quit."""
        self.do_quit('quit')
        return True

    def do_logout(self, *args):
        """quit."""
        self.do_quit('quit')
        return True
