import base64

def parse_cards(path):
	out = ""
	with open(path, "r") as oldfile:
		lines = oldfile.readlines()
		for line in lines:
			out = out + line.replace("percentage-discount", "ololo").replace("Client", "client")
	out64 = base64.b64encode(out)
	return out64