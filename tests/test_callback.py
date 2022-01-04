from lib.base_case import get_sid
from lib.assertions import Assertions
from lib import variables
from lib.payloads import payload_callback_200
import allure
from lib.my_requests import MyRequests


@allure.epic("Callback Cases")
class TestCallback:

    @allure.description("This test successfully returns callback results")
    def test_get_callback_successfully(self):
        sid = get_sid()
        response = MyRequests.post(url=f"{variables.callback_url}",
                                   json=payload_callback_200(sid=sid),
                                   headers={'Content-Type': 'application/json',
                                            'Accept': 'text/plain'}
                                   )
        Assertions.assert_code_status(response, 200)
