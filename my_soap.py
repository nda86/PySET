from zeep import Client
import my_config as cfg

def soap_cards(base64_xml):
	client = Client(cfg.wsdl_cards)
	client.service.getCardsCatalog("cardsCatalogXML", base64_xml)