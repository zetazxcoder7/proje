import re
import json

games = ['{"id": 3864596, "home": "Al-Taawoun", "away": "Al-Ittihad", "slogan": "Al-Taawoun x Al-Ittihad", "camp": "Campeonato Saudita", "transmissao": {"transmissao": "BANDSPORT", "atualizacao": "http://pbpgenerator.365scores.com/api/playbyplay/getcomments?fixtureid=6u7x8uxs65hx92b2yq7uyttsk&sportifiergameid=3864596&lang=31&isLive=False&IsFinished=true"}, "data": "12:00"}', '{"id": 3847724, "home": "Dortmund", "away": "Werder Bremen", "slogan": "Dortmund x Werder Bremen", "camp": "Campeonato Alem\\u00e3o", "transmissao": {"transmissao": " SporTV, Canal GOAT", "atualizacao": "http://pbpgenerator.365scores.com/api/playbyplay/getcomments?fixtureid=5nma3vd97knwd9zxdwy31l7h0&sportifiergameid=3847724&lang=31&isLive=False&IsFinished=true"}, "data": "15:30"}', '{"id": 3832761, "home": "Osasuna", "away": "Granada", "slogan": "Osasuna x Granada", "camp": "Campeonato Espanhol", "transmissao": {"transmissao": "STAR+", "atualizacao": "http://pbpgenerator.365scores.com/api/playbyplay/getcomments?fixtureid=6dkc06e317cpuoez0w07oefo&sportifiergameid=3832761&lang=31&isLive=False&IsFinished=true"}, "data": "16:00"}', '{"id": 3845345, "home": "Le Havre", "away": "Lens", "slogan": "Le Havre x Lens", "camp": "Campeonato Franc\\u00eas", "transmissao": {"transmissao": "STAR+", "atualizacao": "http://pbpgenerator.365scores.com/api/playbyplay/getcomments?fixtureid=hdp24i1hva1ot6c0d0jealn8&sportifiergameid=3845345&lang=31&isLive=False&IsFinished=true"}, "data": "16:00"}', '{"id": 3753813, "home": "Sampaio Corr\\u00eaa", "away": "Vit\\u00f3ria", "slogan": "Sampaio Corr\\u00eaa x Vit\\u00f3ria", "camp": "Brasileiro - S\\u00e9rie B", "transmissao": {"transmissao": " SporTV, Premiere", "atualizacao": "http://pbpgenerator.365scores.com/api/playbyplay/getcomments?fixtureid=d1csdhk409k79ecg97ocot4wk&sportifiergameid=3753813&lang=31&isLive=False&IsFinished=true"}, "data": "19:00"}', '{"id": 3753811, "home": "Mirassol", "away": "Guarani", "slogan": "Mirassol x Guarani", "camp": "Brasileiro - S\\u00e9rie B", "transmissao": {"transmissao": " SporTV, Premiere", "atualizacao": "http://pbpgenerator.365scores.com/api/playbyplay/getcomments?fixtureid=d0uoxvcq7a8y2nb2v08aj1afo&sportifiergameid=3753811&lang=31&isLive=False"}, "data": "21:30"}']

# Converte as strings JSON em dicionários Python
games = [json.loads(game_str) for game_str in games_str]


# Filtra os jogos da MLS que envolvem o Los Angeles FC
la_games = [game for game in games if not (game["camp"] == "Brasileiro - Série B" and "Guarani" not in game["slogan"])]

for game in la_games:
    print(game)
