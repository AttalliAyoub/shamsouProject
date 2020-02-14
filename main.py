from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table

pdfFileName = 'Beaver.pdf'

pfdName = 'Beaver'

Title = 'Beavers'

image = 'American_Beaver.jpg'


def rolerY():
    pdf.drawString(0, 100, 'y100')
    pdf.drawString(0, 200, 'y200')
    pdf.drawString(0, 300, 'y300')
    pdf.drawString(0, 400, 'y400')
    pdf.drawString(0, 500, 'y500')
    pdf.drawString(0, 600, 'y600')
    pdf.drawString(0, 700, 'y700')
    pdf.drawString(0, 800, 'y800')


def rolerx():
    pdf.drawString(100, 0, 'X100')
    pdf.drawString(200, 0, 'X200')
    pdf.drawString(300, 0, 'X300')
    pdf.drawString(400, 0, 'X400')
    pdf.drawString(500, 0, 'X500')
    pdf.drawString(600, 0, 'X600')
    pdf.drawString(700, 0, 'X700')
    pdf.drawString(800, 0, 'X800')
    pdf.drawString(900, 0, 'X900')


artical = [
    'The beaver (genus Castor) is a large, primarily nocturnal, semiaquatic rodent. Castor includes two extant species, the North American',
    'beaver (Castor canadensis) (native to North America) and Eurasian beaver (Castor fiber) (Eurasia).[1] Beavers are known for building dams,',
    'canals, and lodges (homes). They are the second-largest rodent in the world (after the capybara). Their colonies create one or more dams to provide still,',
    'deep water to protect against predators, and to float food and building material. The North American beaver population was once more than 60 million,\
    but as of 1988 was 6–12 million. This population decline is the result of extensive hunting for fur, for glands used as medicine and perfume, and because the beavers" harvesting of trees and flooding of waterways may interfere with other land uses.',
]

tableTitle = 'Beaver Statistics Index'

dataset = [
    [2008,	3, 491,	223],
    [2009,	4, 842,	249],
    [2010,	3, 686,	296],
    [2011,	4, 102,	161],
    [2012,	5, 161,	200],
    [2013,	5, 620,	222],
    [2014,	5, 124,	199],
    [2015,	3, 727,	201],
    [2016,	2, 657,	213],
    [2017,	2, 145,	302],
    [2018,	2, 379,	352],
]

pdf = canvas.Canvas(
    pdfFileName,
    pagesize=A4
    )
# pdf = SimpleDocTemplate(
#     pdfFileName,
#     pagesize=A4
# )

pdf.setTitle(pfdName)
rolerx()
rolerY()
pdf.setFont('Times-Bold', 26)
pdf.drawCentredString(300, 800, Title)
pdf.setFillColorRGB(0, 0, 255)
pdf.drawCentredString(300,  700, 'Artical about beavers')

pdf.line(24,  680, 500, 680)

text = pdf.beginText(24, 660)
text.setFillColorRGB(255, 0, 0)
text.setFont('Helvetica-Bold', 16)
for line in artical:
    text.textLine(line)

pdf.drawText(text)

pdf.drawInlineImage(image, 250, 300, 300, 300)

beverTable = Table(dataset)

beverTable.wrapOn(pdf, 200, 500)
beverTable.drawOn(pdf, 100, 300)

pdf.save()
