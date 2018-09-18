import cmd2


class NetworkMode(cmd2.Cmd):
    """[email] /org/network$    Configure global device settings.
    Template networks get $$ instead.
    """
    prompt = 'meraCLI(config)$'

    def __init__(self):
        super(NetworkMode, self).__init__()
