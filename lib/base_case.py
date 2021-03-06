import json.decoder
import requests
from requests import Response
from lib import variables


def get_cookie(response: Response, cookie_name):
    assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
    return response.cookies[cookie_name]


def get_json_value(response: Response, name):
    try:
        response_as_dict = response.json()
    except json.decoder.JSONDecodeError:
        assert False, f"Response is not in JSON format. Response text is '{response.text}'"

    assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    return response_as_dict[name]


def get_header(response: Response, headers_name):
    assert headers_name in response.headers, f"Cannot find header with name {headers_name} in the last response"
    return response.headers[headers_name]


def get_sid():
    response = requests.post(url=f"{variables.url}/init_session",
                             params={"dboPublicKoUri": "https://portal1.isimplelab.com"}
                             )

    try:
        response_as_dict = response.json()
    except json.decoder.JSONDecodeError:
        assert False, f"Response is not in JSON format. Response text is '{response.text}'"
    return response_as_dict["sid"]
