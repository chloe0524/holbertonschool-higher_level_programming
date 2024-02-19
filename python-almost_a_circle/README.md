# :last_quarter_moon_with_face: Python - Almost a circle

## Tasks

:last_quarter_moon_with_face: **Mandatory** 

### Task 0: If it's not tested it doesn't work

All your files, classes and methods must be unit tested and be PEP 8 validated.

**Mandatory**

### Task 1: Base class

**Mandatory**

Write the first class Base:

- Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package.
- Create a file named models/base.py

### Task 2: First Rectangle

**Mandatory**

Write the class Rectangle that inherits from Base:

- In the file models/rectangle.py
- Class Rectangle inherits from Base
- Private instance attributes, each with its own public getter and setter:
    - __width -> width
    - __height -> height
    - __x -> x
    - __y -> y
- Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
- Call the super class with id - this super call with use the logic of the __init__ of the Base class
- Assign each argument width, height, x, and y to the right attribute

### Task 3: Validate attributes

**Mandatory**

Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):

- If the input is not an integer, raise the TypeError exception with the message: <name of the attribute> must be an integer. Example: width must be an integer
- If width or height is under or equals 0, raise the ValueError exception with the message: <name of the attribute> must be > 0. Example: width must be > 0
- If x or y is under 0, raise the ValueError exception with the message: <name of the attribute> must be >= 0. Example: x must be >= 0

### Task 4: Area first

**Mandatory**

Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

### Task 5: Display #0

**Mandatory**

Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.

### Task 6: __str__

**Mandatory**

Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

### Task 7: Display #1

**Mandatory**

Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y

### Task 8: Update #0

**Mandatory**

Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute.

### Task 9: Update #1

**Mandatory**

Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes.

### Task 10: And now, the Square!

**Mandatory**

Write the class Square that inherits from Rectangle:

- In the file models/square.py
- Class Square inherits from Rectangle
- Class constructor: def __init__(self, size, x=0, y=0, id=None):
- Call the super class with id, x, y, width, and height - this super call will use the logic of the __init__ of the Rectangle class. The width and height must be assigned to the value of size

### Task 11: Square size

**Mandatory**

Update the class Square by adding the public getter and setter size.

### Task 12: Square update

**Mandatory**

Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes.

### Task 13: Rectangle instance to dictionary representation

**Mandatory**

Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle.

### Task 14: Square instance to dictionary representation

**Mandatory**

Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square.

### Task 15: Dictionary to JSON string

**Mandatory**

Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries.

### Task 16: JSON string to file

**Mandatory**

Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file.

### Task 17: JSON string to dictionary

**Mandatory**

Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string.

### Task 18: Dictionary to Instance

**Mandatory**

Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set.

### Task 19: File to instances

**Mandatory**

Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances.

:last_quarter_moon_with_face:

```
