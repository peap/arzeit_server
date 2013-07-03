arzeit_server
=============

Provides RESTful API for ArZeit

API URLs
--------
All actions are performed as a user. Responses are JSON with the following structure:
```javascript
{
    "error": [true|false],
    "error_msg": "",
    "server_time": "2013-07-04 18:45:00.1",
    "username": "eric",
    "data": {},
}
```

List of URLs
------------

timers/
timers/{id}/
timers/{id}/start/
timers/{id}/stop/

timers/{id}/intervals/
timers/{id}/intervals/{id}/
timers/{id}/intervals/tags/
timers/{id}/intervals/tags/{id}/

timers/{id}/totals/year/{year}/
timers/{id}/totals/month/{year}/{month}/
timers/{id}/totals/week/{year}/{week}/
timers/{id}/totals/day/{year}/{month}/{day}/

categories/
categories/{id}/

categories/{id}/totals/year/{year}/
categories/{id}/totals/month/{year}/{month}/
categories/{id}/totals/week/{year}/{week}/
categories/{id}/totals/day/{year}/{month}/{day}/

URL Table (to be completed...)
------------------------------

| URL                      | Method | action                 | data                         |
| ----------------         | :----: | ---------------------- | ---------------------------- |
| timers/                  | GET    | get list of timers     | {[{name, category_id}, ...]} |
| "   "                    | POST   | create new timer       | {name, category_id}          |
| timers/{id}/             | GET    | get timer info         | {name, category_id}          |
| "   "                    | PUT    | update timers          | |
| "   "                    | DELETE | delete timers          | |
| timers/{id}/start/       | POST   | start timer            | |
| timers/{id}/stop/        | POST   | stop timer             | |
| timers/{id}/today/       | GET    | get total for today    | |
| timers/{id}/total/{year}/[{month}/[{day}/] | GET    | get total for today    | |
| timers/{id}/total/week/{week}/ | GET    | get total for today    | |
| categories/              | GET    | get list of categories | |
| "   "                    | POST   | create new category    | |
| categories/{id}/         | GET    | get category           | |
| "   "                    | PUT    | update category        | |
| "   "                    | DELETE | delete category        | |

