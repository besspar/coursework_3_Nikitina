from unittest.mock import Mock, patch

import pytest

from project.dao.models import Director
from project.exceptions import ItemNotFound
from project.schemas.director import DirectorSchema
from project.services import DirectorsService


class TestDirectorsService:
    @pytest.fixture(autouse=True)
    def service(self, db):
        self.service = DirectorsService(db.session)

    @pytest.fixture
    def director(self):
        return Director(id=1, name="director_1")

    @pytest.fixture
    def director_dao_mock(self, director):
        with patch("project.services.directors_service.DirectorDAO") as mock:
            mock.return_value = Mock(
                get_by_id=Mock(return_value=DirectorSchema().dump(director)),
                get_all=Mock(return_value=DirectorSchema(many=True).dump([director])),
            )
            yield mock

    def test_get_all_directors(self, director_dao_mock, director):
        assert self.service.get_all_directors() == DirectorSchema(many=True).dump([director])
        director_dao_mock().get_all.assert_called_once()

    def test_get_item_by_id(self, director_dao_mock, director):
        assert self.service.get_item_by_id(director.id) == DirectorSchema().dump(director)
        director_dao_mock().get_by_id.assert_called_once_with(director.id)

    def test_get_item_by_id_not_found(self, director_dao_mock):
        director_dao_mock().get_by_id.return_value = None

        with pytest.raises(ItemNotFound):
            self.service.get_item_by_id(1)
