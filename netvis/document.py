from pylatex import Document, Package, UnsafeCommand

from utils import colors, to_camel_case


class NetVisDocument(Document):
    def __init__(self, border: int = 10):
        """
        set the document up.

        :param border: border radius of the document in pt
        """
        super().__init__(documentclass="standalone", document_options=[f"border={border}pt", "multi", "tikz"])

        self.preamble.append(Package("./netvis"))

        # go over all colors and add them to the preamble
        for color_name, rgb in colors.items():
            rgb_command = UnsafeCommand("newcommand", f"\\{to_camel_case(color_name)}Color",
                                        extra_arguments=rgb.dumps())
            self.preamble.append(rgb_command)
