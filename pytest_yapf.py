import os

from yapf.yapflib import file_resources
from yapf.yapflib.style import CreateStyleFromConfig
from yapf.yapflib.yapf_api import FormatFile

import pytest


def pytest_addoption(parser):
    group = parser.getgroup('yapf')
    group.addoption('--yapf', action='store_true', help='run yapf on *.py files.')
    group.addoption('--yapfdiff', action='store_true', help='show diff of yapf output.')
    group.addoption('--yapfstyle', action='store', dest='yapfstyle', default=None, help='style to be used by yapf.')


def pytest_collect_file(path, parent):
    config = parent.config
    if config.option.yapf and path.ext == '.py':
        return YapfItem(path, parent)


class YapfError(Exception):
    pass


class YapfItem(pytest.Item, pytest.File):
    def __init__(self, path, parent):
        super(YapfItem, self).__init__(path, parent)
        self.path = str(path)
        self.show_diff = self.parent.config.option.yapfdiff is True
        self.style = self.parent.config.getoption('yapfstyle') or file_resources.GetDefaultStyleForDir(self.path)

    def runtest(self):
        filename = self.path
        error = None
        try:
            diff, encoding, is_changed = FormatFile(self.path, style_config=self.style, print_diff=True)
        except BaseException as e:
            raise BaseException(e)
        if is_changed:
            file_lines = diff.split('\n')
            lines_added = len([x for x in file_lines if x.startswith('+')])
            lines_removed = len([x for x in file_lines if x.startswith('-')])

            message = "ERROR: %s Code formatting is not correct." % (filename, )
            message = "%s\n       Diff: -%s/+%s lines" % (message, lines_removed, lines_added)

            if self.show_diff:
                message = "%s\n\n%s" % (message, diff)

            raise YapfError(message)

    def repr_failure(self, excinfo):
        if excinfo.errisinstance(YapfError):
            return excinfo.value.args[0]
        return super().repr_failure(excinfo)
