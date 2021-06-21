from backend.checkout.domains import Product, Basket
from backend.checkout.schemas import BasketSchemaIn
from backend.external_services.discount.client import request_discount
from backend.product.repository import ProductRepository


class BasketBuilder:
    def __init__(self, basket_in: BasketSchemaIn, product_repository: ProductRepository):
        self.product_repository = product_repository
        self.basket_in = basket_in
        self.__reset()

    def __reset(self):
        self.basket = Basket()

    def get_discount(self, product_id: int) -> int:
        return round(request_discount(product_id), 3)

    def __create(self):
        for product_in in self.basket_in.products:
            product_domain = self.product_repository.get_by_id(product_in.id)
            discount = self.get_discount(product_domain.id)
            product = Product(
                id=product_in.id,
                quantity=product_in.quantity,
                unit_amount=product_domain.amount,
                discount_percentage=discount,
                is_gift=product_domain.is_gift,
            )
            self.basket.add_product(product)

    def build(self) -> Basket:
        self.__create()

        return self.basket
