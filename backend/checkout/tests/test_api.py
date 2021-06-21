from unittest import mock


@mock.patch("backend.checkout.builders.BasketBuilder.get_discount", return_value=0)
class TestCheckoutApiPost:
    def test_index_status_code_200(self, mocked_request_discount, client):
        payload = {"products": [{"id": 1, "quantity": 1}]}
        resp = client.post("/checkout/api/v1/", data=payload, content_type="application/json")
        assert resp.status_code == 200

    def test_index_buy_one_item_without_discounts(self, mocked_request_discount, client):
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
        assert mocked_request_discount.call_count == 1

    def test_index_buy_one_item_with_discount(self, mocked_request_discount, client):
        mocked_request_discount.return_value = 0.05000000074505806
        payload = {"products": [{"id": 1, "quantity": 1}]}
        resp = client.post("/checkout/api/v1/", data=payload, content_type="application/json")

        assert resp.json()["total_discount"] == 758
        assert mocked_request_discount.call_count == 1
