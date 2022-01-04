from lib.base_case import BaseCase
from lib.assertions import Assertions
import variables
import allure
from lib.my_requests import MyRequests


@allure.epic("SID Cases")
class TestUserSID(BaseCase):

    @allure.description("This test successfully returns SID for user")
    def test_get_sid_successfully(self):
        response = MyRequests.post(url=f"{variables.url}/init_session",
                                   params={"dboPublicKoUri": "https://portal1.isimplelab.com"})

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "sid")

    @allure.description("This test checks error 400 if there is no query parameters")
    def test_get_sid_without_params(self):
        response = MyRequests.post(f"{variables.url}/init_session")

        Assertions.assert_code_status(response, 400)
        names = ["errorCode", "errorMessage"]
        Assertions.assert_json_has_keys(response, names)
        Assertions.assert_json_value_by_name(response, "errorCode", "1011", "Received wrong errorCode")

    @allure.description("This test checks error 400 if there is empty query parameters")
    def test_get_sid_with_empty_param(self):
        response = MyRequests.post(f"{variables.url}/init_session", params={})

        Assertions.assert_code_status(response, 400)
        names = ["errorCode", "errorMessage"]
        Assertions.assert_json_has_keys(response, names)
        Assertions.assert_json_value_by_name(response, "errorCode", "1011", "Received wrong errorCode")
