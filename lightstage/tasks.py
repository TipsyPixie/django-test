import json

import requests

from rekindle.celery import app


@app.task
def get_block_number():
    json_headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'jsonrpc': '2.0',
        'id': '1',
        'method': 'eth_blockNumber',
        'params': [],
    }
    block_number_response = requests.post(url='https://ropsten.infura.io/v3/fad38c4f64bd4241a4df068339705c77',
                                          data=json.dumps(data), headers=json_headers, timeout=10)
    response = block_number_response.json()
    error = response.get('error')
    if error is not None:
        raise Exception(error.get('message'))

    latest_block_index = response.get('result')
    print(int(latest_block_index, 16))

    data = {
        'jsonrpc': '2.0',
        'id': '1',
        'method': 'eth_getBlockByNumber',
        'params': [latest_block_index, False],
    }
    get_block_response = requests.post(url='https://ropsten.infura.io/v3/fad38c4f64bd4241a4df068339705c77',
                                       data=json.dumps(data), headers=json_headers, timeout=10)
    response = get_block_response.json()
    error = response.get('error')
    if error is not None:
        raise Exception(error.get('message'))

    result = response.get('result')
    if result is None:
        raise Exception('result not exists')

    return result
