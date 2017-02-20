from zeep import Client
from zeep.wsse.signature import Signature
from zeep.transports import Transport
from requests.auth import HTTPBasicAuth
from requests import Session


user = '90681'
password = 'H33std'
url = 'http://cifinpruebas.asobancaria.com/InformacionComercialactWS/services/InformacionComercial?wsdl'
crendials = dict(username=user, password=password)
session = Session()
session.auth = HTTPBasicAuth(user, password)

from SOAPpy import WSDL
from SOAPpy import URLopener

SOAPpy.Config.SSL.cert_file = 'cert_file'
SOAPpy.Config.SSL.key_file = 'key_file'
url1 = URLopener.URLopener(username=user,passwd=password)
server=WSDL.Proxy(url1.open(url))

print server.methods.keys()