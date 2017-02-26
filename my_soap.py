from zeep import Client
import my_config as cfg

def soap_cards(base64_xml):
	client = Client(cfg.wsdl_cards)
	print client.service.getCardsCatalog(base64_xml)

def soap_goods(base64_xml):
	client = Client(cfg.wsdl_goods)
	print client.service.getGoodsCatalog(base64_xml)