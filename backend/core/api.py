from ninja import Router

router = Router()


@router.get("/health")
def get_health(request):
    return {"result": True}
