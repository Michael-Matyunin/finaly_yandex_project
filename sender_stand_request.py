import confirutation

import requests

import data


# создать заказ

def post_create_order(order_body):
    header_copy = data.headers.copy()
    return requests.post(confirutation.URL_SERVICE + confirutation.CREATE_ORDER_PATH,
                         json=order_body,
                         headers=header_copy)

# получить заказ по треку
def get_track_order(params):
    return requests.get(
        confirutation.URL_SERVICE + confirutation.GET_ORDER_TRACK,
        headers=data.headers,
        params=params
    )
