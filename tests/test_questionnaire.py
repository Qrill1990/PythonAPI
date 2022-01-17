from lib.assertions import Assertions
from lib import variables
import allure
from lib.my_requests import MyRequests


@allure.epic("Questionnaire Cases")
class TestQuestionnaire:

    @allure.title("Тест на получение стандартной анкеты с вопросами")
    @allure.description("This test successfully returns 200 and list of questions")
    def test_get_questionnaire(self):
        response = MyRequests.get(url=f"{variables.url}/questionnaire")

        Assertions.assert_code_status(response, 200)
        #  Рациональность данных проверок не ясна. Возможно имеет смысл сравнивать полученный json с заранее известным
        response_as_dict = response.json()
        for i in range(5):
            assert response_as_dict["questions"][i]["code"] == 'Q0' + f'{i + 1}', "Expected another code element"

        assert response_as_dict["questions"][0]["text"] == 'я не являюсь публичным должностным лицом или его ' \
                                                           'родственником', "Expected another text element"
        assert str(response_as_dict["questions"][0]["multiple"]) == 'False', "Expected another multiple element"
        for i in range(5):
            assert response_as_dict["questions"][i]["answers"][0]["code"] == 'Q0' + f'{i + 1}' + 'A01', "Expected " \
                                                                                                        "another " \
                                                                                                        "answer code "
