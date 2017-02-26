import base64

def parse_cards(path):
	out = ""
	with open(path, "r") as oldfile:
		lines = oldfile.readlines()
		for line in lines:
			out = out + line.replace("discount-percent","percentage-discount").replace("Client", "client")
	out64 = base64.b64encode(out)
	return out64

def parse_goods(path):
	out = ""
	with open(path, "r") as oldfile:
		lines = oldfile.readlines()
		for line in lines:
			out = out + line.replace('type="MAX_DISCOUNT_PERCENT" value="100.00"', 'type="MAX_DISCOUNT_PERCENT" value="0.0"').replace('<delete-from-cash>true</delete-from-cash>', '<delete-from-cash>false</delete-from-cash>')
	out64 = base64.b64encode(out)
	return out64