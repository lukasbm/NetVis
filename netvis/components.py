from pylatex import TikZNode


class Box(TikZNode):
    def __init__(
            self,
            name: str,
            caption: str,
            fill: str,
            opacity: float,
            height: int,
            width: int,
            depth: int
    ):
        """
        Create a box with the given parameters.

        :param name: name of the box
        :param caption: caption of the box
        :param fill: fill color of the box
        :param opacity: opacity of the box
        :param height: height of the box
        :param width: width of the box
        :param depth: depth of the box
        """
        super().__init__(name, caption, options=[
            f"fill={fill}",
            f"opacity={opacity}",
            f"height={height}",
            f"width={width}",
            f"depth={depth}"
        ])

if __name__ == "__main__":
    print(Box(name="hi", caption="test").dumps())
