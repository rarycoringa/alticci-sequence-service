class TestHello:
    def test_endpoint(self, client):
        response = client.get("hello/")

        assert response.status_code == 200
        assert response.json == {"message": "Hello world!"}

    def test_wrong_request(self, client):
        response = client.get("hello/not_found/")

        assert response.status_code == 404

        response = client.post("hello/")

        assert response.status_code == 405
