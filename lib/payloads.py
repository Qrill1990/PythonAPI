import uuid

unique_uuid = uuid.uuid4()


def payload_callback_200_person_data(sid):
    data = {
        'sid': f'{sid}',
        'auth_result': 'true',
        'res_secret': f'{unique_uuid}',
        'extended_result': 'eyJraWQiOiIyNTE4ZDNhMy05NTc0LTRkOTMtODQ0YS0wZjIwNjE2YTI3Mj /'
                           'QiLCJ0eXAiOiJKV1QiLCJhbGciOiJHT1NUMzQxMCJ9.eyJyZXN1bHQiOnR /'
                           'ydWUsInN1YiI6IjEwMDAzMTY5MTEiLCJhdWQiOiJUS19VQlNfREVWIiwib /'
                           'mJmIjoxNTUzMDAxNjgxLCJpc3MiOiJVQlNfREVWIiwibWF0Y2giOiJ7XCJ /'
                           'vdmVyYWxsXCI6MS4wLFwiZmFjZVwiOjEuMCxcInZvaWNlXCI6MS4wfSIsI /'
                           'mV4cCI6MTU1MzAwMjI4MiwiaWF0IjoxNTUzMDAxNjgwfQ==.BxQtSa5H7x /'
                           'pEZ_n8xiyy1F1D-RiQDCDFGnucN6GCkmBKOwY0AxxNEl8TTN9wLNoYGBcE /'
                           'mD1RPNQhrDe45pHFgA==',
        'person_data': {
            'lastName': 'Иванов',
            'addresses': {
                'stateFacts': [
                    'hasSize'
                ],
                'size': '2',
                'eTag': 'EDBE4592683C4BC61B17D5100BE462A00504A99D',
                'elements': [
                    {
                        'stateFacts': [
                            'Identifiable'
                        ],
                        'id': '62621',
                        'type': 'PLV',
                        'countryId': 'RUS',
                        'addressStr': 'г Иркутск, ул 2-я Московская',
                        'fiasCode': '65d77bbf-d002-4ecd-8390-583ccfdbf034',
                        'zipCode': '664014',
                        'region': 'Иркутская',
                        'city': 'Иркутск',
                        'street': '2-я Московская',
                        'house': '77',
                        'eTag': '1DFABE9B957174C89E6FAE6132F6FC9D5071E5F8'
                    },
                    {
                        'stateFacts': [
                            'Identifiable'
                        ],
                        'id': '62620',
                        'type': 'PRG',
                        'countryId': 'RUS',
                        'addressStr': 'г Воронеж, ул Московская',
                        'fiasCode': 'fc60c716-57f2-461a-8a21-52d6a7d650a4',
                        'zipCode': '394018',
                        'region': 'Воронежская',
                        'city': 'Воронеж',
                        'street': 'Московская',
                        'house': '1',
                        'eTag': '55730F91FF9B78767C105A0E5A09D31585C1496F'
                    }
                ]
            },
            'verifying': 'false',
            'gender': 'M',
            'documents': {
                'stateFacts': [
                    'hasSize'
                ],
                'size': '1',
                'eTag': '2778A43AB950AE02B8E8EC2CC8402E14E28C7C23',
                'elements': [
                    {
                        'stateFacts': [
                            'EntityRoot'
                        ],
                        'id': '35801',
                        'type': 'RF_PASSPORT',
                        'vrfStu': 'VERIFIED',
                        'series': '1000',
                        'number': '200300',
                        'issueDate': '10.10.2010',
                        'issueId': '360005',
                        'issuedBy': 'ОВД по Центральному району г. Воронеж',
                        'eTag': 'EEA78C891874184E92214C3D8AA5782330CB6AC7'
                    }
                ]
            },
            'citizenship': 'RUS',
            'inn': '645933077752',
            'updatedOn': '1612547779',
            'birthDate': '10.04.1992',
            'stateFacts': [
                'EntityRoot'
            ],
            'rIdDoc': '35001',
            'firstName': 'Евгений',
            'birthPlace': 'г. Иркутск',
            'trusted': 'true',
            'containsUpCfmCode': 'false',
            'middleName': 'Владимирович',
            'eTag': '1193F6F084C35136D8845769C42DC5842CAF1E16',
            'snils': '000-000-000 31',
            'contacts': {
                'stateFacts': [
                    'hasSize'
                ],
                'size': '2',
                'eTag': 'FBCF47412B3E5F724419371B9745CE6A77D6C098',
                'elements': [
                    {
                        'stateFacts': [
                            'Identifiable'
                        ],
                        'id': '14276100',
                        'type': 'EML',
                        'vrfStu': 'VERIFIED',
                        'value': 'esldff@gmail.com',
                        'eTag': '1D2E54819C4D9676FED052DC52C9EC4AF5D75522'
                    },
                    {
                        'stateFacts': [
                            'Identifiable'
                        ],
                        'id': '14446190',
                        'type': 'MBT',
                        'vrfStu': 'VERIFIED',
                        'value': '+7(999)5888000',
                        'eTag': '2FE8A73E9A89BAA5B9C334B9FCC7BE26E2FAB6CE'
                    }
                ]
            },
            'status': 'REGISTERED'
        }
    }
    return data


