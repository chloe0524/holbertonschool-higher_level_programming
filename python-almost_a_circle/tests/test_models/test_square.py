import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        s = Square(2)
        self.assertEqual(s.size, 2)

    def test_square_str(self):
        s = Square(3)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 3")

    def test_square_display(self):
        s = Square(2)
        s.display()

    def test_square_area(self):
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_square_update_args(self):
        s = Square(1)
        s.update(10, 2, 3, 4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_square_update_kwargs(self):
        s = Square(1)
        s.update(id=10, size=2, x=3, y=4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_square_to_dictionary(self):
        s = Square(1)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict, {'id': 1, 'size': 1, 'x': 0, 'y': 0})

    def test_square_create(self):
        s = Square.create(**{'id': 10, 'size': 2, 'x': 3, 'y': 4})
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_square_save_and_load_from_file(self):
        s1 = Square(2)
        s2 = Square(3)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0].size, 2)
        self.assertEqual(squares[1].size, 3)


if __name__ == '__main__':
    unittest.main()
