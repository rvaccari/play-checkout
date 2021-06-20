from ninja import Router

from backend.checkout.domains import Checkout, Product
from backend.checkout.schemas import CheckoutSchemaIn, CheckoutSchemaOut
from backend.product.repository import ProductRepository

router = Router()


@router.post("/", response=CheckoutSchemaOut)
def index(request, checkout_int: CheckoutSchemaIn):
    product_repository = ProductRepository()
    checkout = Checkout()

    for product_in in checkout_int.products:
        product_domain = product_repository.get_by_id(product_in.id)
        product = Product(
            id=product_in.id,
            quantity=product_in.quantity,
            unit_amount=product_domain.amount,
            discount=0,
            is_gift=product_domain.is_gift,
        )
        checkout.add_product(product)
    return checkout
