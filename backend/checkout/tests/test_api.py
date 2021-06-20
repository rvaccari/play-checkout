import json

import pytest


class TestCheckoutApiPost:
    def test_index_status_code_200(self, client):
        payload = {"products": [{"id": 1, "quantity": 1}]}
        resp = client.post("/checkout/api/v1/", data=payload, content_type="application/json")
        assert resp.status_code == 200

    def test_index_buy_one_item_without_discounts(self, client):
        payload = {"products": [{"id": 1, "quantity": 1}]}
        resp = client.post("/checkout/api/v1/", data=payload, content_type="application/json")

        expected = {
            "total_amount": 15157,
            "total_amount_with_discount": 15157,
            "total_discount": 0,
            "products": [
                {
                    "id": 1,
                    "quantity": 1,
                    "unit_amount": 15157,
                    "total_amount": 15157,
                    "discount": 0,
                    "is_gift": False,
                }
            ],
        }
        assert resp.json() == expected
