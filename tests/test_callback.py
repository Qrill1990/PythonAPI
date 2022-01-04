from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib import variables
from lib.payloads import Payloads
import allure
from lib.my_requests import MyRequests


@allure.epic("Callback Cases")
class TestCallback(BaseCase):

    @allure.description("This test successfully returns callback results")
    def test_get_callback_successfully(self):
        sid = self.get_sid()
        response = MyRequests.post(url=f"{variables.callback_url}",
                                   json=Payloads.payload_callback_200(self, sid=sid),
                                   headers={'Content-Type': 'application/json',
                                            'Accept': 'text/plain'}
                                   )
        Assertions.assert_code_status(response, 200)