def payload_callback_200_user_data(sid):
    data = {
        'sid': f'{sid}',
        'auth_result': 'true',
        'res_secret': f'{uuid.uuid4()}',
        'extended_result': 'eyJraWQiOiIyNTE4ZDNhMy05NTc0LTRkOTMtODQ0YS0wZjIwNjE2YTI3Mj /'
                           'QiLCJ0eXAiOiJKV1QiLCJhbGciOiJHT1NUMzQxMCJ9.eyJyZXN1bHQiOnR /'
                           'ydWUsInN1YiI6IjEwMDAzMTY5MTEiLCJhdWQiOiJUS19VQlNfREVWIiwib /'
                           'mJmIjoxNTUzMDAxNjgxLCJpc3MiOiJVQlNfREVWIiwibWF0Y2giOiJ7XCJ /'
                           'vdmVyYWxsXCI6MS4wLFwiZmFjZVwiOjEuMCxcInZvaWNlXCI6MS4wfSIsI /'
                           'mV4cCI6MTU1MzAwMjI4MiwiaWF0IjoxNTUzMDAxNjgwfQ==.BxQtSa5H7x /'
                           'pEZ_n8xiyy1F1D-RiQDCDFGnucN6GCkmBKOwY0AxxNEl8TTN9wLNoYGBcE /'
                           'mD1RPNQhrDe45pHFgA==',
        'user_data': {
            'lastName': 'Иванов',
            'addresses': {
                'stateFacts': [
                    'hasSize'
                ],
                'size': '2',
                'eTag': 'EDBE4592683C4BC61B17D5100BE462A00504A99D',
                'elements': [
                    {
                        'stateFacts': [
                            'Identifiable'
                        ],
                        'id': '62621',
                        'type': 'PLV',
                        'countryId': 'RUS',
                        'addressStr': 'г Иркутск, ул 2-я Московская',
                        'fiasCode': '65d77bbf-d002-4ecd-8390-583ccfdbf034',
                        'zipCode': '664014',
                        'region': 'Иркутская',
                        'city': 'Иркутск',
                        'street': '2-я Московская',
                        'house': '77',
                        'eTag': '1DFABE9B957174C89E6FAE6132F6FC9D5071E5F8'
                    },
                    {
                        'stateFacts': [
                            'Identifiable'
                        ],
                        'id': '62620',
                        'type': 'PRG',
                        'countryId': 'RUS',
                        'addressStr': 'г Воронеж, ул Московская',
                        'fiasCode': 'fc60c716-57f2-461a-8a21-52d6a7d650a4',
                        'zipCode': '394018',
                        'region': 'Воронежская',
                        'city': 'Воронеж',
                        'street': 'Московская',
                        'house': '1',
                        'eTag': '55730F91FF9B78767C105A0E5A09D31585C1496F'
                    }
                ]
            },
            'verifying': 'false',
            'gender': 'M',
            'documents': {
                'stateFacts': [
                    'hasSize'
                ],
                'size': '1',
                'eTag': '2778A43AB950AE02B8E8EC2CC8402E14E28C7C23',
                'elements': [
                    {
                        'stateFacts': [
                            'EntityRoot'
                        ],
                        'id': '35801',
                        'type': 'RF_PASSPORT',
                        'vrfStu': 'VERIFIED',
                        'series': '1000',
                        'number': '200300',
                        'issueDate': '10.10.2010',
                        'issueId': '360005',
                        'issuedBy': 'ОВД по Центральному району г. Воронеж',
                        'eTag': 'EEA78C891874184E92214C3D8AA5782330CB6AC7'
                    }
                ]
            },
            'citizenship': 'RUS',
            'inn': '645933077752',
            'updatedOn': '1612547779',
            'birthDate': '10.04.1992',
            'stateFacts': [
                'EntityRoot'
            ],
            'rIdDoc': '35001',
            'firstName': 'Евгений',
            'birthPlace': 'г. Иркутск',
            'trusted': 'true',
            'containsUpCfmCode': 'false',
            'middleName': 'Владимирович',
            'eTag': '1193F6F084C35136D8845769C42DC5842CAF1E16',
            'snils': '000-000-000 31',
            'contacts': {
                'stateFacts': [
                    'hasSize'
                ],
                'size': '2',
                'eTag': 'FBCF47412B3E5F724419371B9745CE6A77D6C098',
                'elements': [
                    {
                        'stateFacts': [
                            'Identifiable'
                        ],
                        'id': '14276100',
                        'type': 'EML',
                        'vrfStu': 'VERIFIED',
                        'value': 'esldff@gmail.com',
                        'eTag': '1D2E54819C4D9676FED052DC52C9EC4AF5D75522'
                    },
                    {
                        'stateFacts': [
                            'Identifiable'
                        ],
                        'id': '14446190',
                        'type': 'MBT',
                        'vrfStu': 'VERIFIED',
                        'value': '+7(999)5888000',
                        'eTag': '2FE8A73E9A89BAA5B9C334B9FCC7BE26E2FAB6CE'
                    }
                ]
            },
            'status': 'REGISTERED'
        }
    }
    return data


