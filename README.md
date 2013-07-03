arzeit_server
=============

Provides RESTful API for ArZeit

API URLs
--------
All actions are performed as a user. Responses are JSON with the following structure:

```json
{
    "error": [true|false],
    "error_msg": "",
    "server_time": "2013-07-04 18:45:00.1",
    "username": "eric",
    "active_timer_id": 34,
    "data": {}
}
```

List of URLs
------------

```
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
```

