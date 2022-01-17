import allure
from lib import variables
from lib.assertions import Assertions
from lib.my_requests import MyRequests
from lib.payloads import common_json_headers, payload_questionnaire_200, unique_uuid
from lib.payloads import payload_questionnaire_with_wrong_res_secret, payload_questionnaire_with_empty_res_secret
from lib.payloads import payload_questionnaire_without_res_secret, payload_questionnaire_400_answer_value
from lib.payloads import payload_questionnaire_400_no_answers, payload_questionnaire_400_no_question


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

    @allure.title("Тест на успешную отправку ответов на вопросы")
    @allure.description("This test successfully returns 200")
    def test_questionnaire_success(self):
        response = MyRequests.post(url=f"{variables.url}/questionnaire/fill", headers=common_json_headers,
                                   json=payload_questionnaire_200(unique_uuid))

        Assertions.assert_code_status(response, 200)

    @allure.title("Тест на отправку ответов на вопросы с неверным resSecret")
    @allure.description("This test returns 400 because there is no resSecret in database")
    def test_questionnaire_wrong_res_secret(self):
        response = MyRequests.post(url=f"{variables.url}/questionnaire/fill", headers=common_json_headers,
                                   json=payload_questionnaire_with_wrong_res_secret())

        Assertions.assert_code_status(response, 400)
        names = ["errorCode", "errorMessage"]
        Assertions.assert_json_has_keys(response, names)
        Assertions.assert_json_value_by_name(response, "errorCode", "1012", "There is wrong errorCode in response")

    @allure.title("Тест на отправку ответов на вопросы с пустым resSecret")
    @allure.description("This test returns 400 because there is empty resSecret")
    def test_questionnaire_empty_res_secret(self):
        response = MyRequests.post(url=f"{variables.url}/questionnaire/fill", headers=common_json_headers,
                                   json=payload_questionnaire_with_empty_res_secret())

        Assertions.assert_code_status(response, 400)
        names = ["errorCode", "errorMessage"]
        Assertions.assert_json_has_keys(response, names)
        Assertions.assert_json_value_by_name(response, "errorCode", "1012", "There is wrong errorCode in response")
        Assertions.assert_json_value_by_name(response, "errorMessage", "Запрос с resSecret =  не найден!",
                                             "There is wrong errorMessage in response")

    @allure.title("Тест на отправку ответов на вопросы без resSecret")
    @allure.description("This test returns 400 because there is no resSecret")
    def test_questionnaire_empty_res_secret(self):
        response = MyRequests.post(url=f"{variables.url}/questionnaire/fill", headers=common_json_headers,
                                   json=payload_questionnaire_without_res_secret())

        Assertions.assert_code_status(response, 400)
        names = ["timestamp", "status", "error", "path"]
        Assertions.assert_json_has_keys(response, names)
        Assertions.assert_json_value_by_name(response, "error", "Bad Request", "There is wrong error in response")
        Assertions.assert_json_value_by_name(response, "path", "/ubi/questionnaire/fill",
                                             "There is wrong path in response")

    @allure.title("Тест на отправку ответов на вопросы c неверным ответом")
    @allure.description("This test returns 400 because there is wrong answer value")
    def test_questionnaire_wrong_answer_value(self):
        response = MyRequests.post(url=f"{variables.url}/questionnaire/fill", headers=common_json_headers,
                                   json=payload_questionnaire_400_answer_value(unique_uuid))

        Assertions.assert_code_status(response, 400)
        names = ["errorCode", "errorMessage"]
        Assertions.assert_json_has_keys(response, names)
        Assertions.assert_json_value_by_name(response, "errorCode", "1009", "There is wrong error in response")
        Assertions.assert_json_value_by_name(response, "errorMessage",
                                             "В поле answerValue вопроса с кодом Q01 и ответа с кодом Q01A01 "
                                             "необходимо передавать 0 или 1",
                                             "There is wrong errorMessage in response")

    @allure.title("Тест на отправку ответов на вопросы без ответа")
    @allure.description("This test returns 400 because there is no answer value")
    def test_questionnaire_empty_answer(self):
        response = MyRequests.post(url=f"{variables.url}/questionnaire/fill", headers=common_json_headers,
                                   json=payload_questionnaire_400_no_answers(unique_uuid))

        Assertions.assert_code_status(response, 400)
        names = ["errorCode", "errorMessage"]
        Assertions.assert_json_has_keys(response, names)
        Assertions.assert_json_value_by_name(response, "errorCode", "1010", "There is wrong error in response")
        Assertions.assert_json_value_by_name(response, "errorMessage",
                                             "Для вопроса с кодом Q05 необходимо выбрать как минимум один вариант "
                                             "ответа",
                                             "There is wrong errorMessage in response")

    @allure.title("Тест на отправку ответов на вопросы без вопроса")
    @allure.description("This test returns 400 because there is no question")
    def test_questionnaire_empty_question(self):
        response = MyRequests.post(url=f"{variables.url}/questionnaire/fill", headers=common_json_headers,
                                   json=payload_questionnaire_400_no_question(unique_uuid))

        Assertions.assert_code_status(response, 400)
        names = ["errorCode", "errorMessage"]
        Assertions.assert_json_has_keys(response, names)
        Assertions.assert_json_value_by_name(response, "errorCode", "1003", "There is wrong error in response")
        Assertions.assert_json_value_by_name(response, "errorMessage", "Отсутствуют ответы на вопросы: [Q05]",
                                             "There is wrong errorMessage in response")
