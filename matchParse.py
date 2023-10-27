from requests_html import HTMLSession
import requests
import pymysql


session = HTMLSession()
url = "https://www.opendota.com/matches/highMmr"
r = session.get(url)
r.html.render(sleep=1, keep_page=True, scrolldown=2, timeout=25)
matches_not_final = {}
r = r.html.links



try:
    connection = pymysql.connect(host='37.140.192.80',
                                 user='u0823922_codolo1',
                                 password='codologia1',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 database="u0823922_test")
    print("successfully...")
except Exception as ex:
    print("connection refused...")

matches = {}
t = 0
for i in r:
    if len(i) == 19:
        matches_not_final[t] = i[9:]
        t += 1
print(1)
print(len(matches_not_final))
for i in range(len(matches_not_final)):

        response = requests.get('https://api.opendota.com/api/matches/' + matches_not_final[i]).json()
        radiant = []
        dire = []
        if "picks_bans" in response:
            for j in range(len(response['picks_bans'])):
                if response['picks_bans'][j]["team"] == 0 and response["picks_bans"][j]["is_pick"] is True:
                    radiant.append(str(response["picks_bans"][j]["hero_id"]))
                elif response['picks_bans'][j]["team"] == 1 and response["picks_bans"][j]["is_pick"] is True:
                    dire.append(str(response["picks_bans"][j]["hero_id"]))
            sl = dict()
            radiant_str = ""
            dire_str = ""
            with open ("heroes.txt", "r") as f:
                s = f.read().split("\n")
                for row in s:
                    row = row.split(";")
                    sl[row[0]] = row[1]
            if "radiant_win" in response:
                radiantWin = response["radiant_win"]
            if radiantWin:
                radiantWin = 0
            else:
                radiantWin = 1
            if len(radiant) == 5 and len(dire) == 5:
                for j in range(5):
                    radiant[j] = sl[radiant[j]]
                    radiant_str += f"{radiant[j]} "
                for j in range(5):
                    dire[j] = sl[dire[j]]
                    dire_str += f"{dire[j]} "
                try:
                    with connection.cursor() as cursor:
                        id = response['match_id']
                        print(id)
                        insert_query = f"INSERT INTO `match1` (`ID_MATCH`, `RADIANT`, `DIRE`, `RADIANT_WIN`) " \
                                       f"VALUES ({id}, " \
                                       f"'{radiant_str}', '{dire_str}', '{radiantWin}');"
                        cursor.execute(insert_query)
                        connection.commit()
                        id = 0
                except Exception as ex:
                    print(ex)
                    print(radiant_str, dire_str)
            radiant = []
            dire = []
            radiantWin = None
            response = ""

print("END")