class TestAlticciSequenceTermView:
    def test_endpoint(self, client):
        term = 8
        value = 5

        expected_json = {
            "term": term,
            "value": value,
        }

        response = client.get(f"/alticci/{term}")

        assert response.status_code == 200
        assert response.json == expected_json

    def test_wrong_request(self, client):
        term = 'a'

        response = client.get(f"/alticci/{term}")

        assert response.status_code == 404

        term = 8

        response = client.post(f"/alticci/{term}")

        response.status_code == 405


class TestAlticciSequenceTermListView:
    def test_endpoint(self, client):
        first_term = 5
        last_term = 7

        expected_json = [
            {
                "term": 5,
                "value": 2,
            },
            {
                "term": 6,
                "value": 3,
            },
            {
                "term": 7,
                "value": 4,
            }
        ]

        response = client.get(f"/alticci/{first_term}/{last_term}")

        assert response.status_code == 200
        assert response.json == expected_json

    def test_bad_order(self, client):
        first_term = 7
        last_term = 5

        response = client.get(f"/alticci/{first_term}/{last_term}")

        assert response.status_code == 400

    def test_wrong_request(self, client):
        term = 'a'

        response = client.get(f"/alticci/{term}/{term}")

        assert response.status_code == 404

        first_term = 8
        last_term = 10

        response = client.post(f"/alticci/{first_term}/{last_term}")

        response.status_code == 405
