import pylatex.tikz
from pylatex import Document, Package


pylatex.tikz.TikZNode

class NetVisDocument(Document):
    def __init__(self, border: int = 10):
        """
        set the document up.

        :param border: border radius of the document in pt
        """
        super().__init__(documentclass="standalone", document_options=[f"border={border}pt", "multi", "tikz"])

        self.preamble.append(Package("./netvis"))

    # TODO: method for adding layers!

