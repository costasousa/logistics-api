from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_driver():
    response = client.post("/drivers/", json={
        "id": 1,
        "name": "Lucas",
        "place_veiculo": "ABCD-1234"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "lUCAS"

def test_list_drivers():
    response = client.get("/drivers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_delivery():
    response = client.post("/deliveries/", json={
        "id": 1,
        "package": "Notebook",
        "destination": "Rua X",
        "status": "pending"
    })
    assert response.status_code == 200
    assert response.json()["package"] == "Notebook"

def test_list_deliveries():
    response = client.get("/deliveries/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_assign_driver():
    # cria motorista e entrega primeiro
    client.post("/drivers/", json={
        "id": 2,
        "name": "Maria",
        "vehicle_plate": "DEF-5678"
    })
    client.post("/deliveries/", json={
        "id": 2,
        "package": "Documentos",
        "destination": "Rua Y",
        "status": "pending"
    })
    response = client.put("/deliveries/2/assign/2")
    assert response.status_code == 200
    assert response.json()["assigned_driver_id"] == 2

def test_update_delivery_status():
    response = client.put("/deliveries/2/status/in_transit")
    assert response.status_code == 200
    assert response.json()["status"] == "in_transit"