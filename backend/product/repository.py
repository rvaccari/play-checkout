from typing import List

from backend.product.domains import Product


class ProductNotFoundException(Exception):
    """Product not found exception."""


class ProductRepository:
    def __init__(self):
        self.products = [
            Product(
                **{
                    "id": 1,
                    "title": "Ergonomic Wooden Pants",
                    "description": "Deleniti beatae porro.",
                    "amount": 15157,
                    "is_gift": False,
                }
            ),
            Product(
                **{
                    "id": 2,
                    "title": "Ergonomic Cotton Keyboard",
                    "description": "Iste est ratione excepturi repellendus adipisci qui.",
                    "amount": 93811,
                    "is_gift": False,
                }
            ),
            Product(
                **{
                    "id": 3,
                    "title": "Gorgeous Cotton Chips",
                    "description": "Nulla rerum tempore rem.",
                    "amount": 60356,
                    "is_gift": False,
                }
            ),
            Product(
                **{
                    "id": 4,
                    "title": "Fantastic Frozen Chair",
                    "description": "Et neque debitis omnis quam enim cupiditate.",
                    "amount": 56230,
                    "is_gift": False,
                }
            ),
            Product(
                **{
                    "id": 5,
                    "title": "Incredible Concrete Soap",
                    "description": "Dolorum nobis temporibus aut dolorem quod qui corrupti.",
                    "amount": 42647,
                    "is_gift": False,
                }
            ),
            Product(
                **{
                    "id": 6,
                    "title": "Handcrafted Steel Towels",
                    "description": "Nam ea sed animi neque qui non quis iste.",
                    "amount": 900,
                    "is_gift": True,
                }
            ),
        ]

    def all(self) -> List[Product]:
        return self.products

    def get_by_id(self, product_id: int) -> Product:
        for product in self.products:
            if product.id == product_id:
                return product

        raise ProductNotFoundException(f"Product {product_id} not found")
