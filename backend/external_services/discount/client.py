import logging

import grpc
from django.conf import settings

from backend.external_services.discount.discount_pb2 import GetDiscountRequest
from backend.external_services.discount.discount_pb2_grpc import DiscountStub

logger = logging.getLogger(__name__)


def request_discount(product_id: int) -> int:
    base_log_message = f"request_discount: product {product_id}"
    try:
        logger.info(f"{base_log_message} - start")
        with grpc.insecure_channel(settings.DISCOUNT_SERVICE_URL) as channel:
            stub = DiscountStub(channel)
            response = stub.GetDiscount(GetDiscountRequest(productID=product_id))
            logger.info(f"{base_log_message} - end")
            return response.percentage if response else 0
    except Exception as e:
        message = getattr(e, "message", None) or str(e)
        logger.error(f"{base_log_message} - Got {e.__class__.__name__} exception with message: {message}.")
        return 0
