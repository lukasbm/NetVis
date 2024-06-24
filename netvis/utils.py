from typing import Optional

from pylatex.base_classes import Arguments


class RGB(Arguments):
    def __init__(self,
                 red: Optional[float] = None,
                 green: Optional[float] = None,
                 blue: Optional[float] = None,
                 white: Optional[float] = None,
                 magenta: Optional[float] = None,
                 yellow: Optional[float] = None,
                 cyan: Optional[float] = None,
                 black: Optional[float] = None,
                 ):
        """
        Create an RGB color.

        :param red: red value
        :param green: green value
        :param blue: blue value
        """
        res = "rgb:"
        if red is not None:
            res += f"red,{red};"
        if green is not None:
            res += f"green,{green};"
        if blue is not None:
            res += f"blue,{blue};"
        if white is not None:
            res += f"white,{white};"
        if magenta is not None:
            res += f"magenta,{magenta};"
        if yellow is not None:
            res += f"yellow,{yellow};"
        if cyan is not None:
            res += f"cyan,{cyan};"
        if black is not None:
            res += f"black,{black};"

        if res.endswith("rgb:"):  # nothing specified
            raise ValueError("No color specified")

        if res.endswith(";"):  # remove trailing ;
            res = res[:-1]

        super().__init__(res)


def to_camel_case(snake_str):
    return "".join(x.capitalize() for x in snake_str.lower().split("_"))


# some predefined default colors
colors = {
    "conv": RGB(yellow=5, red=2.5, white=5),
    "conv_relu": RGB(yellow=5, red=5, white=5),
    "pool": RGB(red=1, black=0.3),
    "upsample": RGB(green=5, red=5, white=5),
    "detect": RGB(red=5, white=2),
    "unpool": RGB(blue=2, green=1, black=0.3),
    "fc": RGB(blue=5, red=2.5, white=5),
    "fc_relu": RGB(blue=5, red=5, white=4),
    "softmax": RGB(magenta=5, black=7),
    "sum": RGB(green=1),
    "shortcut": RGB(blue=3, green=1, white=5),
    "mult": RGB(magenta=1),
    "conc": RGB(red=5),
    "edge": RGB(blue=4, red=1, green=4, black=3)
}

if __name__ == "__main__":
    print(colors["conv"].dumps())
