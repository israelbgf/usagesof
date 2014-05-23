__author__ = 'israel.bgf'


class Usages:

    def __init__(self, from_file):
        self.from_file = from_file

    def lookup(self, command):
        usages = []
        for line in open(self.from_file):
            if line.startswith(command):
                usages.append(tuple(map(lambda x: x.strip(), line.split(">>>"))))
        return usages


class Formatter:

    START_DEFAULT = '\033[0'
    START_BOLD = '\033[1'

    def format(self, command_usage):
        command, usage = command_usage.split(">>>")
        return self.format_command(command) + "\n\n" + self.format_usage(usage)

    def format_command(self, command):
        return self.START_BOLD + command + self.START_DEFAULT

    def format_usage(self, usage):
        return usage.replace('{', self.START_BOLD).replace('}', self.START_DEFAULT)
