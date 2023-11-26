import requests


def GetEscrowContainer(eid):
    url = ("https://api.sandbox.upland.me/developers-api/containers/" + str(eid))
    # print(url)

    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Basic MjMyOmVjMjFlZmZlLTYyZDktNDAzZi04MTc3LTEwODdjMWJlNmJjYw==',
      'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
    }

    response = requests.request("GET", url, headers=headers)
    data = response.json()

    # print(data)

    return data


# def run():
#     GetEscrowContainer(1885)
#
#
# run()