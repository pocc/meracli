import cmd2


class InterfaceConfigMode(cmd2.Cmd):
    """[email] /Org/Net/Device Name#

    Configure interface settings."""
    def __init__(self):
        super(InterfaceConfigMode, self).__init__()


