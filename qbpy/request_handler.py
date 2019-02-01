import base64

from lxml import etree as xml
from .configuration import CONFIGURATION
from .exceptions import QuickBaseException

class _RequestHandler:
    """
    Build API calls to send to Quick Base.

    Converts the parameters provided to the API method and creates a Quick Base
    compliant request payload. This allows the abstraction of complex and
    inconvenient API parameters into an easier user interface.

    Headers are added only when the request needs to have a set of custom headers
    When headers are not required, the attribute is set to None.

    :param action: The Quick Base API method being called
    :type action: string

    :param parameters: A dictionary containing parameters to be used with the
        API call; this dictionary is merged with the defaults
    :type parameters: dictionary

    :return: A response returned by the Quick Base API
    :rtype: response object
    """
    def __init__(self, action, parameters):
        self.action = action
        self.allowable_parameters = CONFIGURATION[action]['allowable_parameters']
        self.method = CONFIGURATION[action]['method']
        self.parameters = parameters
        self.scope = CONFIGURATION[action]['scope']
        self.xml = CONFIGURATION[action]['xml']

    def __repr__(self):
        return 'RequestHandler ({0}) at {1}'.format(self.action, hex(id(self)))

    @property
    def headers(self):
        """
        Creates headers for XML requests.
        """
        if self.xml:
            if self.action == 'API_UploadFile':
                action = self.parameters['action']
            else:
                action = self.action

            return {
                'Content-Type': 'application/xml',
                'QUICKBASE-ACTION': action,
            }
        return None

    @property
    def payload(self):
        """
        Build a payload object.

        Converts parameters into a format which can be used by the requests
        library in order to generate a payload to send to Quick Base.

        :return: A payload formatted for use by the requests library
        :rtype: dictionary
        """
        def convert_fields(payload):
            """
            Alter payload to handle fid identifiers.

            Alters the payload. When field(s) are included in the payload, the
            keys and values are converted to _fid_N format, and the original
            fields payload is removed.

            :param payload: An existing payload
            :type payload: dictionary

            :return: A modified payload, with fields surfaced in fid format
            :rtype: dictionary
            """
            if 'field' in payload:
                for fid in payload['field'].items():
                    payload['_fid_' + fid[0]] = fid[1]
                del payload['field']

            if 'fields' in payload:
                for fid in payload['fields'].items():
                    payload['_fid_' + fid[0]] = fid[1]
                del payload['fields']

            return payload

        def create_xml(payload):
            """
            Convert payload into XML.

            :param payload: An existing payload
            :type payload: dictionary

            :return: A modified payload, with the payload converted to XML
            :rtype: string
            """
            qdbapi = xml.Element('qdbapi')

            # add generic parameters to xml payload
            for parameter in payload:
                if parameter not in ['field', 'pagebody', 'records_csv']:
                    xml.SubElement(qdbapi, parameter).text = str(payload[parameter])
                elif parameter == 'field':
                    for fid in payload[parameter]:
                        tag = xml.SubElement(qdbapi, 'field')
                        if fid == 'rid':
                            tag.attrib['fid'] = str(fid)
                        else:
                            tag.attrib['fid'] = str(fid)

                        content = payload[parameter][fid]
                        if isinstance(content, dict):
                            tag.attrib['filename'] = content['filename']
                            tag.text = base64.b64encode(content['file'])
                        else:
                            tag.text = str(content)
                else:
                    try:
                        xml.SubElement(qdbapi, parameter).text = xml.CDATA(payload[parameter])
                    except TypeError:
                        raise QuickBaseException({
                            'errcode': -2,
                            'errtext': 'Empty payload',
                            'errdetail': 'CDATA payload objects cannot be None',
                        })

            return xml.tostring(qdbapi).decode()

        # lowercase all payload parameters
        self.parameters = {key.lower(): value for key, value in self.parameters.items()}

        # filter payload to only allowable parameters
        payload = {
            key : value
            for (key, value)
            in self.parameters.items()
            if key in self.allowable_parameters
        }

        if self.xml:
            return create_xml(payload)
        return convert_fields(payload)

    def send_request(self):
        """
        Send request to Quick Base.

        Sends request to Quick Base, combining the url, payload, and headers
        to deliver an API call to Quick Base for processing.
        """
        return self.method(self.url, self.payload, headers=self.headers)

    @property
    def url(self):
        """
        Generate url for API call.

        Generates the url to use in API calls. Differentiates between the
        URL required for XML calls and those sent via url alternative.
        """
        url = 'https://{realm}.{domain}/db/{dbid}'
        # requests sent via URL receive an API call argument
        if not self.xml:
            url += '?a={action}'

        return url.format(
            realm=self.parameters['realm'],
            domain=self.parameters['domain'],
            dbid='main' if self.scope == 'realm' else self.parameters['dbid'],
            action=self.action)
