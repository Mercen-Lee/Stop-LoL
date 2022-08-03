from requests import get

summoners = {'검든호랑나비': '우영기 본계', '3성조이스틱': '강지석 본계', '일단원딜은못함': '강지석 부계'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
urlformatter = 'https://www.op.gg/_next/data/J6N7Pij1G7XQlWv8mgCoi/summoners/kr/%s.json?region=kr&summoner=%s'

print('\n마지막 플레이 시간\n')

try:
    for summoner in list(summoners.keys()):
        url = urlformatter % (summoner, summoner)
        latestplay = get(url, headers=headers).json()['pageProps']['games']['data'][0]['created_at']
        print(summoners[summoner] + ': ' + latestplay[:-9].replace('T', ' '))
    print('\n불러오기 성공\n')
    
except:
    print('불러오기 실패\n')
