#!/usr/bin/env python
import random as rd
from enum import Enum
from typing import IO, List, NamedTuple


class HtmlDocument:
    """An HTML document that allows appending SVG content"""
    TAB: str = "   "  # HTML indentation tab (default: three spaces)

    def __init__(self, file_name: str, win_title: str) -> None:
        """
        HtmlDocument constructor creates an instance of HtmlDocument when the class is called
        Parameters
        ----------
            self: HtmlDocument (refers to the instance of the class being operated on)
            file_name: str
            win_title: str

        Returns
        -------
            None
        """
        self.win_title: str = win_title
        self.__tabs: int = 0
        self.__file: IO = open(file_name, "w")
        self.__write_head()

    def increase_indent(self) -> None:
        """
        increase_indent method increases the number of tab characters used for indentation
        Parameters
        ----------
            self: HtmlDocument (refers to the instance of the class being operated on)
            
        Returns
        -------
            None
        """
        self.__tabs += 1

    def decrease_indent(self) -> None:
        """
        decrease_indent method decreases the number of tab characters used for indentation
        Parameters
        ----------
            self: HtmlDocument (refers to the instance of the class being operated on)
            
        Returns
        -------
            None
        """
        self.__tabs -= 1

    def append(self, content: str) -> None:
        """
        append method appends the given HTML content to the current document
        Parameters
        ----------
            self: HtmlDocument (refers to the instance of the class being operated on)
            content: str
            
        Returns
        -------
            None
        """
        ts: str = HtmlDocument.TAB * self.__tabs
        self.__file.write(f'{ts}{content}\n')

    def __write_head(self) -> None:
        """
        write_head method appends the HTML preamble to the current document
        Parameters
        ----------
            self: HtmlDocument (refers to the instance of the class being operated on)
            
        Returns
        -------
            None
        """
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

    def __init__(self, ctx: int, cty: int, rad: int, red: int, gre: int, blu: int, op: float) -> None:
        """
        CircleShape constructor creates an instance of CircleShape when the class is called
        Parameters
        ----------
            self: CircleShape (refers to the instance of the class being operated on)
            ctx: int
            cty: int
            rad: int
            red: int
            gre: int
            blu: int
            op: float

        Returns
        -------
            None
        """
        self.sha: int = 0
        self.ctx: int = ctx
        self.cty: int = cty
        self.rad: int = rad
        self.red: int = red
        self.gre: int = gre
        self.blu: int = blu
        self.op: float = op
        CircleShape.ccnt += 1

    def as_svg(self) -> str:
        """
        as_svg method produces the SVG code representing the CircleShape
        Parameters
        ----------
            self: CircleShape (refers to the instance of the class being operated on)

        Returns
        -------
            str: this SVG code is returned in the form of a string
        """
        return f'<circle cx="{self.ctx}" cy="{self.cty}" r="{self.rad}" ' \
               f'fill="rgb({self.red},{self.gre},{self.blu})" ' \
               f'fill-opacity="{self.op}"></circle>'

    def __str__(self) -> str:
        """
        str method customizes the string representation of this shape
        Parameters
        ----------
            self: CircleShape (refers to the instance of the class being operated on)

        Returns
        -------
            str: string representation of a CircleShape
        """
        return f'\nGenerated random circle\n' \
               f'shape = {self.sha}\n' \
               f'radius = {self.rad}\n' \
               f'(centerx, centery) = ({self.ctx},{self.cty})\n' \
               f'(red, green, blue) = ({self.red},{self.gre},{self.blu})\n' \
               f'opacity = {self.op:.1f}\n'


class SvgCanvas:
    """Generates an SVG file with CircleShapes"""
    TAB: str = "   "  # HTML indentation tab (default: three spaces)

    def __init__(self, file_name: str, win_title: str) -> None:
        """
        SvgCanvas constructor creates an instance of SvgCanvas when the class is called
        Parameters
        ----------
            self: CircleShape (refers to the instance of the class being operated on)
            file_name: str
            win_title: str

        Returns
        -------
            None
        """
        self.win_title: str = win_title
        self.__tabs: int = 0
        self.__file: IO = open(file_name, "w")
        self.__write_head()

    def increase_indent(self) -> None:
        """
        increase_indent method increases the number of tab characters used for indentation
        Parameters
        ----------
            self: SvgCanvas (refers to the instance of the class being operated on)
            
        Returns
        -------
            None
        """
        self.__tabs += 1

    def decrease_indent(self) -> None:
        """
        decrease_indent method decreases the number of tab characters used for indentation
        Parameters
        ----------
            self: SvgCanvas (refers to the instance of the class being operated on)
            
        Returns
        -------
            None
        """
        self.__tabs -= 1


    def append(self, content: str) -> None:
        """
        append method appends the given HTML content to the current document
        Parameters
        ----------
            self: SvgCanvas (refers to the instance of the class being operated on)
            content: str
            
        Returns
        -------
            None
        """
        ts: str = HtmlDocument.TAB * self.__tabs
        self.__file.write(f'{ts}{content}\n')

    def __write_head(self) -> None:
        """
        write_head method appends the HTML/SVG preamble to the current document
        Parameters
        ----------
            self: SvgCanvas (refers to the instance of the class being operated on)
            
        Returns
        -------
            None
        """
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
        """
        write_end method appends closing of the HTML/SVG file to the current document
        Parameters
        ----------
            self: SvgCanvas (refers to the instance of the class being operated on)
            
        Returns
        -------
            None
        """
        self.decrease_indent()
        self.append('</svg>')
        self.decrease_indent()
        self.append('</body>')
        self.append('</html>')

    def genArt(self) -> None:
        """
        genArt method creates the CircleShapes and appends them to the HTML file
        Parameters
        ----------
            self: SvgCanvas (refers to the instance of the class being operated on)
            
        Returns
        -------
            None
        """
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


def main() -> None:
    fnam: str = "a41.html"
    with open(fnam, "w") as f:
        canvas = SvgCanvas(fnam, "My Art")
        canvas.genArt()
        canvas.write_end()
main()
