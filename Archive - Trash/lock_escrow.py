

def LockEscrow(eid, credential):
    url = "/containers/" + str(eid) + "/lock"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {credential}',
        'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
    }

    conn.request("POST", url, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


# url = "https://api.sandbox.upland.me/developers-api/containers/" + str(eid) + "/lock"
#
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': 'Basic MjMyOmVjMjFlZmZlLTYyZDktNDAzZi04MTc3LTEwODdjMWJlNmJjYw==',
#     'Cookie': 'sticky-session-1=1699553168.246.2069.619172|aebf5e9dc298523c710b3cfe411c6704'
# }
#
# requests.request("POST", url, headers=headers)