from unittest import mock

from backend.checkout.builders import BasketBuilder
from backend.checkout.schemas import BasketSchemaIn


class TestBasketBuilder:
    @mock.patch("backend.checkout.builders.BasketBuilder.get_discount", return_value=0)
    @mock.patch("backend.product.repository.ProductRepository")
    def test_create_basket_when_basket_in_contains_two_item(self, mock_product_repository, mock_get_discount):
        basket_in = BasketSchemaIn(**{"products": [{"id": 1, "quantity": 1}, {"id": 2, "quantity": 1}]})
        builder = BasketBuilder(basket_in, mock_product_repository)
        basket = builder.build()
        assert len(basket.products) == 2
        assert mock_get_discount.call_count == 2
