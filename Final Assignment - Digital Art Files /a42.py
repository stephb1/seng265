#!/usr/bin/env python
import random as rd
from enum import Enum
from typing import IO, List, NamedTuple

class HtmlDocument:
    """An HTML document that allows appending SVG content"""
    TAB: str = "   "  # HTML indentation tab (default: three spaces)

    def __init__(self, file_name: str, win_title: str) -> None:
        """HtmlDocument constructor creates an instance of HtmlDocument when the class is called"""
        self.win_title: str = win_title
        self.__tabs: int = 0
        self.__file: IO = open(file_name, "w")
        self.__write_head()

    def increase_indent(self) -> None:
        """increase_indent method: Increases the number of tab characters used for indentation"""
        self.__tabs += 1

    def decrease_indent(self) -> None:
        """decrease_indent method: Decreases the number of tab characters used for indentation"""
        self.__tabs -= 1

    def append(self, content: str) -> None:
        """append method: Appends the given HTML content to this document"""
        ts: str = HtmlDocument.TAB * self.__tabs
        self.__file.write(f'{ts}{content}\n')

    def __write_head(self) -> None:
        """write_head method: Appends the HTML preamble to this document"""
        self.append('<html>')
        self.append('<head>')
        self.increase_indent()
        self.append(f'<title>{self.win_title}</title>')
        self.decrease_indent()
        self.append('</head>')
        self.append('<body>')


class CircleShape:
    """A circle shape representing an SVG circle element"""
    ccnt: int = 0  # counting number of circles being constructed

    @classmethod
    def get_circle_count(cls) -> int:
        """counts the number of circles created"""
        return CircleShape.ccnt

    def __init__(self, x: int, y: int, rad: int, rx: int, ry: int, width: int, height: int, red: int, gre: int, blu: int, op: float) -> None:
        """Initializes a circle"""
        self.sha: int = 0
        self.x: int = x
        self.y: int = y
        self.rad: int = rad
        self.rx: int = rx
        self.ry: int = ry
        self.width: int = width
        self.height: int = height
        self.red: int = red
        self.gre: int = gre
        self.blu: int = blu
        self.op: float = op
        CircleShape.ccnt += 1

    def as_svg(self) -> str:
        """as_svg method: Produces the SVG code representing this shape"""
        return f'<circle cx="{self.x}" cy="{self.y}" r="{self.rad}" ' \
               f'fill="rgb({self.red},{self.gre},{self.blu})" ' \
               f'fill-opacity="{self.op}"></circle>'

    def __str__(self) -> str:
        """str method: String representation of CircleShape"""
        return f'{self.sha:>3} {self.x:>3} {self.y:>3} {self.rad:>3} {self.rx:>3} {self.ry:>3} {self.width:>3} {self.height:>3} {self.red:>3} {self.gre:>3} {self.blu:>3} {self.op:>3.1f}'
    
class RectangleShape:
    """A rectangle shape that can be drawn as an SVG rect element"""
    ccnt: int = 0  # counting number of rectangles being constructed

    @classmethod
    def get_rect_count(cls) -> int:
        """counts the number of rectangles created"""
        return RectangleShape.ccnt

    def __init__(self, x: int, y: int, rad: int, rx: int, ry: int, width: int, height: int, red: int, gre: int, blu: int, op: float) -> None:
        """Initializes a rectangle"""
        self.sha: int = 1
        self.x: int = x
        self.y: int = y
        self.rad: int = rad
        self.rx: int = rx
        self.ry: int = ry
        self.width: int = width
        self.height: int = height
        self.red: int = red
        self.gre: int = gre
        self.blu: int = blu
        self.op: float = op
        RectangleShape.ccnt += 1

    def as_svg(self) -> str:
        """as_svg method: Produces the SVG code representing RectangleShape"""
        return f'<rect x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" ' \
               f'fill="rgb({self.red},{self.gre},{self.blu})" ' \
               f'fill-opacity="{self.op}"></rect>'

    def __str__(self) -> str:
        """str method: String representation of RectangleShape"""
        return f'{self.sha:>3} {self.x:>3} {self.y:>3} {self.rad:>3} {self.rx:>3} {self.ry:>3} {self.width:>3} {self.height:>3} {self.red:>3} {self.gre:>3} {self.blu:>3} {self.op:>3.1f}'

