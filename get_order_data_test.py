# Михаил Матюнин 23-я когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data


# создать заказ
def create_order():
    response = sender_stand_request.post_create_order(data.order_body)
    new_order_track = response.json().get("track")
    return new_order_track


# базовая функция для проверки трека заказа
def positive_assert():
    order_track = create_order()
    params = {"t": order_track}
    response = sender_stand_request.get_track_order(params)

    assert response.status_code == 200


def test_get_order():
    positive_assert()
