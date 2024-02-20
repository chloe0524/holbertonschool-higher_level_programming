import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_base_auto_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_base_auto_increment_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj2.id, obj1.id + 1)

    def test_base_given_id(self):
        obj = Base(89)
        self.assertEqual(obj.id, 89)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')
        self.assertIsInstance(Base.to_json_string([{'id': 12}]), str)

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])
        self.assertIsInstance(Base.from_json_string('[{"id": 89}]'), list)


if __name__ == '__main__':
    unittest.main()
