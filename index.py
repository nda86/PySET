import sys
import my_parse
import my_soap

def import_cards(path):
	base64_xml = my_parse.parse_cards(path)
	my_soap.soap_cards(base64_xml)

def import_goods(path):
	base64_xml = my_parse.parse_goods(path)
	my_soap.soap_goods(base64_xml)

if __name__ == "__main__":
	path = sys.argv[2]
	if (sys.argv[1] == "c"):
		import_cards(path)
	if (sys.argv[1] == "g"):
		import_goods(path)

		