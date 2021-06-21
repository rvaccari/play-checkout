from backend.checkout.domains import Basket, Product


class TestProductDomain:
    def test_create_product_without_discount(self):
        product = Product(id=1, quantity=1, unit_amount=100, discount_percentage=0, is_gift=False)
        assert product.quantity == 1
        assert product.unit_amount == 100
        assert product.discount == 0
        assert product.total_amount == 100

    def test_create_product_with_discount(self):
        product = Product(id=1, quantity=2, unit_amount=100, discount_percentage=0.30, is_gift=False)
        assert product.quantity == 2
        assert product.unit_amount == 100
        assert product.discount == 60
        assert product.total_amount == 200

    def test_create_product_with_a_gift(self):
        product = Product(id=1, quantity=1, unit_amount=100, discount_percentage=30, is_gift=True)
        assert product.quantity == 1
        assert product.unit_amount == 0
        assert product.discount == 0
        assert product.total_amount == 0


class TestBasketDomain:
    def test_create_basket_without_product_the_totals_must_be_zero(self):
        basket = Basket()
        assert len(basket.products) == 0
        assert basket.total_amount == 0
        assert basket.total_amount_with_discount == 0
        assert basket.total_discount == 0

    def test_create_basket_domain_with_one_product_without_discount(self):
        basket = Basket()

        product = Product(id=1, quantity=1, unit_amount=100, discount_percentage=0, is_gift=False)
        basket.add_product(product)

        assert len(basket.products) == 1
        assert basket.total_amount == 100
        assert basket.total_amount_with_discount == 100
        assert basket.total_discount == 0

    def test_create_basket_domain_with_two_products_with_discount(self):
        basket = Basket()

        basket.add_product(Product(id=1, quantity=2, unit_amount=150, discount_percentage=0.12, is_gift=False))
        basket.add_product(Product(id=2, quantity=1, unit_amount=100, discount_percentage=0, is_gift=False))

        assert len(basket.products) == 2
        assert basket.total_amount == 400
        assert basket.total_amount_with_discount == 364
        assert basket.total_discount == 36

    def test_create_basket_domain_with_a_gift(self):
        basket = Basket()

        basket.add_product(Product(id=1, quantity=2, unit_amount=150, discount_percentage=0.10, is_gift=False))
        basket.add_product(Product(id=2, quantity=1, unit_amount=100, discount_percentage=0, is_gift=True))

        assert len(basket.products) == 2
        assert basket.total_amount == 300
        assert basket.total_amount_with_discount == 270
        assert basket.total_discount == 30
