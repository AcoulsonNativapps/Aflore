from suds.client import Client
from suds.transport.https import HttpAuthenticated
from suds.wsse import  Security
from suds.wsse import Timestamp


WSUNS = \
    ('wsu',
     'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd')

user = '90681'
password = 'H33std'
url = 'http://cifinpruebas.asobancaria.com/InformacionComercialactWS/services/InformacionComercial?wsdl'

crendials = dict(username=user, password=password)
t = HttpAuthenticated(**crendials)
client = Client(url=url, transport=t)
print client
parametrosConsulta = client.factory.create('{http://dto.infocomercial.cifin.asobancaria.com}ParametrosConsultaDTO')

parametrosConsulta.codigoInformacion = '154'
parametrosConsulta.motivoConsulta = '24'
parametrosConsulta.numeroIdentificacion = '1143356938'
parametrosConsulta.tipoIdentificacion ='1'

#print parametrosConsulta

list_of_methods = [method for method in client.wsdl.services[0].ports[0].methods]
method = client.wsdl.services[0].ports[0].methods[list_of_methods[0]]

#print list_of_methods
#print method.binding.input.param_defs(method)


import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)
logging.getLogger('suds.xsd.schema').setLevel(logging.DEBUG)
logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)

# res = client.service.consultaXml(parametrosConsulta)
# print res


