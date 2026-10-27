def booking_payload(firstname="Sasanka", lastname="Tester"):
    return {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-12-01", "checkout": "2026-12-05"},
        "additionalneeds": "Breakfast",
    }