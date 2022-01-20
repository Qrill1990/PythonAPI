from lib.base_case import get_sid
import allure
from lib.my_requests import MyRequests
from lib import variables
from lib import payloads
from lib.assertions import Assertions
import os.path


@allure.epic("Integration Cases")
class TestJsonFileFolder:
    @allure.title("Тест на проверку, что json файл выгрузился")
    @allure.description("This test checks if json file exists")
    def test_check_json_file(self):
        sid = get_sid()
        response = MyRequests.post(url=f"{variables.callback_url}",
                                   json=payloads.payload_callback_200_person_data(sid=sid),
                                   headers=payloads.common_json_headers
                                   )
        Assertions.assert_code_status(response, 200)

        response1 = MyRequests.post(url=f"{variables.url}/questionnaire/fill", headers=payloads.common_json_headers,
                                    json=payloads.payload_questionnaire_200(payloads.unique_uuid))

        Assertions.assert_code_status(response1, 200)

        assert os.path.isfile(f'/Users/kirilllyubushkin/Downloads/{sid}.json'), "There is no file in directory"
        os.remove(f'/Users/kirilllyubushkin/Downloads/{sid}.json')
