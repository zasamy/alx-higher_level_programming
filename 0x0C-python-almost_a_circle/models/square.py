#!/usr/bin/python3
"""square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initiallize attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieve size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if args and len(agrs) != 0:
            i = 0
            for z in args:
                if i == 0:
                    if z is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = z
                elif i == 1:
                    self.size = z
                elif i == 2:
                    self.x = z
                elif i == 3:
                    self.y = z
                i += 1

        elif kwargs and len(kwargs) != 0:
            for s, v in kwargs.items():
                if s == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif s == "size":
                    self.size = v
                elif s == "x":
                    self.x = v
                elif s == "y":
                    self.y = v

    def __str__(self):
        """string representation of squre"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def to_dictionary(self):
        """returns dictionary representation of square"""
        dt = {}
        dt["id"] = self.id
        dt["size"] = self.size
        dt["x"] = self.x
        dt["y"] = self.y
        return dt
