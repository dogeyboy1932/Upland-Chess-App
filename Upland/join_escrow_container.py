import requests
import json
# from FIXED_VARIABLES import filepath
# from openpyxl import load_workbook
# from Upland.get_escrow_container import GetEscrowContainer
# from query_uplandID_index import QueryUplandIDRow
# from create_escrow_container import CreateEscrowContainer


def JoinEscrow(bearerToken, containerId, upxAmount):
    url = "https://api.sandbox.upland.me/developers-api/User/join"

    payload = json.dumps({
      "containerId": containerId,
      "upxAmount": upxAmount,
      "sparkAmount": 0,
      "assets": [],
    })

    bearer = 'Bearer ' + bearerToken
    # print(bearer)

    headers = {
      # 'Authorization': str(bearer),
      'Authorization': bearer,
      'Content-Type': 'application/json',
      'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def run():
    # eid = CreateEscrowContainer()
    # eid = 1902

    bearer = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI0ODI5OGVhMC0yNDBhLTExZWUtOWMwNC1iMzcyMDk2MTViOGIiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiZGYyYjM2ZGMtOGM3OS00NzcxLTljZWYtZWNlOThhZGFmMDYxIiwiaWF0IjoxNzAwOTY4MTIxfQ.iJmZdWkwsYDVx6ZzhhwA9i9ai26oq8-7CtJipDdh0wk'
    # bearer = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIwOTQ4ZGE1MC04N2Q0LTExZWUtYjBjMi02MzM4M2I3OTUzNjAiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiZmFlZjMzMmQtNGVlNy00ODAyLTljZGUtYjExNTBlM2U5ZWRhIiwiaWF0IjoxNzAwOTYwNTU0fQ.JuoXMTrzYsS3UJ5ALFaT2Zs3gqjxZXR41-WFh0UGi4I'

    # JoinEscrow(bearer, eid, 200)
    # print(GetEscrowContainer(eid))


run()






# def join_escrow(bearerToken, containerId, upxAmount):
#     url = "https://api.sandbox.upland.me/developers-api/User/join"
#
#     payload = {
#         "containerId": 1888,
#         "upxAmount": 100,
#         "sparkAmount": 0,
#         "assets": []
#     }
#
#     headers = {
#         'Authorization': f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI0ODI5OGVhMC0yNDBhLTExZWUtOWMwNC1iMzcyMDk2MTViOGIiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiN2U0NjUwZjctMzdiZi00OGFjLTlhYWQtNmRlOTczZmY2NGU2IiwiaWF0IjoxNzAwODYzNTYzfQ.JWrczdQvPABSKRgQxeCFhtaGlo3WhNaGWBZnb5FH_T8',
#         'Content-Type': 'application/json',
#         'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#
#     print(response.text)




# def run():
#     workbook = load_workbook(filepath)
#     worksheet = workbook['Sheet']
#
#     idx1 = QueryUplandIDRow("dogeyboy19")
#     # idx2 = QueryUplandIDRow("testact1112")
#
#     bearer1 = worksheet[idx1][4]
#     # bearer2 = worksheet[idx2][4]
#
#     # escrowId = CreateEscrowContainer()
#     # print(escrowId)
#
#     # join_escrow()
#     get_escrow()

    # join_escrow(bearer1, escrowId, 100)
    # join_escrow(bearer2, escrowId, 100)

    # print(worksheet[idx1][1].value)
    # print(worksheet[idx2][1].value)

    # print(bearer1.value)


    # upland_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI0ODI5OGVhMC0yNDBhLTExZWUtOWMwNC1iMzcyMDk2MTViOGIiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiNzMwZWU0ZGItNWVlNS00MGFmLTk3M2MtNTZlNzc3OTc3MTVjIiwiaWF0IjoxNzAwNzY4NzIyfQ.wxb8F5elHyCRCTlpGFbMfPAi8sd52EjqgUynrwYTAKA"
    # upland_user_id = "48298ea0-240a-11ee-9c04-b37209615b8b"

    # join_escrow()

# run()

# import requests

# import requests
# import json



# def join_escrow(containerID, upxAmount, bearer):
#     url = "https://api.sandbox.upland.me/developers-api/Users/join"
#
#     payload = json.dumps({
#         "containerId": containerID,
#         "upxAmount": upxAmount,
#         "sparkAmount": 0,
#         "assets": []
#     })
#     headers = {
#         'Authorization': f'Bearer {bearer}',
#         'Content-Type': 'application/json',
#         'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#
#     print(response.text)

# def join_escrow(upland_access_token, upland_user_id):
#     url = 'https://api.sandbox.upland.me/developers-api/user/join'
#
#     headers = {
#         'Authorization': f'Bearer {upland_access_token}',
#         'UserId': upland_user_id,
#     }
#
#     response = requests.post(url)
#     data = response.json()
#
#     if response.status_code == 200:
#         app_id = data['appId']
#
#         return "AppID:" f"{app_id}"
#     else:
#         print(f'Request failed with status code {response.status_code}')


# def run():
#     containerID = 1867
#     upxAmount = 100
#     upland_access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI0ODI5OGVhMC0yNDBhLTExZWUtOWMwNC1iMzcyMDk2MTViOGIiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiN2E1NjI1M2EtMjNiYi00ODUxLWJkZWYtMDFkZDIzMDQzYWNhIiwiaWF0IjoxNzAwNzY4Mjg0fQ.XMA6FYxRSb7X4rtlz0zeteY-aF9PyuPwRpP8mN_wQIE"
#
#     join_escrow(containerID, upxAmount, upland_access_token)
#
#
# run()












# def join_escrow(upland_access_token, upland_user_id):
#     url = 'https://api.sandbox.upland.me/developers-api/user/join'
#
#     headers = {
#         'Authorization': f'Bearer {upland_access_token}',
#         'UserId': upland_user_id,
#     }
#
#     response = requests.post(url)
#     data = response.json()
#
#     if response.status_code == 200:
#         app_id = data['appId']
#
#         return "AppID:" f"{app_id}"
#     else:
#         print(f'Request failed with status code {response.status_code}')
