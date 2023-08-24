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

    part = request.get_clean_response()
    assert part['Manufacturer'] == 'Diodes Incorporated'
    assert part['ManufacturerPartNumber'] == 'DMP2066LSN-7'
    assert part['MouserPartNumber'] == '621-DMP2066LSN-7'

if __name__ == '__main__':
    test_version()
    test_search_partnumber()
