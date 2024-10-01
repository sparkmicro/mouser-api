import click
import json

from . import __version__
from .api import MouserOrderRequest, MouserPartSearchRequest
from .api import MouserCartRequest, MouserOrderHistoryRequest


# API Keys File (Default)
API_KEYS_FILE = 'mouser_api_keys.yaml'


@click.command()
@click.version_option(version=__version__, prog_name='Mouser Python API')
@click.argument('request_type', type=click.Choice(['cart', 'history', 'order', 'search'], case_sensitive=False), required=True)
@click.argument('operation', required=True)
@click.option('--number', required=False, help='Part or Order number.')
@click.option('--keyword', required=False, help='Keyword(s) to search')
@click.option('--record-limit', required=False, help='How many records --keyword search should return')
@click.option('--option', required=False, help='Options supported by Mouser search engine. Available options depend on OPERATION.')
@click.option('--export', is_flag=True, required=False, help='Export data to CSV.')
def mouser_cli(request_type, operation, number, keyword, record_limit, option, export):
    ''' Main CLI entry point '''

    args = []

    # Create request
    if request_type == 'order':
        args.append(number)
        request = MouserOrderRequest(operation, API_KEYS_FILE, *args)

        if request.url:
            print(f'[LINK]\t{request.api_url}')
            # Run request
            request.run()

            if export:
                # Export order lines to CSV
                filename = request.export_order_lines_to_csv(order_number=number, clean=True)
                print(f'[DATA]\tOrder lines exported to {filename}')
            else:
                # Print it
                print('[DATA]')
                request.print_response()

    elif request_type == 'search':
        request = MouserPartSearchRequest(operation, API_KEYS_FILE, *args)

        if request.url:
            print(f'[LINK]\t{request.api_url}')

            if operation == 'partnumber':
                if not number:
                    print('[ERROR]\tMissing Mouser Part Number')
                else:
                    if option not in [None, 'None', 'Exact']:
                        print('[ERROR]\t --option must be [None|Exact]')
                    else:
                        # Run request
                        search = request.part_search(number, option)
                        # Print body
                        print('[BODY]')
                        print(json.dumps(request.body, indent=4, sort_keys=True))
                        if search:
                            # Print result
                            print('[DATA]')
                            request.print_clean_response()

            if operation == 'keyword':
                if not keyword:
                    print('[ERROR]\t Missing --keyword flag and keyword(s)')
                else:
                    if option not in [None, 'None', 'Rohs', 'InStock', 'RohsAndInStock']:
                        print('[ERROR]\t --option must be [None|Rohs|InStock|RohsAndInStock]')
                    else:
                        # Run request
                        search = request.keyword_search(keyword, record_limit, option)
                        # Print body
                        print('[BODY]')
                        print(json.dumps(request.body, indent=4, sort_keys=True))
                        if search:
                            # Print result
                            print('[DATA]')
                            request.print_clean_response()

    elif request_type == 'cart':
        request = MouserCartRequest(operation, API_KEYS_FILE, *args)

    elif request_type == 'history':
        request = MouserOrderHistoryRequest(operation, API_KEYS_FILE, *args)