class EllipseShape:
    """An ellipse shape that can be drawn as an SVG ellipse element"""
    ccnt: int = 0  # counting number of ellipses being constructed

    @classmethod
    def get_ellipse_count(cls) -> int:
        """counts the number of ellipses created"""
        return EllipseShape.ccnt

    def __init__(self, x: int, y: int, rad: int, rx: int, ry: int, width: int, height: int, red: int, gre: int, blu: int, op: float) -> None:
        """Initializes an ellipse"""
        self.sha: int = 2
        self.x: int = x
        self.y: int = y
        self.rad: int = rad
        self.rx: int = rx
        self.ry: int = ry
        self.width: int = width
        self.height: int = height
        self.red: int = red
        self.gre: int = gre
        self.blu: int = blu
        self.op: float = op
        EllipseShape.ccnt += 1

    def as_svg(self) -> str:
        """as_svg method: Produces the SVG code representing this shape"""
        return f'<ellipse cx="{self.x}" cy="{self.y}" rx="{self.x}" ry="{self.y}" ' \
               f'fill="rgb({self.red},{self.gre},{self.blu})" ' \
               f'fill-opacity="{self.op}"></ellipse>'

    def __str__(self) -> str:
        """str method: String representation of this shape"""
        return f'{self.sha:>3} {self.x:>3} {self.y:>3} {self.rad:>3} {self.rx:>3} {self.ry:>3} {self.width:>3} {self.height:>3} {self.red:>3} {self.gre:>3} {self.blu:>3} {self.op:>3.1f}'

class SvgCanvas:
    """Generates an SVG file with RandomShapes"""
    TAB: str = "   "  # HTML indentation tab (default: three spaces)

    def __init__(self, file_name: str, win_title: str) -> None:
        """SvgCanvas constructor creates an instance of SvgCanvas when the class is called"""
        self.win_title: str = win_title
        self.__tabs: int = 0
        self.__file: IO = open(file_name, "w")
        self.__write_head()

    def increase_indent(self) -> None:
        """increase_indent method: Increases the number of tab characters used for indentation"""
        self.__tabs += 1

    def decrease_indent(self) -> None:
        """decrease_indent method: Decreases the number of tab characters used for indentation"""
        self.__tabs -= 1

    def append(self, content: str) -> None:
        """append method: Appends the given HTML content to this document"""
        ts: str = HtmlDocument.TAB * self.__tabs
        self.__file.write(f'{ts}{content}\n')

    def __write_head(self) -> None:
        """write_head method: Appends the HTML/SVG preamble to this document"""
        self.append('<html>')
        self.append('<head>')
        self.increase_indent()
        self.append(f'<title>{self.win_title}</title>')
        self.decrease_indent()
        self.append('</head>')
        self.append('<body>')
        self.increase_indent()
        self.append('<svg width="500" height="300">')
        self.increase_indent()
    
    def write_end(self) -> None:
        """write_end method: appends closing of the HTML/SVG file to the current document"""
        self.decrease_indent()
        self.append('</svg>')
        self.decrease_indent()
        self.append('</body>')
        self.append('</html>')

    def genArt(self) -> None:
        """genArt method: creates the CircleShapes and appends them to the HTML file"""
        c1 = CircleShape(50, 50, 50, 255, 0, 0, 1.0)
        self.append(c1.as_svg())
        c2 = CircleShape(150, 50, 50, 255, 0, 0, 1.0)
        self.append(c2.as_svg())
        c3 = CircleShape(250, 50, 50, 255, 0, 0, 1.0)
        self.append(c3.as_svg())
        c4 = CircleShape(350, 50, 50, 255, 0, 0, 1.0)
        self.append(c4.as_svg())
        c5 = CircleShape(450, 50, 50, 255, 0, 0, 1.0)
        self.append(c5.as_svg())
        c6 = CircleShape(50, 250, 50, 0, 0, 255, 1.0)
        self.append(c6.as_svg())
        c7 = CircleShape(150, 250, 50, 0, 0, 255, 1.0)
        self.append(c7.as_svg())
        c8 = CircleShape(250, 250, 50, 0, 0, 255, 1.0)
        self.append(c8.as_svg())
        c9 = CircleShape(350, 250, 50, 0, 0, 255, 1.0)
        self.append(c9.as_svg())
        c10 = CircleShape(450, 250, 50, 0, 0, 255, 1.0)
        self.append(c10.as_svg())

class Table:
    """creates a table with appropriate comments"""
    def __init__(self) -> None:
        self.list = []
        for i in range(10):
            art_config = PyArtConfig()
            shape = RandomShape(art_config)
            self.list.append(shape)
    
    def __str__(self) -> str:
        """str method: String representation of a table object"""
        my_table = f'\nCNT SHA   X   Y RAD  RX  RY   W   H   R   G   B  OP\n'
        for i in range(10):
            my_table += f'{i:>3} {str(self.list[i].create_shape())}\n'
        return my_table

    
