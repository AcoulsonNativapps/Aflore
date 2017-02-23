import datetime
import xml.dom.minidom
import hashlib, datetime, email, os, sys, time, traceback
from pysimplesoap.client import SoapClient, SimpleXMLElement
from pysimplesoap.wsse import BinaryTokenSignature
from suds.transport.https import HttpAuthenticated



import logging
logging.basicConfig(level=logging.INFO)
#logging.getLogger('suds.client').setLevel(logging.DEBUG)
#logging.getLogger('suds.transport').setLevel(logging.DEBUG)
#logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)



user = '90681'
password = 'H33std'
WSDL = 'http://cifinpruebas.asobancaria.com/InformacionComercialactWS/services/InformacionComercial?wsdl'
crendials = dict(username=user, password=password)
t = HttpAuthenticated(**crendials)
location='http://cifinpruebas.asobancaria.com/InformacionComercialactWS/services/InformacionComercial'
keyfile='key_nopass.pem'
cert='cert.pem'
headers = {"Content-TYpe" : "text/xml;charset=UTF-8",
           "SOAPAction" : ""}


from suds.client import Client
from suds.wsse import Security, Timestamp
from wsse.suds import WssePlugin

def get_client(our_keyfile_path, our_certfile_path, their_certfile_path):
    wsse = Security()
    wsse.tokens.append(Timestamp())

    return Client(
        WSDL,
        transport=t,
        location=location,
        wsse=wsse,
        headers=headers,
        plugins=[
            WssePlugin(
                keyfile=our_keyfile_path,
                certfile=our_certfile_path,
                their_certfile=their_certfile_path,
            ),
        ],
    )
if __name__ == '__main__':


    client = get_client(keyfile,cert,cert)

    parametrosConsulta = client.factory.create('{http://dto.infocomercial.cifin.asobancaria.com}ParametrosConsultaDTO')

    parametrosConsulta.codigoInformacion = '154'
    parametrosConsulta.motivoConsulta = '24'
    parametrosConsulta.numeroIdentificacion = '1143356938'
    parametrosConsulta.tipoIdentificacion = '1'
    print client.service.consultaXml(parametrosConsulta)
