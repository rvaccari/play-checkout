from ninja import NinjaAPI

from backend.checkout.api_v1 import router as checkout_router_v1
from backend.core.api import router as core_router

api = NinjaAPI()

api.add_router("/", core_router)
api.add_router("checkout/api/v1/", checkout_router_v1)
