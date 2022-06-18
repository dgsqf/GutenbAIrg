from fpdf import FPDF

def CutTextInPages(text):
    text = text.split()
    n = 200
    return [' '.join(text[i:i + n]) for i in range(0, len(text), n)]


class Book:
    def __init__(self, title=None):
        self.title=title
        self.chapters={}
    def AddChapter(self,pages,title):
        self.chapters[title]=pages

