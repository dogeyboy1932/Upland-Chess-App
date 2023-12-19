from Chess.test2 import Lichess


def test_stream():
    gameid="gIMf5rSl"
    lichess=Lichess(debug=True)
    # gameid=lichess.waitForChallenge()
    lichess.streamGame(gameid)

test_stream()

# import http.client
#
# conn = http.client.HTTPSConnection("api.sandbox.upland.me")
# payload = ''
# headers = {
#   'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI0ODI5OGVhMC0yNDBhLTExZWUtOWMwNC1iMzcyMDk2MTViOGIiLCJhcHBJZCI6MjMyLCJ0b2tlbklkIjoiZWY2MWEwY2MtMjgyMC00Y2FhLTkwODktOGZhMTdkY2EzMTY2IiwiaWF0IjoxNzAxNTUzMzY5fQ.0zKCRi2lxIsftkN_XdrB-tg_bY6hDLkltd3LRXDlNno',
#   'Cookie': 'sticky-session-1=1701556690.435.2069.742375|9a5cc3e4d08faea009d8e16f5c97bee9'
# }
# conn.request("GET", "/developers-api/user/profile", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))