class Irange(NamedTuple):
    """A simple integer range with minimum and maximum values"""
    imin: int
    imax: int

    def __str__(self) -> str:
        """str method: String representation"""
        return f'{self.imin},{self.imax}'
    
class Frange(NamedTuple):
    """A simple float range with minimum and maximum values"""
    fmin: float
    fmax: float

    def __str__(self) -> str:
        """str method: String representation"""
        return f'{self.fmin},{self.fmax}'


class PyArtConfig:
    """Input configuration to guide the art to be applied to random shapes; ranges are set at the start of the class"""
    default_sha: Irange = Irange(0, 2)
    default_x: Irange = Irange(0, 500)
    default_y: Irange = Irange(0, 500)
    default_rad: Irange = Irange(0, 100)
    default_rx: Irange = Irange(10, 30)
    default_ry: Irange = Irange(10, 30)
    default_width: Irange = Irange(10, 100)
    default_height: Irange = Irange(10, 100)
    default_red: Irange = Irange(0, 255)
    default_green: Irange = Irange(0, 255)
    default_blue: Irange = Irange(0, 255)
    default_op: Frange = Frange(0.0, 1.0)

    def __init__(self) -> None:
        """PyArtConfig constructor creates an instance of PyArtConfig when the class is called"""
        self.default_sha = rd.randint(self.default_sha.imin, self.default_sha.imax)
        self.default_x = rd.randint(self.default_x.imin, self.default_x.imax)
        self.default_y = rd.randint(self.default_y.imin, self.default_y.imax)
        self.default_rad = rd.randint(self.default_rad.imin, self.default_rad.imax)
        self.default_rx = rd.randint(self.default_rx.imin, self.default_rx.imax)
        self.default_ry = rd.randint(self.default_ry.imin, self.default_ry.imax)
        self.default_width = rd.randint(self.default_width.imin, self.default_width.imax)
        self.default_height = rd.randint(self.default_height.imin, self.default_height.imax)
        self.default_red = rd.randint(self.default_red.imin, self.default_red.imax)
        self.default_green = rd.randint(self.default_green.imin, self.default_green.imax)
        self.default_blue = rd.randint(self.default_blue.imin, self.default_blue.imax)
        self.default_op = rd.uniform(self.default_op.fmin, self.default_op.fmax)
    

class RandomShape:
    """A shape that can take the form of any type of supported shape"""
    def __init__(self, art_config: PyArtConfig):
        """Initializes a RandomShape"""
        self.art_config = art_config

    def __str__(self) -> str:
        """str method: String representation of a RandomShape"""
        return f'Generated Random Shape\n' \
               f'shape = {self.art_config.default_sha}\n' \
               f'(x, y) = ({self.art_config.default_x},{self.art_config.default_y})\n' \
               f'radius = {self.art_config.default_rad}\n' \
               f'(red, green, blue) = ({self.art_config.default_red},{self.art_config.default_green},{self.art_config.default_blue})\n' \
               f'opacity = {self.art_config.default_op}'
    
    def create_shape(self) -> str:
        """create_shape method: checks which shape was randomly generated and then creates an instance of it"""
        if (self.art_config.default_sha == 0):
            circle = CircleShape(self.art_config.default_x, self.art_config.default_y, self.art_config.default_rad, self.art_config.default_rx, self.art_config.default_ry, self.art_config.default_width, self.art_config.default_height, self.art_config.default_red, self.art_config.default_green, self.art_config.default_blue, self.art_config.default_op)
            return circle
        elif (self.art_config.default_sha == 1):
            rect = RectangleShape(self.art_config.default_x, self.art_config.default_y, self.art_config.default_rad, self.art_config.default_rx, self.art_config.default_ry, self.art_config.default_width, self.art_config.default_height, self.art_config.default_red, self.art_config.default_green, self.art_config.default_blue, self.art_config.default_op)
            return rect
        else:
            ellipse = EllipseShape(self.art_config.default_x, self.art_config.default_y, self.art_config.default_rad, self.art_config.default_rx, self.art_config.default_ry, self.art_config.default_width, self.art_config.default_height, self.art_config.default_red, self.art_config.default_green, self.art_config.default_blue, self.art_config.default_op)
            return ellipse
        
    def as_Part2_line(self) -> str:
        """as_Part2_line method: returns a string of the object data in the form of a line of numbers"""
        return str(self.create_shape())
    
    def as_svg(self) -> str:
        """as_svg method: returns a string of the object data in the form of SVG commands"""
        return self.create_shape().as_svg()

            
def main() -> None:
    table = Table()
    print(table)
main()
