class TestAlticciSequenceTermView:
    def test_endpoint(self, client):
        term = 8
        value = 5

        expected_json = {
            "term": term,
            "value": value,
        }

        response = client.get(f"alticci/{term}")

        assert response.status_code == 200
        assert response.json == expected_json

    def test_wrong_request(self, client):
        term = 'a'

        response = client.get(f"alticci/{term}")

        assert response.status_code == 404

        term = 8

        response = client.post(f"alticci/{term}")

        response.status_code == 405
