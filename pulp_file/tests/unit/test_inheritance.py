from django.test import TestCase
from pulp_file.app.models import FileContent, FilePublisher, FileRemote
from pulpcore.plugin.models import Content, Publisher, Remote


class TestInheritance(TestCase):

    def test_inheritances(self):
        self.assertTrue(issubclass(FileContent, Content))
        self.assertTrue(issubclass(FilePublisher, Publisher))
        self.assertTrue(issubclass(FileRemote, Remote))

    def test_app_reg(self):
        import pydevd
        pydevd.settrace('localhost', port=12345, stdoutToServer=True, stderrToServer=True)