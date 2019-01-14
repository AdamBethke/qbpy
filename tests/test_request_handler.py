import pytest
from qbpy.request_handler import _RequestHandler

API_URL_ROOT = 'https://realm.quickbase.com/db/dbid'

class TestRequestHandler:
    def test_repr(self):
        rh = _RequestHandler('API_DoQuery', {})
        assert repr(rh) == 'RequestHandler ({0}) at {1}'.format(rh.action, hex(id(rh)))

    # URL #####################################################################
    @pytest.mark.parametrize('method, url', [
        ('API_AddRecord', API_URL_ROOT + '?a=API_AddRecord'),
        ('API_DoQuery', API_URL_ROOT + '?a=API_DoQuery'),
        ('API_ImportFromCSV', API_URL_ROOT),
        ('API_PurgeRecords', API_URL_ROOT + '?a=API_PurgeRecords'),
        ('API_RemoveUserFromRole', API_URL_ROOT + '?a=API_RemoveUserFromRole'),
        ('API_UserRoles', API_URL_ROOT + '?a=API_UserRoles')
    ])
    def test_url(self, method, url):
        assert _RequestHandler(method, {
            'domain' : 'quickbase.com',
            'realm' : 'realm',
            'dbid' : 'dbid'
        }).url == url

    # PAYLOAD #################################################################
    @pytest.mark.parametrize('method, parameters, payload', [
        (
            'API_DoQuery',
            {'query' : "({'7'.EX.'1'})"},
            {'query' : "({'7'.EX.'1'})"}
        ),
        (
            'API_AddRecord',
            {'fields' : {'6' : 'Values', '7' : '1'}},
            {'_fid_6': 'Values', '_fid_7': '1'}
        ),
        (
            'API_PurgeRecords',
            {'query' : ''},
            {'query' : ''},
        ),
    ])
    def test_standard_payload(self, method, parameters, payload):
        assert _RequestHandler(
            method,
            dict({
                'realm': '1',
                'domain': 'quickbase.com',
                'dbid': '1'
            }, **parameters)
        ).payload == payload

    def test_xml_payload(self):
        assert _RequestHandler(
            'API_ImportFromCSV',
            dict({
                'realm': '1',
                'domain': 'quickbase.com',
                'dbid': '1',
                'records_csv': '1, 2, 3',
                'clist': '1.2.3.4',
                'skipfirst': 1,
                'apptoken': '1234',
                'usertoken': '2345',
                'clist_output': '1.2.3.4',
            })
        ).payload \
        == '<qdbapi><records_csv><![CDATA[1, 2, 3]]></records_csv><clist>1.2.3.4</clist><skipfirst>1</skipfirst><apptoken>1234</apptoken><usertoken>2345</usertoken><clist_output>1.2.3.4</clist_output></qdbapi>'
