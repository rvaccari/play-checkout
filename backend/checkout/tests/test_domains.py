from backend.checkout.domains import Checkout, Product


class TestProductDomain:
    def test_create_product_without_discount(self):
        product = Product(id=1, quantity=1, unit_amount=100, discount=0, is_gift=False)
        assert product.quantity == 1
        assert product.unit_amount == 100
        assert product.discount == 0
        assert product.total_amount == 100

    def test_create_product_with_discount(self):
        product = Product(id=1, quantity=2, unit_amount=100, discount=30, is_gift=False)
        assert product.quantity == 2
        assert product.unit_amount == 100
        assert product.discount == 30
        assert product.total_amount == 200

    def test_create_product_with_a_gift(self):
        product = Product(id=1, quantity=1, unit_amount=100, discount=30, is_gift=True)
        assert product.quantity == 1
        assert product.unit_amount == 0
        assert product.discount == 0
        assert product.total_amount == 0


class TestCheckoutDomain:
    def test_create_checkout_without_product_the_totals_must_be_zero(self):
        checkout = Checkout()
        assert len(checkout.products) == 0
        assert checkout.total_amount == 0
        assert checkout.total_amount_with_discount == 0
        assert checkout.total_discount == 0

    def test_create_checkout_domain_with_one_product_without_discount(self):
        checkout = Checkout()

        product = Product(id=1, quantity=1, unit_amount=100, discount=0, is_gift=False)
        checkout.add_product(product)

        assert len(checkout.products) == 1
        assert checkout.total_amount == 100
        assert checkout.total_amount_with_discount == 100
        assert checkout.total_discount == 0

    def test_create_checkout_domain_with_two_products_with_discount(self):
        checkout = Checkout()

        checkout.add_product(Product(id=1, quantity=2, unit_amount=150, discount=50, is_gift=False))
        checkout.add_product(Product(id=2, quantity=1, unit_amount=100, discount=0, is_gift=False))

        assert len(checkout.products) == 2
        assert checkout.total_amount == 400
        assert checkout.total_amount_with_discount == 350
        assert checkout.total_discount == 50

    def test_create_checkout_domain_with_a_gift(self):
        checkout = Checkout()

        checkout.add_product(Product(id=1, quantity=2, unit_amount=150, discount=50, is_gift=False))
        checkout.add_product(Product(id=2, quantity=1, unit_amount=100, discount=0, is_gift=True))

        assert len(checkout.products) == 2
        assert checkout.total_amount == 300
        assert checkout.total_amount_with_discount == 250
        assert checkout.total_discount == 50
