arzeit_server
=============

Provides RESTful API for ArZeit

API URLs:
---------
All actions are performed as a user

| URL              | GET | POST | PUT | DELETE | result                 |
| ---------------- | :-: | :--: | :-: | :----: | ---------------------- |
| timers/          |  x  |      |     |        | get list of timers     |
| timers/          |     |  x   |     |        | create new timer       |
| timers/{id}/     |  x  |      |     |        | get timer              |
| timers/{id}/     |     |      |  x  |        | update timers          |
| timers/{id}/     |     |      |     |   x    | delete timers          |
| categories/      |  x  |      |     |        | get list of categories |
| categories/      |     |  x   |     |        | create new category    |
| categories/{id}/ |  x  |      |     |        | get category           |
| categories/{id}/ |     |      |  x  |        | update category        |
| categories/{id}/ |     |      |     |   x    | delete category        |

