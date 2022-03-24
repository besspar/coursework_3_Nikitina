import pytest

from project.dao.models import Director


class TestGenresView:
    url = "/directors/"

    @pytest.fixture
    def director(self, db):
        d = Director(name="Тейлор Шеридан")
        db.session.add(d)
        db.session.commit()
        return d

    def test_get_director(self, client, director):
        response = client.get(self.url)
        assert response.status_code == 200
        assert response.json == [
            {"id": director.id, "name": director.name},
        ]


class TestDirectorView:
    url = "/director/{director_id}"

    @pytest.fixture
    def director(self, db):
        d = Director(name="Тейлор Шеридан")
        db.session.add(d)
        db.session.commit()
        return d

    def test_get_director(self, client, director):
        response = client.get(self.url.format(director_id=director.id))
        assert response.status_code == 200
        assert response.json == {"id": director.id, "name": director.name}

    def test_director_not_found(self, client):
        response = client.get(self.url.format(director_id=1))
        assert response.status_code == 404
