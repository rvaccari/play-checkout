from django.test import Client


def test_health(client: Client):
    resp = client.get("/health")
    assert resp.status_code == 200
