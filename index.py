import sys
import os
import my_parse
import my_soap

def import_cards(path):
	base64_xml = my_parse.parse_cards(path)
	print my_soap.soap_cards(base64_xml)

if __name__ == "__main__":
	path = sys.argv[1]
	import_cards(path)