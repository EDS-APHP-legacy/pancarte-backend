import json

import requests

from moniwave.settings import DEBUG, PANCARTE_DB


def construct_url(*path):
    url = 'http://{}:{}/{}'.format(
        PANCARTE_DB['endpoint']['host'],
        PANCARTE_DB['endpoint']['port'],
        '/'.join(path))
    if DEBUG:
        print(url)
    return url


def http_get(*path, **params):
    url = construct_url(*path)

    result = requests.get(url, params=params)

    if result.status_code != 200:
        raise RuntimeError(result.reason)

    return json.loads(result.text)


def http_post(*path, **params):
    url = construct_url(*path)

    result = requests.post(url, data=params)

    if result.status_code != 201:
        raise RuntimeError(result.reason)

    return json.loads(result.text)


def http_put(*path, id, **params):
    url = construct_url(*path, str(id))

    result = requests.put(url, data=params)

    if result.status_code != 200:
        raise RuntimeError(result.reason)

    return json.loads(result.text)


def http_delete(*path, id):
    url = construct_url(*path, str(id))

    result = requests.delete(url)

    if result.status_code != 204:
        raise RuntimeError(result.reason)

    return json.loads(result.text)

