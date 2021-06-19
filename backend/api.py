from ninja import NinjaAPI

from backend.core.api import router as core_router

api = NinjaAPI()

api.add_router("/", core_router)
