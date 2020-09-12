from httprunner import HttpRunner, Config, Step, RunRequest


class TestCaseLogin(HttpRunner):

    config = (
        Config("testcase description")
        .verify(False)
        .base_url("https://$host")
        .variables(
            **{
                "phone": "18613143458",
                "password": "msFrwx$!kz3RTRm@Q*pV",
                "host": "mubu.com",
            }
        )
        .export("unreadCount")
    )

    teststeps = [
        Step(
            RunRequest("/")
            .get("/")
            .with_headers(
                **{
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "cache-control": "max-age=0",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "sum_two": "${sum_two(1, 8)}",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                }
            )
            .with_cookies(
                **{
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1599890930",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1599876997",
                    "SESSION": "5d686e1f-826d-4fdc-b504-14b881b6f009",
                    "SLARDAR_WEB_ID": "146babda-a2e0-487a-8b52-4bde6399779f",
                    "_ga": "GA1.2.1447840665.1599876997",
                    "_gat": "1",
                    "_gid": "GA1.2.970346615.1599876997",
                    "country": "US",
                    "csrf_token": "8250e036-f280-4bdb-914f-f3cb77eade64",
                    "data-unique-id": "2b076550-f4be-11ea-a24c-bd8a5840b3db",
                    "data_unique_id": "5a9ff0f2-cc52-4b79-9534-2c318e60bf0e",
                    "language": "en-US",
                    "mubu_inner": "1",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "reg_focusId": "1b148ce7-1055-4171-a1cd-1748072a111",
                    "reg_prepareId": "17480729b79-17480729b0a-4171-a1cd-3c746bea2c3b",
                    "s_v_web_id": "kez1gs78_cBo9G4q5_Vp2j_4z5H_BdsG_1hPeNK4vPVF0",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/login")
            .get("/login")
            .with_headers(
                **{
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "referer": "https://${host}/",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                }
            )
            .with_cookies(
                **{
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1599890937",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1599876997",
                    "SESSION": "5d686e1f-826d-4fdc-b504-14b881b6f009",
                    "SLARDAR_WEB_ID": "ac6b00fe-5f6e-4711-9429-f011cbf86897",
                    "_ga": "GA1.2.1447840665.1599876997",
                    "_gat": "1",
                    "_gid": "GA1.2.970346615.1599876997",
                    "country": "US",
                    "csrf_token": "8250e036-f280-4bdb-914f-f3cb77eade64",
                    "data-unique-id": "2b076550-f4be-11ea-a24c-bd8a5840b3db",
                    "data_unique_id": "5a9ff0f2-cc52-4b79-9534-2c318e60bf0e",
                    "language": "en-US",
                    "mubu_inner": "1",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "reg_focusId": "1b148ce7-1055-4171-a1cd-1748072a111",
                    "reg_prepareId": "17480729b79-17480729b0a-4171-a1cd-3c746bea2c3b",
                    "s_v_web_id": "kez1gs78_cBo9G4q5_Vp2j_4z5H_BdsG_1hPeNK4vPVF0",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/login/password")
            .get("/login/password")
            .with_headers(
                **{
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "referer": "https://${host}/login",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                }
            )
            .with_cookies(
                **{
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1599890940",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1599876997",
                    "SESSION": "5d686e1f-826d-4fdc-b504-14b881b6f009",
                    "SLARDAR_WEB_ID": "473e82c2-dfd0-470a-9a5d-a690fd8e881d",
                    "_ga": "GA1.2.1447840665.1599876997",
                    "_gat": "1",
                    "_gid": "GA1.2.970346615.1599876997",
                    "country": "US",
                    "csrf_token": "8250e036-f280-4bdb-914f-f3cb77eade64",
                    "data-unique-id": "2b076550-f4be-11ea-a24c-bd8a5840b3db",
                    "data_unique_id": "5a9ff0f2-cc52-4b79-9534-2c318e60bf0e",
                    "language": "en-US",
                    "mubu_inner": "1",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "reg_focusId": "8797e022-049d-4296-9054-17480ee6634",
                    "reg_prepareId": "17480ee60c8-17480ee6066-4296-9054-f90b2cf8efe7",
                    "s_v_web_id": "kez1gs78_cBo9G4q5_Vp2j_4z5H_BdsG_1hPeNK4vPVF0",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/api/login/submit")
            .post("/api/login/submit")
            .with_headers(
                **{
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "content-length": "65",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "origin": "https://${host}",
                    "referer": "https://${host}/login/password",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "x-requested-with": "XMLHttpRequest",
                }
            )
            .with_cookies(
                **{
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1599890942",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1599876997",
                    "SESSION": "5d686e1f-826d-4fdc-b504-14b881b6f009",
                    "SLARDAR_WEB_ID": "cbae0f61-fa20-4db3-99f7-85103c083195",
                    "_ga": "GA1.2.1447840665.1599876997",
                    "_gat": "1",
                    "_gid": "GA1.2.970346615.1599876997",
                    "country": "US",
                    "csrf_token": "8250e036-f280-4bdb-914f-f3cb77eade64",
                    "data-unique-id": "2b076550-f4be-11ea-a24c-bd8a5840b3db",
                    "data_unique_id": "5a9ff0f2-cc52-4b79-9534-2c318e60bf0e",
                    "language": "en-US",
                    "mubu_inner": "1",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "reg_focusId": "8797e022-049d-4296-9054-17480ee6634",
                    "reg_prepareId": "17480ee60c8-17480ee6066-4296-9054-f90b2cf8efe7",
                    "s_v_web_id": "kez1gs78_cBo9G4q5_Vp2j_4z5H_BdsG_1hPeNK4vPVF0",
                }
            )
            .with_data(
                {"password": "$password", "phone": "$phone", "remember": "true",}
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
        ),
        Step(
            RunRequest("/list")
            .get("/list")
            .with_headers(
                **{
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "referer": "https://${host}/login/password",
                    "phone": "$phone",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                }
            )
            .with_cookies(
                **{
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1599890942",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1599876997",
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTQ0OTE2NCIsImV4cCI6MTYwMjQ4Mjk0NCwiaWF0IjoxNTk5ODkwOTQ0fQ.ot8AteuCcCv_0HpxGKfu8XUlPoador_5GD1EKFbo5nzGtYeefByF1DaTzI1EgpJQd4hI71prClWPBF7lUWicNQ",
                    "SESSION": "5d686e1f-826d-4fdc-b504-14b881b6f009",
                    "SLARDAR_WEB_ID": "cbae0f61-fa20-4db3-99f7-85103c083195",
                    "_ga": "GA1.2.1447840665.1599876997",
                    "_gat": "1",
                    "_gid": "GA1.2.970346615.1599876997",
                    "country": "US",
                    "csrf_token": "8250e036-f280-4bdb-914f-f3cb77eade64",
                    "data-unique-id": "2b076550-f4be-11ea-a24c-bd8a5840b3db",
                    "data_unique_id": "5a9ff0f2-cc52-4b79-9534-2c318e60bf0e",
                    "language": "en-US",
                    "mubu_inner": "1",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "reg_focusId": "8797e022-049d-4296-9054-17480ee6634",
                    "reg_prepareId": "17480ee60c8-17480ee6066-4296-9054-f90b2cf8efe7",
                    "s_v_web_id": "kez1gs78_cBo9G4q5_Vp2j_4z5H_BdsG_1hPeNK4vPVF0",
                    "user_persistence": "2fed7e44-9c7f-49a1-88d6-1287655322a5",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/api/list/tip_new_update")
            .post("/api/list/tip_new_update")
            .with_headers(
                **{
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "content-length": "0",
                    "origin": "https://${host}",
                    "referer": "https://${host}/list",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "x-requested-with": "XMLHttpRequest",
                }
            )
            .with_cookies(
                **{
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1599890942",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1599876997",
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTQ0OTE2NCIsImV4cCI6MTYwMjQ4Mjk0NCwiaWF0IjoxNTk5ODkwOTQ0fQ.ot8AteuCcCv_0HpxGKfu8XUlPoador_5GD1EKFbo5nzGtYeefByF1DaTzI1EgpJQd4hI71prClWPBF7lUWicNQ",
                    "SESSION": "5d686e1f-826d-4fdc-b504-14b881b6f009",
                    "SLARDAR_WEB_ID": "cbae0f61-fa20-4db3-99f7-85103c083195",
                    "_ga": "GA1.2.1447840665.1599876997",
                    "_gat": "1",
                    "_gid": "GA1.2.970346615.1599876997",
                    "country": "US",
                    "csrf_token": "8250e036-f280-4bdb-914f-f3cb77eade64",
                    "data-unique-id": "2b076550-f4be-11ea-a24c-bd8a5840b3db",
                    "data_unique_id": "5a9ff0f2-cc52-4b79-9534-2c318e60bf0e",
                    "language": "en-US",
                    "mubu_inner": "1",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "reg_focusId": "8797e022-049d-4296-9054-17480ee6634",
                    "reg_prepareId": "17480ee60c8-17480ee6066-4296-9054-f90b2cf8efe7",
                    "s_v_web_id": "kez1gs78_cBo9G4q5_Vp2j_4z5H_BdsG_1hPeNK4vPVF0",
                    "user_persistence": "2fed7e44-9c7f-49a1-88d6-1287655322a5",
                }
            )
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
        ),
        Step(
            RunRequest("/api/list/get")
            .post("/api/list/get")
            .with_headers(
                **{
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "content-length": "38",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "origin": "https://${host}",
                    "referer": "https://${host}/list",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "x-requested-with": "XMLHttpRequest",
                }
            )
            .with_cookies(
                **{
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1599890942",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1599876997",
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTQ0OTE2NCIsImV4cCI6MTYwMjQ4Mjk0NCwiaWF0IjoxNTk5ODkwOTQ0fQ.ot8AteuCcCv_0HpxGKfu8XUlPoador_5GD1EKFbo5nzGtYeefByF1DaTzI1EgpJQd4hI71prClWPBF7lUWicNQ",
                    "SESSION": "5d686e1f-826d-4fdc-b504-14b881b6f009",
                    "SLARDAR_WEB_ID": "cbae0f61-fa20-4db3-99f7-85103c083195",
                    "_ga": "GA1.2.1447840665.1599876997",
                    "_gat": "1",
                    "_gid": "GA1.2.970346615.1599876997",
                    "country": "US",
                    "csrf_token": "8250e036-f280-4bdb-914f-f3cb77eade64",
                    "data-unique-id": "2b076550-f4be-11ea-a24c-bd8a5840b3db",
                    "data_unique_id": "5a9ff0f2-cc52-4b79-9534-2c318e60bf0e",
                    "language": "en-US",
                    "mubu_inner": "1",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "reg_focusId": "8797e022-049d-4296-9054-17480ee6634",
                    "reg_prepareId": "17480ee60c8-17480ee6066-4296-9054-f90b2cf8efe7",
                    "s_v_web_id": "kez1gs78_cBo9G4q5_Vp2j_4z5H_BdsG_1hPeNK4vPVF0",
                    "user_persistence": "2fed7e44-9c7f-49a1-88d6-1287655322a5",
                }
            )
            .with_data({"folderId": "0", "keywords": "", "sort": "name", "source": ""})
            .teardown_hook("${get_folders_num($response)}", "foldersNum")
            .extract()
            .with_jmespath("body.data.folders", "foldersList")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
            .assert_length_greater_than("$foldersList", 5)
            .assert_greater_than("$foldersNum", 5)
        ),
        Step(
            RunRequest("/api/message/get_message_unread")
            .post("/api/message/get_message_unread")
            .with_headers(
                **{
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "content-length": "0",
                    "origin": "https://${host}",
                    "referer": "https://${host}/list",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "HttpRunner/${get_httprunner_version()}",
                    "x-requested-with": "XMLHttpRequest",
                }
            )
            .with_cookies(
                **{
                    "Hm_lpvt_4426cbb0486a79ea049b4ad52d81b504": "1599890942",
                    "Hm_lvt_4426cbb0486a79ea049b4ad52d81b504": "1599876997",
                    "Jwt-Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTQ0OTE2NCIsImV4cCI6MTYwMjQ4Mjk0NCwiaWF0IjoxNTk5ODkwOTQ0fQ.ot8AteuCcCv_0HpxGKfu8XUlPoador_5GD1EKFbo5nzGtYeefByF1DaTzI1EgpJQd4hI71prClWPBF7lUWicNQ",
                    "SESSION": "5d686e1f-826d-4fdc-b504-14b881b6f009",
                    "SLARDAR_WEB_ID": "cbae0f61-fa20-4db3-99f7-85103c083195",
                    "_ga": "GA1.2.1447840665.1599876997",
                    "_gat": "1",
                    "_gid": "GA1.2.970346615.1599876997",
                    "country": "US",
                    "csrf_token": "8250e036-f280-4bdb-914f-f3cb77eade64",
                    "data-unique-id": "2b076550-f4be-11ea-a24c-bd8a5840b3db",
                    "data_unique_id": "5a9ff0f2-cc52-4b79-9534-2c318e60bf0e",
                    "language": "en-US",
                    "mubu_inner": "1",
                    "reg_entrance": "https%3A%2F%2Fmubu.com%2F",
                    "reg_focusId": "8797e022-049d-4296-9054-17480ee6634",
                    "reg_prepareId": "17480ee60c8-17480ee6066-4296-9054-f90b2cf8efe7",
                    "s_v_web_id": "kez1gs78_cBo9G4q5_Vp2j_4z5H_BdsG_1hPeNK4vPVF0",
                    "user_persistence": "2fed7e44-9c7f-49a1-88d6-1287655322a5",
                }
            )
            .with_data("")
            .extract()
            .with_jmespath("body.data.unreadCount", "unreadCount")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", None)
        ),
    ]


if __name__ == "__main__":
    TestCaseLogin().test_start()
