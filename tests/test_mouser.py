from mouser import __version__
from mouser.api import MouserPartSearchRequest


def test_version():
    assert __version__ == '0.1.5'

def test_search_partnumber(file_keys='mouser_api_keys.yaml'):

    partnumber = 'DMP2066LSN-7'

    request = MouserPartSearchRequest('partnumber', file_keys=file_keys)
    assert request.api_url == 'https://api.mouser.com/api/v1.0/search/partnumber'

    success = request.part_search(partnumber)
    assert success is True

    part = request.get_clean_response()[0]
    assert part['Manufacturer'] == 'Diodes Incorporated'
    assert part['ManufacturerPartNumber'] == 'DMP2066LSN-7'
    assert part['MouserPartNumber'] == '621-DMP2066LSN-7'

def test_search_keyword(file_keys='mouser_api_keys.yaml'):

    keyword = 'DMP2066LSN-7'

    request = MouserPartSearchRequest('keyword', file_keys=file_keys)
    assert request.api_url == 'https://api.mouser.com/api/v1.0/search/keyword'

    success = request.keyword_search(keyword)
    assert success is True

    part = request.get_clean_response()[0]
    assert part['Manufacturer'] == 'Diodes Incorporated'
    assert part['ManufacturerPartNumber'] == 'DMP2066LSN-7'
    assert part['MouserPartNumber'] == '621-DMP2066LSN-7'


def test_search_ibn():

    ibn_code = '60W0DO'

    request = MouserPartSearchRequest('ibn')
    assert request.api_url == 'https://api.mouser.com/api/mobile/v2/search/getIBNs?ibnCode='

    success = request.ibn_search(ibn_code)
    assert success is True

    ibn_data = request.get_ibn_data()
    assert ibn_data.get('IBNCode') == ibn_code
    assert 'MouserPartNumber' in ibn_data


if __name__ == '__main__':
    test_version()
    test_search_partnumber()
    test_search_keyword()
    test_search_ibn()
