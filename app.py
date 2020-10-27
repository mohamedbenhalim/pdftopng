import fitz
import PyPDF2


import os

rootdir = 'C:/dev/pdftopng/docs/'
writer = PyPDF2.PdfFileWriter()


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print (os.path.join(subdir, file))

        pdffile = os.path.join(subdir, file)
        doc = fitz.open(pdffile)
        page = doc.loadPage(0)  # number of page
        pix = page.getPixmap()
        output = file+".png"
        pix.writePNG(output)
        reader = PyPDF2.PdfFileReader(pdffile)
        for i in range(reader.numPages):
            page = reader.getPage(i)
            page.compressContentStreams()
            writer.addPage(page)

        with open('test_out2.pdf', 'wb') as f:
            writer.write(f)



