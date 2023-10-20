import requests
import json

def transmissao(id):
    try:
        urlpegartv = f"http://mobileapi.365scores.com/Data/Games/GameCenter/?apptype=1&appversion=5.8.22&games={id}&lang=31&oddsformat=1&shownaodds=true&storeversion=5.8.22&theme=dark&topbm=53&tz=93&uc=21&withexpanded=true&withexpandedstats=true&withnews=true"
        req_tvs = requests.get(urlpegartv)
        req_tra = json.loads(req_tvs.text)

        bodyTra = req_tra['TVNetworks']
        #print(bodyTra)
        
        url_att = req_tra['Games'][0]['PlayByPlayFeedURL']
        names = [item['Name'] for item in bodyTra if item['Name'] != 'bet365']
        names = ", ".join(names)
        return {
            "transmissao": names,
            "atualizacao": url_att
        }
                

    except:
        return False
    
    
response = requests.get("http://mobileapi.365scores.com/Data/Games/?apptype=1&appversion=5.8.22&favoritecompetitions=7,11,17,25,35,102,113,115,116,389,572,613&lang=31&light=true&oddsformat=1&onlymajorgames=false&onlyontv=true&startdate=20%2F10%2F2023&enddate=20%2F10%2F2023&storeversion=5.8.22&theme=dark&tz=93&uc=21&sport=1")
response = json.loads(response.text)
games = response['Games']

for game in games:
    if game['SID'] == 1:
        id = game['ID']
        trans = transmissao(id)
        
        if trans != False:
            timeCasa = game['Comps'][0]['Name']
            timeFora = game['Comps'][1]['Name']
            print(f"{timeCasa} x {timeFora} - {trans['transmissao']}")

