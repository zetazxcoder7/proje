import requests
import json
import datetime
import re

def hora(data):
    dt = datetime.datetime.fromisoformat(data)
    hora = dt.hour
    minuto = dt.minute
    hora_formatada = f"{hora:02d}"
    minuto_formatado = f"{minuto:02d}"

    # Exibir o resultado
    return f"{hora_formatada}:{minuto_formatado}"


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
    
def jogos():
    response = requests.get("https://webws.365scores.com/web/games/myscores/?appTypeId=5&langId=31&timezoneName=America/Fortaleza&userCountryId=323&competitions=6071,5096,113,572,115,102,11,7,116,114,389,573,13,17,595,35,25,332,73,104,649,5501,6164,76,10,15,6316,23,37&competitors=1267&startDate=20/10/2023&endDate=20/10/2023&showOdds=true&withSuggested=true")
    response = json.loads(response.text)
    games = response['games']

    games_str = []
    for game in games:
        if game['sportId'] == 1:
            id = game['id']
            trans = transmissao(id)
            
            if trans != False:
                diajogo = game['startTime']
                diajogo = hora(diajogo)
                timeCasa = game['homeCompetitor']['name']
                timeFora = game['awayCompetitor']['name']
                comp = game['competitionDisplayName']
                sla = json.dumps({
                    "id": id,
                    "home": timeCasa,
                    "away": timeFora,
                    "slogan": f"{timeCasa} x {timeFora}",
                    "camp": comp,
                    "transmissao": trans,
                    "data": diajogo
                })
                games_str.append(sla)

    games = [json.loads(game_str) for game_str in games_str]
    games = [game for game in games if not (game["camp"] == "MLS" and "Inter Miami" not in game["slogan"])]
    
    return games
        



