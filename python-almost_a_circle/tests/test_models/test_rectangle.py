import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_str(self):
        r = Rectangle(3, 4)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 3/4")

    def test_rectangle_display(self):
        r = Rectangle(2, 2)
        r.display()

    def test_rectangle_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_rectangle_update_args(self):
        r = Rectangle(1, 1)
        r.update(10, 2, 3, 4, 5)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_rectangle_update_kwargs(self):
        r = Rectangle(1, 1)
        r.update(id=10, width=2, height=3, x=4, y=5)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_rectangle_to_dictionary(self):
        r = Rectangle(1, 1)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict, {'id': 1, 'width': 1, 'height': 1, 'x': 0, 'y': 0})

    def test_rectangle_create(self):
        r = Rectangle.create(**{'id': 10, 'width': 2, 'height': 3, 'x': 4, 'y': 5})
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_rectangle_save_and_load_from_file(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].width, 2)
        self.assertEqual(rectangles[1].height, 5)


if __name__ == '__main__':
    unittest.main()
