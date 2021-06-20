from dataclasses import dataclass


@dataclass
class Product:
    def __init__(self, id: int, quantity: int, unit_amount: int, discount: int, is_gift: bool):
        self.id = id
        self.quantity = quantity
        self.is_gift = is_gift
        if is_gift:
            self.unit_amount = 0
            self.discount = 0
            self.total_amount = 0
        else:
            self.unit_amount = unit_amount
            self.discount = discount
            self.total_amount = unit_amount * quantity

    id: int
    quantity: int
    unit_amount: int
    total_amount: int
    discount: int
    is_gift: bool


@dataclass
class Checkout:
    def __init__(self):
        self.products = []
        self.total_amount = 0
        self.total_amount_with_discount = 0
        self.total_discount = 0

    total_amount: int
    total_amount_with_discount: int
    total_discount: int
    products: list[Product]

    def add_product(self, product: Product):
        self.total_amount += product.total_amount
        self.total_amount_with_discount += product.total_amount - product.discount
        self.total_discount += product.discount
        self.products.append(product)
