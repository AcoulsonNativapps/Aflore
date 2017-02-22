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



client = Client(
 url,
    transport=Transport(session=session),
    wsse=Signature(
    'aflore.key', 'key_nopass.pem',
    'pwd123'))

print client.wsdl.dump()

parametroCon = client.get_type('ns0:ParametrosConsultaDTO')
strin = client.get_type('ns1:string')
codigoInformacion = strin('154')
motivoConsulta = strin('24')
numeroIdentificacion = strin('1143356938')
tipoIdentificacion = strin('1')


print client.service.__getattr__('consultaXml')(parametrosConsulta=parametroCon(codigoInformacion=codigoInformacion,
                                                             motivoConsulta=motivoConsulta,
                                                             numeroIdentificacion=numeroIdentificacion,
                                                             tipoIdentificacion=tipoIdentificacion))