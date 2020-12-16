import xml.sax
from xml.dom import minidom



class BikeHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.name = ""
        self.number = ""
        self.type = ""
        self.brand = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "bike":
            print("BIKE")
            type = attributes["type"]
            print("Type: ", type)

    def endElement(self, tag):
        if self.CurrentData == "name":
            print("Name: ", self.name)
        elif self.CurrentData == "number":
            print("Number: ", self.number)
        elif self.CurrentData == "brand":
            print("Brand: ", self.brand)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "name":
            self.name = content
        elif self.CurrentData == "number":
            self.number = content
        elif self.CurrentData == "brand":
            self.brand = content


sax = BikeHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(sax)
parser.parse("bikes.xml")


bikes = minidom.parse("bikes.xml")
types = bikes.getElementsByTagName("bike")
for type in types:
    type.getElementsByTagName("number")[0].childNodes[0].data = 10

with open("bikes_update.xml", 'w+') as file:
    file.write(bikes.toxml())

