class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, new_hexcode):
        self._hexcode = new_hexcode
        self.r = int(self._hexcode[0:2], 16)
        self.g = int(self._hexcode[2:4], 16)
        self.b = int(self._hexcode[4:6], 16)


color = Color('0000FF')

color.hexcode = 'A782E3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)