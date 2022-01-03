from lib.base_case import BaseCase
from lib.assertions import Assertions
import Variables
import allure
from lib.my_requests import MyRequests


@allure.epic("SID Cases")
class TestUserSID(BaseCase):

    @allure.description("This test successfully return SID for user")
    def test_get_sid_successfully(self):
        response = MyRequests.post(url=f"{Variables.url}/init_session",
                                   params={"dboPublicKoUri":"https://portal1.isimplelab.com"})

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "sid")