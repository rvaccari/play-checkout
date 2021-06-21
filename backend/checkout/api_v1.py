import logging

from ninja import Router

from backend.checkout.builders import BasketBuilder
from backend.checkout.schemas import BasketSchemaIn, BasketSchemaOut
from backend.product.repository import ProductRepository

logger = logging.getLogger(__name__)

router = Router()


@router.post("/", response=BasketSchemaOut)
def index(request, basket_in: BasketSchemaIn):
    base_log_message = f"checkout.index:create_basket"
    logger.info(f"{base_log_message} - start")

    product_repository = ProductRepository()

    logger.info(f"{base_log_message} - call BasketBuilder")
    basket_builder = BasketBuilder(basket_in, product_repository)

    logger.info(f"{base_log_message} - end")

    return basket_builder.build()
