# Django Assignment

## Technology Used

- Django
- DRF
- Python 3.0+
- This `django` service is deployed on `[render.com](http://render.com)` .
- Database Used - PostgreSQL

## Features Built

### `/bitcoin`

→ Gets the list of all the bitcoin prices fetched and saved into the database.

→ `HTTP Method` - GET

→ `Auth required` - **_NO_**

---

### `/bitcoin/fetch_bitcoin_price`

→ Fetches the latest bitcoin price and saves the bitcoin price into the database with the current timestamp.

→ `HTTP Method` - GET

→ `Auth required` - **_YES (User is required to be logged in.)_**

---

### `/user/register`

→ Registers the user into the database

→ `HTTP Method` - POST

→ Structure of the data used to create a user.

```json
{
	"username": "user",
	"email": "email@email.com",
	"password": "password"
}
```

---

### `/user/login`

→ User is logged in using this route.

→ A `JWT token` is returned in a `HTTP-ONLY COOKIE`

→ `HTTP Method` - POST

→ Structure of the data used to create a user.

```json
{
	"username": "user",
	"password": "password"
}
```

---

### `/user/logout`

→ User is logged out using this route.

→ `HTTP Method` - POST

---
