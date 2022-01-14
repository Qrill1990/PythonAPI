from lib.assertions import Assertions
from lib import variables
import allure
from lib.my_requests import MyRequests


@allure.epic("License Cases")
class TestLicense:

    @allure.title("Тест на корректный возврат токена")
    @allure.description("This test successfully returns license token")
    def test_get_license_successfully(self):
        response = MyRequests.post(url=f"{variables.url}/jwt", params={"installId": "D530D"})

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "token")

    @allure.title("Тест на ответ 400 если installId пустой")
    @allure.description("This test  returns code 400  because installId is empty")
    def test_get_license_with_empty_install_id_param(self):
        response = MyRequests.post(url=f"{variables.url}/jwt", params={"installId": ""})

        Assertions.assert_code_status(response, 400)
        names = ["errorCode", "errorMessage"]
        Assertions.assert_json_has_keys(response, names)
        Assertions.assert_json_value_by_name(response, "errorCode", "1011", "There is wrong errorCode in the response")
        Assertions.assert_json_value_by_name(response, "errorMessage", "Отсутствует обязательный параметр: installId",
                                             "There is wrong errorMessage in the response")

    @allure.title("Тест на ответ 400 если installId отсутствует")
    @allure.description("This test  returns code 400  because installId is empty")
    def test_get_license_without_install_id_param(self):
        response = MyRequests.post(url=f"{variables.url}/jwt")

        Assertions.assert_code_status(response, 400)
        names = ["errorCode", "errorMessage"]
        Assertions.assert_json_has_keys(response, names)
        Assertions.assert_json_value_by_name(response, "errorCode", "1011", "There is wrong errorCode in the response")
        Assertions.assert_json_value_by_name(response, "errorMessage", "Отсутствует обязательный параметр: installId",
                                             "There is wrong errorMessage in the response")
