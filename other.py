import datetime
import xml.dom.minidom
import hashlib, datetime, email, os, sys, time, traceback
from pysimplesoap.client import SoapClient, SimpleXMLElement
from pysimplesoap.wsse import BinaryTokenSignature




user = '90681'
password = 'H33std'
WSDL = 'http://cifinpruebas.asobancaria.com/InformacionComercialactWS/services/InformacionComercial?wsdl'
crendials = dict(username=user, password=password)


CERT = "aflore.crt"
PRIVATEKEY = "aflore.key"
PASSPHRASE = "pwd123"
import urllib2 as u2
from suds.client import Client
from suds.transport.http import HttpTransport, Reply, TransportError
import httplib

class HTTPSClientAuthHandler(u2.HTTPSHandler):
    def __init__(self, key, cert):
        u2.HTTPSHandler.__init__(self)
        self.key = key
        self.cert = cert

    def https_open(self, req):
        # Rather than pass in a reference to a connection class, we pass in
        # a reference to a function which, for all intents and purposes,
        # will behave as a constructor
        return self.do_open(self.getConnection, req)

    def getConnection(self, host, timeout=300):
        return httplib.HTTPSConnection(host, key_file=self.key,
                                       cert_file=self.cert)

class HTTPSClientCertTransport(HttpTransport):
    def __init__(self, key, cert, proxy_settings=None, *args, **kwargs):
        HttpTransport.__init__(self, *args, **kwargs)
        self.key = key
        self.cert = cert
        self.proxy_settings = proxy_settings

    def u2open(self, u2request):
        """
        Open a connection.
        @param u2request: A urllib2 request.
        @type u2request: urllib2.Requet.
        @return: The opened file-like urllib2 object.
        @rtype: fp
        """
        tm = self.options.timeout

        https_client_auth_handler = HTTPSClientAuthHandler(self.key,
                                                           self.cert)

        # Add a proxy handler if the proxy settings is specified.
        # Otherwise, just use the HTTPSClientAuthHandler.
        if self.proxy_settings:
            proxy_handler = u2.ProxyHandler(self.proxy_settings)
            url = u2.build_opener(proxy_handler, https_client_auth_handler)
        else:
            url = u2.build_opener(https_client_auth_handler)

        url = u2.build_opener()

        if self.u2ver() < 2.6:
            socket.setdefaulttimeout(tm)
            return url.open(u2request)
        else:
            return url.open(u2request, timeout=tm)

# Test #
if __name__ == '__main__':
    key= 'key_nopass.pem'
    cert = 'key.pem'
    proxy_settings = {'https': 'http://90681:H33std@http://cifinpruebas.asobancaria.com:80'}
    transport = HTTPSClientCertTransport(key, cert, proxy_settings)


    client = Client(WSDL, transport=transport)
    parametrosConsulta = client.factory.create('{http://dto.infocomercial.cifin.asobancaria.com}ParametrosConsultaDTO')

    parametrosConsulta.codigoInformacion = '154'
    parametrosConsulta.motivoConsulta = '24'
    parametrosConsulta.numeroIdentificacion = '1143356938'
    parametrosConsulta.tipoIdentificacion = '1'
    print client
    method = getattr(client.service, 'consultaXml')
    print method(parametrosConsulta)