def payload_callback_400(sid):
    data = {
        'sid': f'{sid}',
        'auth_result': 'true',
        'res_secret': f'{unique_uuid}',
        'extended_result': 'eyJraWQiOiIyNTE4ZDNhMy05NTc0LTRkOTMtODQ0YS0wZjIwNjE2YTI3Mj /'
                           'QiLCJ0eXAiOiJKV1QiLCJhbGciOiJHT1NUMzQxMCJ9.eyJyZXN1bHQiOnR /'
                           'ydWUsInN1YiI6IjEwMDAzMTY5MTEiLCJhdWQiOiJUS19VQlNfREVWIiwib /'
                           'mJmIjoxNTUzMDAxNjgxLCJpc3MiOiJVQlNfREVWIiwibWF0Y2giOiJ7XCJ /'
                           'vdmVyYWxsXCI6MS4wLFwiZmFjZVwiOjEuMCxcInZvaWNlXCI6MS4wfSIsI /'
                           'mV4cCI6MTU1MzAwMjI4MiwiaWF0IjoxNTUzMDAxNjgwfQ==.BxQtSa5H7x /'
                           'pEZ_n8xiyy1F1D-RiQDCDFGnucN6GCkmBKOwY0AxxNEl8TTN9wLNoYGBcE /'
                           'mD1RPNQhrDe45pHFgA=='
    }
    return data


def payload_callback_400_auth(sid):
    data = {
        'sid': f'{sid}'
    }
    return data


def payload_questionnaire_200(res_secret):
    data = {
        "resSecret": f"{res_secret}",
        "questions": [
            {
                "questionCode": "Q01",
                "answers": [
                    {
                        "answerCode": "Q01A01",
                        "answerValue": "1"
                    }
                ]
            },
            {
                "questionCode": "Q02",
                "answers": [
                    {
                        "answerCode": "Q02A01",
                        "answerValue": "0"
                    }
                ]
            },
            {
                "questionCode": "Q03",
                "answers": [
                    {
                        "answerCode": "Q03A01",
                        "answerValue": "1"
                    }
                ]
            },
            {
                "questionCode": "Q04",
                "answers": [
                    {
                        "answerCode": "Q04A01",
                        "answerValue": "0"
                    }
                ]
            },
            {
                "questionCode": "Q05",
                "answers": [
                    {
                        "answerCode": "Q05A01",
                        "answerValue": "1"
                    }
                ]
            }
        ]
    }
    return data


def payload_questionnaire_with_wrong_res_secret():
    data = {
        "resSecret": f"{uuid.uuid4()}",
        "questions": [
            {
                "questionCode": "Q01",
                "answers": [
                    {
                        "answerCode": "Q01A01",
                        "answerValue": "1"
                    }
                ]
            },
            {
                "questionCode": "Q02",
                "answers": [
                    {
                        "answerCode": "Q02A01",
                        "answerValue": "0"
                    }
                ]
            },
            {
                "questionCode": "Q03",
                "answers": [
                    {
                        "answerCode": "Q03A01",
                        "answerValue": "1"
                    }
                ]
            },
            {
                "questionCode": "Q04",
                "answers": [
                    {
                        "answerCode": "Q04A01",
                        "answerValue": "0"
                    }
                ]
            },
            {
                "questionCode": "Q05",
                "answers": [
                    {
                        "answerCode": "Q05A01",
                        "answerValue": "1"
                    }
                ]
            }
        ]
    }
    return data


