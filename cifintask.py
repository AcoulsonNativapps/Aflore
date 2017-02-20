from suds.client import Client
from suds.transport.https import HttpAuthenticated


user = '90681'
password = 'H33std'
url = 'http://cifinpruebas.asobancaria.com/InformacionComercialactWS/services/InformacionComercial?wsdl'

crendials = dict(username=user, password=password)
t = HttpAuthenticated(**crendials)
client = Client(url=url, transport=t)
#print client
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

#res = client.service.consultaXml(parametrosConsulta)
#print res


