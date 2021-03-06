from lib.base_case import get_sid
from lib.assertions import Assertions
from lib import variables
from lib.payloads import *
import allure
from lib.my_requests import MyRequests
import uuid


@allure.epic("Callback Cases")
class TestCallback:
    sid = get_sid()

    @allure.title("Тест на ответ 200 если передан массив person_data")
    @allure.description("This test successfully returns callback results with person_data")
    def test_get_callback_successfully_with_person_data(self):
        response = MyRequests.post(url=f"{variables.callback_url}",
                                   json=payload_callback_200_person_data(sid=self.sid),
                                   headers=common_json_headers
                                   )
        Assertions.assert_code_status(response, 200)

    @allure.title("Тест на ответ 200 если передан массив user_data")
    @allure.description("This test successfully returns callback results with user_data")
    def test_get_callback_successfully_with_user_data(self):
        response = MyRequests.post(url=f"{variables.callback_url}",
                                   json=payload_callback_200_user_data(sid=get_sid()),
                                   headers=common_json_headers
                                   )
        Assertions.assert_code_status(response, 200)

    @allure.title("Тест на ответ 400 если передан несуществующий сид")
    @allure.description("This test returns 400 because there is no sid in database")
    def test_get_callback_with_wrong_sid(self):
        response = MyRequests.post(url=f"{variables.callback_url}",
                                   json=payload_callback_200_user_data(sid=uuid.uuid4()),
                                   headers=common_json_headers
                                   )
        Assertions.assert_code_status(response, 400)
        names = ["code", "message"]
        Assertions.assert_json_has_keys(response, names)
        Assertions.assert_json_value_by_name(response, "code", "BNK-0003", "There is wrong code")
        Assertions.assert_json_value_by_name(response, "message",
                                             "Сессия с указанным sid не существует",
                                             "there is wrong message in message key")

    @allure.title("Тест на ответ 400 если не передан массив person_data/user_data")
    @allure.description("This test returns 400 because there is no person_data/user_data in payload")
    def test_get_callback_without_person_data(self):
        response = MyRequests.post(url=f"{variables.callback_url}",
                                   json=payload_callback_400(sid=self.sid),
                                   headers=common_json_headers
                                   )
        Assertions.assert_code_status(response, 400)
        names = ["code", "message"]
        Assertions.assert_json_has_keys(response, names)
        Assertions.assert_json_value_by_name(response, "code", "BNK-0001", "There is wrong code from adapter")
        Assertions.assert_json_value_by_name(response, "message",
                                             "В запросе отсутствует параметр user_data/person_data",
                                             "there is wrong message in message key")

    @allure.title("Тест на ответ 400 если передан только сид")
    @allure.description("This test returns 400 because there is no data but sid")
    def test_get_callback_without_anything_but_sid(self):
        response = MyRequests.post(url=f"{variables.callback_url}",
                                   json=payload_callback_400_auth(sid=self.sid),
                                   headers=common_json_headers
                                   )
        Assertions.assert_code_status(response, 400)
        names = ["code", "message"]
        Assertions.assert_json_has_keys(response, names)
        Assertions.assert_json_value_by_name(response, "code", "BNK-0001", "There is wrong code from adapter")
        Assertions.assert_json_value_by_name(response, "message", "В запросе отсутствует параметр auth_result",
                                             "there is wrong message in message key")

    @allure.title("Тест на ответ 400 если передано пустое тело запроса")
    @allure.description("This test returns 400 because there is empty callback")
    def test_get_callback_without_anything(self):
        response = MyRequests.post(url=f"{variables.callback_url}",
                                   json={},
                                   headers=common_json_headers
                                   )
        Assertions.assert_code_status(response, 400)
        names = ["code", "message"]
        Assertions.assert_json_has_keys(response, names)
        Assertions.assert_json_value_by_name(response, "code", "BNK-0001", "There is wrong code from adapter")
        Assertions.assert_json_value_by_name(response, "message", "В запросе отсутствует параметр sid",
                                             "there is wrong message in message key")