def payload_questionnaire_with_empty_res_secret():
    data = {
        "resSecret": "",
        "questions": [
            {
                "questionCode": "Q01",
                "answers": [
                    {
                        "answerCode": "Q01A01",
                        "answerValue": "1"
                    }
                ]
            },
            {
                "questionCode": "Q02",
                "answers": [
                    {
                        "answerCode": "Q02A01",
                        "answerValue": "0"
                    }
                ]
            },
            {
                "questionCode": "Q03",
                "answers": [
                    {
                        "answerCode": "Q03A01",
                        "answerValue": "1"
                    }
                ]
            },
            {
                "questionCode": "Q04",
                "answers": [
                    {
                        "answerCode": "Q04A01",
                        "answerValue": "0"
                    }
                ]
            },
            {
                "questionCode": "Q05",
                "answers": [
                    {
                        "answerCode": "Q05A01",
                        "answerValue": "1"
                    }
                ]
            }
        ]
    }
    return data


def payload_questionnaire_without_res_secret():
    data = {
        "questions": [
            {
                "questionCode": "Q01",
                "answers": [
                    {
                        "answerCode": "Q01A01",
                        "answerValue": "1"
                    }
                ]
            },
            {
                "questionCode": "Q02",
                "answers": [
                    {
                        "answerCode": "Q02A01",
                        "answerValue": "0"
                    }
                ]
            },
            {
                "questionCode": "Q03",
                "answers": [
                    {
                        "answerCode": "Q03A01",
                        "answerValue": "1"
                    }
                ]
            },
            {
                "questionCode": "Q04",
                "answers": [
                    {
                        "answerCode": "Q04A01",
                        "answerValue": "0"
                    }
                ]
            },
            {
                "questionCode": "Q05",
                "answers": [
                    {
                        "answerCode": "Q05A01",
                        "answerValue": "1"
                    }
                ]
            }
        ]
    }
    return data


def payload_questionnaire_400_answer_value(res_secret):
    data = {
        "resSecret": f"{res_secret}",
        "questions": [
            {
                "questionCode": "Q01",
                "answers": [
                    {
                        "answerCode": "Q01A01",
                        "answerValue": "2"
                    }
                ]
            },
            {
                "questionCode": "Q02",
                "answers": [
                    {
                        "answerCode": "Q02A01",
                        "answerValue": "0"
                    }
                ]
            },
            {
                "questionCode": "Q03",
                "answers": [
                    {
                        "answerCode": "Q03A01",
                        "answerValue": "1"
                    }
                ]
            },
            {
                "questionCode": "Q04",
                "answers": [
                    {
                        "answerCode": "Q04A01",
                        "answerValue": "0"
                    }
                ]
            },
            {
                "questionCode": "Q05",
                "answers": [
                    {
                        "answerCode": "Q05A01",
                        "answerValue": "1"
                    }
                ]
            }
        ]
    }
    return data


def payload_questionnaire_400_no_answers(res_secret):
    data = {
        "resSecret": f"{res_secret}",
        "questions": [
            {
                "questionCode": "Q01",
                "answers": [
                    {
                        "answerCode": "Q01A01",
                        "answerValue": "1"
                    }
                ]
            },
            {
                "questionCode": "Q02",
                "answers": [
                    {
                        "answerCode": "Q02A01",
                        "answerValue": "0"
                    }
                ]
            },
            {
                "questionCode": "Q03",
                "answers": [
                    {
                        "answerCode": "Q03A01",
                        "answerValue": "1"
                    }
                ]
            },
            {
                "questionCode": "Q04",
                "answers": [
                    {
                        "answerCode": "Q04A01",
                        "answerValue": "0"
                    }
                ]
            },
            {
                "questionCode": "Q05",
                "answers": []
            }
        ]
    }
    return data


def payload_questionnaire_400_no_question(res_secret):
    data = {
        "resSecret": f"{res_secret}",
        "questions": [
            {
                "questionCode": "Q01",
                "answers": [
                    {
                        "answerCode": "Q01A01",
                        "answerValue": "1"
                    }
                ]
            },
            {
                "questionCode": "Q02",
                "answers": [
                    {
                        "answerCode": "Q02A01",
                        "answerValue": "0"
                    }
                ]
            },
            {
                "questionCode": "Q03",
                "answers": [
                    {
                        "answerCode": "Q03A01",
                        "answerValue": "1"
                    }
                ]
            },
            {
                "questionCode": "Q04",
                "answers": [
                    {
                        "answerCode": "Q04A01",
                        "answerValue": "0"
                    }
                ]
            }
        ]
    }
    return data


common_json_headers = {'Content-Type': 'application/json', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br'}
