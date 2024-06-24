from pylatex import TikZ, NoEscape

from document import NetVisDocument

if __name__ == '__main__':
    doc = NetVisDocument()

    with doc.create(TikZ()):
        doc.append(NoEscape(r"""
        \pic[shift={(0,0,0)}] at (0,0,0) {Box={name=crp1,caption=SoftmaxLoss: $E_\mathcal{S}$ ,%
                fill={rgb:blue,1.5;red,3.5;green,3.5;white,5},opacity=0.5,height=20,width=7,depth=20}};
                """))

    # doc.generate_tex("full")
    doc.generate_pdf('test', clean_tex=False, clean=True)
