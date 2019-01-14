import pytest
from unittest import mock
from qbpy.response_handler import _ResponseHandler
from qbpy.exceptions import RequestException, QuickBaseException

def mocked_request(*args, **kwargs):
    class MockResponse:
        def __init__(self, xml, status_code):
            self.xml = xml
            self.status_code = status_code
        @property
        def text(self):
            return self.xml
    if args[0] == 'API_GetNumRecords':
        return MockResponse(
            '''<?xml version="1.0" ?>
               <qdbapi>
                   <action>API_GetNumRecords</action>
                   <errcode>0</errcode>
                   <errtext>No error</errtext>
                   <num_records>17</num_records>
               </qdbapi>
               ''', 200)
    elif args[0] == 'RequestException':
        return MockResponse(None, 404)
    elif args[0] == 'QuickBaseException':
        return MockResponse(
            '''<?xml version="1.0" ?>
               <qdbapi>
                   <action>API_GetNumRecords</action>
                   <errcode>2</errcode>
                   <errtext>Invalid Input</errtext>
                   <errdetail>You did not specify a name for the new application.</errdetail>
               </qdbapi>
               ''', 200)
    elif args[0] == 'RootStructureError':
        return MockResponse(
            '''<?xml version="1.0" ?>
               <other>
                   <action>API_GetNumRecords</action>
                   <errcode>1</errcode>
                   <errtext>Unknown error</errtext>
                   <errdetail>You did not specify a name for the new application.</errdetail>
               </other>
               ''', 200)


class TestResponseHandler:
    def test_repr(self):
        """Test object representation"""
        rh = _ResponseHandler(action='API_GetNumRecords', response=mocked_request('API_GetNumRecords'))
        assert repr(rh) == 'ResponseHandler ({0}) at {1}'.format('API_GetNumRecords', hex(id(rh)))

    def test_property_action(self):
        """Action property returns the action  parameter from the response"""
        rh = _ResponseHandler(action='API_GetNumRecords', response=mocked_request('API_GetNumRecords'))
        assert rh.action == 'API_GetNumRecords'

    def test_property_error(self):
        """Error property returns (errcode, errtext) tuple"""
        rh = _ResponseHandler(action='API_GetNumRecords', response=mocked_request('API_GetNumRecords'))
        assert rh.error == {
            'errcode': 0,
            'errtext': 'No error',
            'errdetail': None
        }

    # ERROR HANDLING ##########################################################
    def test_api_unreachable(self):
        """
        Raises a RequestException when the API returns status code other than 200
        """
        with pytest.raises(RequestException):
            _ResponseHandler(action='API_GetNumRecords', response=mocked_request('RequestException'))

    def test_api_error(self):
        """
        Raises a QuickBaseException when the API returns a valid status code,
        and a non-zero errcode indicating a problem with the request
        """
        with pytest.raises(QuickBaseException):
            _ResponseHandler(action='API_GetNumRecords', response=mocked_request('QuickBaseException'))

    @pytest.mark.parametrize('mocked_request', [
        mocked_request('RootStructureError'),
    ])
    def test_api_structure_error(self, mocked_request):
        """
        Raises a QuickBaseException when the API returns an invalid structure
        which would cause an immediate parsing failure
        """
        with pytest.raises(QuickBaseException):
            _ResponseHandler(action='API_GetNumRecords', response=mocked_request)
