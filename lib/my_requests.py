import requests
from lib.logger import Logger
import allure


class MyRequests:
    @staticmethod
    def post(url: str, json: dict = None, data: dict = None, params: dict = None, headers: dict = None,
             cookies: dict = None):
        with allure.step(f"POST request to URL '{url}'"):
            return MyRequests._send(url, json, data, params, headers, cookies, "POST")

    @staticmethod
    def get(url: str, json: dict = None, data: dict = None, params: dict = None, headers: dict = None,
            cookies: dict = None):
        with allure.step(f"GET request to URL '{url}'"):
            return MyRequests._send(url, json, data, params, headers, cookies, "GET")

    @staticmethod
    def put(url: str,  json: dict = None, data: dict = None,  params: dict = None, headers: dict = None,
            cookies: dict = None):
        with allure.step(f"PUT request to URL '{url}'"):
            return MyRequests._send(url, json, data, params, headers, cookies, "PUT")

    @staticmethod
    def delete(url: str,  json: dict = None, data: dict = None,  params: dict = None, headers: dict = None,
               cookies: dict = None):
        with allure.step(f"DELETE request to URL '{url}'"):
            return MyRequests._send(url, json, data, params, headers, cookies, "DELETE")

    @staticmethod
    def _send(url: str, json: dict, data: dict, params: dict, headers: dict, cookies: dict, method: str):

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_request(url, json, data, params, headers, cookies, method)

        if method == "GET":
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(url, json=json, data=data, params=params, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(url, json=json, data=json, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, json=json, data=json, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP method '{method}' was received")

        Logger.add_response(response)

        return response
