import csv
from xml.dom.minidom import Document, DOMImplementation


def prepare_xml(csv_data):
    imp = DOMImplementation()
    doctype = imp.createDocumentType("concept", "-//OASIS//DTD DITA Concept//EN", "concept.dtd")
    doc = Document()
    doc.appendChild(doctype)

    concept = doc.createElement("concept")
    concept.setAttribute("base", "pdm-category(Platforms) pdm-subcategory(Platform Products) pdm-product(DX 200 SW Platform) keys(ref_errormsg)")
    concept.setAttribute("id", "error_list")

    title = doc.createElement("title")
    title_text = doc.createTextNode("Error messages list")
    title.appendChild(title_text)
    concept.appendChild(title)

    shortdesc = doc.createElement("shortdesc")
    shortdesc_text = doc.createTextNode("This section lists all the error messages.")
    shortdesc.appendChild(shortdesc_text)
    concept.appendChild(shortdesc)

    conbody = doc.createElement("conbody")
    section = doc.createElement("section")
    p = doc.createElement("p")
    dl = doc.createElement("dl")

    for column in csv_data:
         xml_entry = f'<dlentry><dt>{column[3]}</dt><dd><p>{column[4]}</p><p>{column[1]}</p></dd></dlentry>'
         dl.appendChild(doc.createTextNode(xml_entry))


    p.appendChild(dl)
    section.appendChild(p)
    conbody.appendChild(section)
    concept.appendChild(conbody)
    doc.appendChild(concept)
    
    xml_string = doc.toprettyxml(encoding="UTF-8").decode("utf-8")

    xml_string = xml_string.replace("&lt;", "<")
    xml_string = xml_string.replace("&lt;=", "<=")
    xml_string = xml_string.replace("&gt;", ">")
    xml_string = xml_string.replace("&amp", "&")
    
    return xml_string


def write_xml(xml_string, output_file):
    with open(output_file, "w", encoding="UTF-8") as f:
        f.write(xml_string)

        
def main():
    # Enter the CSV file's name
    csv_file_name = input("Enter the name of the CSV file: ")

    # Reading the CSV data
    with open(csv_file_name, "r", encoding="UTF-8") as csvfile:
        csv_data = list(csv.reader(csvfile, delimiter=";"))
        csv_data = csv_data[1:]

    # This rows prepare XML for each row
    xml_string = prepare_xml(csv_data)

    # Write the XML string to a file
    output_file = "error_list.xml"
    write_xml(xml_string, output_file)

if __name__ == "__main__":
    main()
