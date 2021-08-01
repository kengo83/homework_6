import requests
from pprint import pprint

API_Endpoint = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
ApplicationId = 1089791896465980338

def get_name_and_price(keyword):
    params = {
        'keyword' : keyword,
        'applicationId': ApplicationId,
        'format':'json'
    }
    r = requests.get(API_Endpoint, params=params)
    resp = r.json()
    #pprint(resp)
    for i in resp['Items']:
        item = i['Item']
        name = item['itemName']
        print('[Name]'+ str(name))
        print('[Price]' + '￥' + str(item['itemPrice']))

    return resp

if __name__ == "__main__":
    keyword = input('検索キーワードを入力して下さい:')
    get_name_and_price(keyword)



    

