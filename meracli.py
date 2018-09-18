# -*- coding: utf-8 -*-
"""Meraki CLI."""
from meracli.overview_mode import OverviewMode
from merlink.browsers.dashboard import DashboardBrowser


def main(*args):
    """Starts the program."""
    agent = DashboardBrowser()
    login_result = agent.login(args[1], args[2])
    if login_result:
        cookies = agent.browser.get_cookies()
        cli = OverviewMode(args[1], args[2], cookies)
        cli.cmdloop()


if __name__ == '__main__':
    main()
