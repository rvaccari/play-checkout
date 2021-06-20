from ninja import Schema


class ProductSchemaIn(Schema):
    id: int
    quantity: int


class CheckoutSchemaIn(Schema):
    products: list[ProductSchemaIn]


class ProductSchemaOut(Schema):
    id: int
    quantity: int
    unit_amount: int
    total_amount: int
    discount: int
    is_gift: bool


class CheckoutSchemaOut(Schema):
    total_amount: int
    total_amount_with_discount: int
    total_discount: int
    products: list[ProductSchemaOut]
