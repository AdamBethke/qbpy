import pytest
from qbpy import QuickBase

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
                   <errcode>1</errcode>
                   <errtext>Unknown error</errtext>
               </qdbapi>
               ''', 200)
    elif args[0] == 'RootStructureError':
        return MockResponse(
            '''<?xml version="1.0" ?>
               <other>
                   <action>API_GetNumRecords</action>
                   <errcode>1</errcode>
                   <errtext>Unknown error</errtext>
               </other>
               ''', 200)

class TestQuickBaseparameters:
    def test_repr(self):
        """Test object representation"""
        qb = QuickBase({})
        assert repr(qb) == 'QuickBase Connection (www) at {0}'.format(hex(id(qb)))

    def test_property_action(self):
        """Action property returns _last_action"""
        qb = QuickBase({})
        qb._last_action = '_last_action'
        assert qb.action == '_last_action'

    def test_property_response(self):
        """Response property returns _last_response"""
        qb = QuickBase({})
        qb._last_response = '_last_response'
        assert qb.response == '_last_response'

    # CONNECTION parameters ######################################################
    def test_has_default_parameters(self):
        """
        Creating a Quick Base connection sets defaults when not overriden
        """
        assert QuickBase({}).parameters == QuickBase.default_parameters

    def test_parameters_add_new(self):
        """Specifying option(s) adds the option if not in the default option(s)"""
        assert all([
            QuickBase({'clist': '1.2.3.4.5'}).parameters.get('clist') == '1.2.3.4.5',
            QuickBase({'ignoreError': True}).parameters.get('ignoreError') is True,
            (
                QuickBase({
                    'clist': '1.2.3.4.5',
                    'ignoreError': True
                }).parameters.get('clist') == '1.2.3.4.5'
                and
                QuickBase({
                    'clist': '1.2.3.4.5',
                    'ignoreError': True
                }).parameters.get('ignoreError') is True
            ),
        ])

    def test_parameters_override_defaults(self):
        """Specifying option(s) overrides existing default option(s)"""
        assert all([
            QuickBase({'realm': 'abc'}).parameters.get('realm') == 'abc',
            QuickBase({'skipfirst': '0'}).parameters.get('skipfirst') == '0',
            (
                QuickBase({
                    'realm': 'abc',
                    'skipfirst': '0'
                }).parameters.get('realm') == 'abc'
                and
                QuickBase({
                    'realm': 'abc',
                    'skipfirst': '0'
                }).parameters.get('skipfirst') == '0'
            ),
        ])


class TestQuickBaseAPI:
    def test_api(self):
        """
        """
        pass


class TestQuickBasePandas:
    def test_pandas_implemented(self):
        """Converts the last response into a pandas dataframe"""
        pass

    def test_pandas_not_implemented(self):
        """Outputs a warning when requesting pandas dataframe not implemented"""
        pass


class TestQuickBaseJSON:
    def test_json(self):
        """Converts the last response into a json object"""
        qb = QuickBase({})
        qb._last_response = {'key': 1}
        assert qb.json() == '{\n    "key": 1\n}'


class TestQuickBaseDownloadFiles:
    def test_download_files(self):
        """Downloads files from QuickBase using DoQuery => Manual"""
        pass
