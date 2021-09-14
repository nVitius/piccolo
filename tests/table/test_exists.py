from tests.example_apps.music.tables import Band

from ..base import DBTestCase


class TestExists(DBTestCase):
    def test_exists(self):
        self.insert_rows()

        response = Band.exists().where(Band.name == "Pythonistas").run_sync()

        self.assertTrue(response is True)
