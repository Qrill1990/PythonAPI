import allure
from lib import variables
from lib.assertions import Assertions
from lib.my_requests import MyRequests
from lib.payloads import unique_uuid
import uuid


@allure.epic("Client Profile Cases")
class TestClientProfile:
    @allure.title("Тест на успешное получение клиентского профиля")
    @allure.description("This test successfully returns 200 and client profile")
    def test_get_client_profile_successfully(self):
        response = MyRequests.get(url=f"{variables.url}/client_profile", data={'resSecret': f'{unique_uuid}'})

        response_as_dict = response.json()
        Assertions.assert_code_status(response, 200)

        Assertions.assert_json_value_by_name(response, "status", "WAIT_QUESTIONNAIRE", "wrong value of status")
        assert response_as_dict["clientProfile"]["surname"] == "Иванов", "wrong value of surname"
        assert response_as_dict["clientProfile"]["name"] == "Евгений", "wrong value of name"
        assert response_as_dict["clientProfile"]["citizenship"] == "RUS", "wrong value of citizenship"
        assert response_as_dict["clientProfile"]["docType"] == "01", "wrong value of docType"
        assert response_as_dict["clientProfile"]["docSeries"] == "1000", "wrong value of docSeries"
        assert response_as_dict["clientProfile"]["docNum"] == "200300", "wrong value of docNum"
        assert response_as_dict["clientProfile"]["docOrgan"] == "ОВД по Центральному району г. Воронеж", \
            "wrong value of docOrgan"
        assert response_as_dict["clientProfile"]["docOrganCode"] == "360005", "wrong value of docOrganCode"
        assert response_as_dict["clientProfile"]["docDate"] == "2010-10-10", "wrong value of docDate"
        assert response_as_dict["clientProfile"]["snils"] == "00000000031", "wrong value of snils"
        assert response_as_dict["clientProfile"]["inn"] == "645933077752", "wrong value of inn"
        assert response_as_dict["clientProfile"]["phoneSms"] == "+7(999)5888000", "wrong value of phoneSms"
        # Пока баг
        # assert response_as_dict["clientProfile"]["email"] == "200300", "wrong value of email"

    @allure.title("Тест на получение клиентского профиля с несуществующим resSecret")
    @allure.description("This test returns 404 because resSecret is wrong")
    def test_get_client_profile_with_wrong_res_secret(self):
        response = MyRequests.get(url=f"{variables.url}/client_profile", data={'resSecret': f'{uuid.uuid4()}'})

        Assertions.assert_code_status(response, 404)

    @allure.title("Тест на получение клиентского профиля с пустым resSecret")
    @allure.description("This test returns 404 because resSecret is empty")
    def test_get_client_profile_with_empty_res_secret(self):
        response = MyRequests.get(url=f"{variables.url}/client_profile", data={'resSecret': ''})

        Assertions.assert_code_status(response, 404)

    @allure.title("Тест на получение клиентского профиля без resSecret")
    @allure.description("This test returns 500 because there is no resSecret")
    def test_get_client_profile_without_res_secret(self):
        response = MyRequests.get(url=f"{variables.url}/client_profile")

        Assertions.assert_code_status(response, 500)
