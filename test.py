from item_info import get_name_and_price
from max_min import get_max_min_money
from ranking import get_genre_ranking

def test_item_info():
    keyword = "PS5"
    resp = get_name_and_price(keyword)
    assert resp['Items'][0]['Item']['itemName']
    assert resp['Items'][0]['Item']['itemPrice']

def test_max_min():
    keyword = "PS5"
    resp = get_max_min_money(keyword)
    assert resp['Products'][0]['Product']['minPrice']
    assert resp['Products'][0]['Product']['maxPrice']

def test_ranking():
    genreId = 100283
    resp = get_genre_ranking(genreId)
    assert resp['Items'][0]['Item']['rank']




