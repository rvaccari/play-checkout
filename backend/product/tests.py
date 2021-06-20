import pytest

from backend.product.repository import ProductRepository, ProductNotFoundException


class TestRepository:
    @pytest.fixture
    def product_repository(self):
        return ProductRepository()

    def test_get_all_products(self, product_repository):
        assert product_repository.all()

    def test_get_by_id_success(self, product_repository):
        assert product_repository.get_by_id(1)

    def test_product_not_found_exception(self, product_repository):
        with pytest.raises(ProductNotFoundException, match=r".* 0 .*"):
            assert product_repository.get_by_id(0)
