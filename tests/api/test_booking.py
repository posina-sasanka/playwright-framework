import pytest
from utils.test_data import booking_payload


@pytest.mark.api
def test_create_and_get_booking(api_context):
    payload = booking_payload()
    created = api_context.post("/booking", data=payload)
    assert created.ok
    body = created.json()
    booking_id = body["bookingid"]
    assert body["booking"]["firstname"] == payload["firstname"]

    fetched = api_context.get(f"/booking/{booking_id}")
    assert fetched.ok
    assert fetched.json()["lastname"] == payload["lastname"]


@pytest.mark.api
def test_update_booking(api_context, auth_token):
    booking_id = api_context.post("/booking", data=booking_payload()).json()["bookingid"]

    updated = booking_payload(firstname="Updated", lastname="Name")
    resp = api_context.put(
        f"/booking/{booking_id}",
        data=updated,
        headers={"Cookie": f"token={auth_token}"},
    )
    assert resp.ok
    assert resp.json()["firstname"] == "Updated"


@pytest.mark.api
def test_delete_booking(api_context, auth_token):
    booking_id = api_context.post("/booking", data=booking_payload()).json()["bookingid"]

    resp = api_context.delete(
        f"/booking/{booking_id}", headers={"Cookie": f"token={auth_token}"}
    )
    assert resp.status == 201  # this API returns 201 on delete

    assert api_context.get(f"/booking/{booking_id}").status == 404