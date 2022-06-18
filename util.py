from fpdf import FPDF

def CutTextInPages(text):
    text = text.split()
    n = 250
    return [' '.join(text[i:i + n]) for i in range(0, len(text), n)]
class PDF(FPDF):
    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Select Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Print centered page number
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')



class Book:
    def __init__(self, title=None):
        self.title=title
        self.chapters={}
    def AddChapter(self,pages,title):
        self.chapters[title]=pages

    def RenderChapters(self):

        for i in self.chapters:
            pdf = PDF()
            pdf.set_top_margin(40)
            pdf.set_right_margin(10)
            pdf.set_left_margin(10)
            for j in self.chapters[i]:
                pdf.add_page()

                pdf.set_font("Arial", size=15)

                pdf.multi_cell(180, 10, txt=j,align='C')
            pdf.output(f"{i}.pdf")



