import requests
from pprint import pprint

API_Endpoint = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426'
ApplicationId = 1089791896465980338

def get_max_min_money(keyword):
    params = {
        'applicationId' : ApplicationId,
        'format':'json',
        'keyword':keyword
    }
    r = requests.get(API_Endpoint, params=params)
    resp = r.json()
    #pprint(resp)
    for i in resp['Products']:
        product = i['Product']
        name = product['productName']
        max_money = product['maxPrice']
        min_money = product['minPrice']
        print('[Name]'+ str(name))
        print('[max_price]'+ '￥' + str(max_money))
        print('[min_money]' + '￥' + str(min_money))

    return resp

if __name__=="__main__":
    keyword = input('検索キーワードを入力して下さい:')
    get_max_min_money(keyword)

