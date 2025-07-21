import requests
from govesb import DataFormatEnum
from govesb.services.esb_helper import ESBHelper


destination_scheme = 'https'
destination_host = '0.0.0.0'
destination_port = '8080'
destination_path = 'api/receive-data'
destination_username = 'system-username'
destination_password = 'password'

destination_url = f'{destination_scheme}://{destination_host}:{destination_port}/{destination_path}'

govesb_public_key = 'MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEon0az66Kz+6ZIz4G7La8uPeSbOT/E/suRjNMgFQ4isjJwFXaS20vHcndEFxXz8M68sbxkbLrGuNS/wFcEzubWQ=='
system_private_key = 'MD4CAQAwEAYHKoZIzj0CAQYFK4EEAAoEJzAlAgEBBCA+WSlrAHLF9SVtOzHu1QucdBCOkxcaYnP0Pwyntw4vYA=='

sample_data = {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}

responseData = ESBHelper.verify_and_extract_data(str(sample_data), DataFormatEnum.JSON, govesb_public_key)

print('responseData', responseData)

if not responseData.has_data and responseData is None:
    body = ESBHelper.create_response('{}', DataFormatEnum.JSON, system_private_key, False, "Signature Verification Failed")
else:
    print('sample payload', responseData.verified_data)
    response = requests.post(url=destination_url, data=responseData.verified_data, auth=(destination_username, destination_password))

