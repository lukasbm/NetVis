from pylatex import Document, TikZ, Axis, Plot, TikZCoordinate, TikZDraw, TikZNode, TikZNodeAnchor

if __name__ == '__main__':
    doc = Document(documentclass="standalone", document_options=["border=10pt", "multi", "tikz"])

    with doc.create(TikZ()):
        doc.append()


    doc.generate_pdf('full', clean_tex=False, clean=True)
