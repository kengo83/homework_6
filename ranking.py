import requests
import pandas as pd

API_Endpoint = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'
ApplicationId = 1089791896465980338

def get_genre_ranking(genreId):
    rank_list = []
    name_list = []
    price_list = []
    url_list = []
    params = {
        'applicationId': ApplicationId,
        'format':'json',
        'genreId':genreId
    }
    r = requests.get(API_Endpoint, params=params)
    resp = r.json()
    title = resp['title']
    print(f'ランキングタイトル:{title}')
    for i in resp['Items']:
        item = i['Item']
        rank = item['rank']
        rank_list.append(str(rank))
        name = item['itemName']
        name_list.append(str(name))
        price = item['itemPrice']
        price_list.append(str(price))
        url = item['itemUrl']
        url_list.append(str(url))
        print('[rank]' + str(rank))
        print('[name]' + str(name))
        print('[price]' + str(price))
        print('[url]' + str(url))

    df = pd.DataFrame(
        {"ランク": rank_list,
        "商品名": name_list,
        "価格": price_list,
        "商品URL": url_list,
        })
    
    df.to_csv('ranking.csv')

    return resp

if __name__ == "__main__":
    genreId = input("ジャンルIDを入力してください >>> ")
    get_genre_ranking(genreId)