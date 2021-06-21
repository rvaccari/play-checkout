from unittest import mock

from backend.external_services.discount.client import request_discount


class TestDiscountClient:

    # TODO Create a decent test
    def test_request_discount(self):
        discount = request_discount(1)
        assert discount == 0
