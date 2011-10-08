gevent-redis
========

Asynchronous [Redis](http://redis-db.com/) client that works within [Gevent](http://www.gevent.org/).


Usage
-----

    >>> import geventredis
    >>> redis_client = geventredis.connect('127.0.0.1', 6379)
    >>> redis_client.set('foo', 'bar')
    'OK'
    >>> for msg in redis_client.monitor():
           print msg
    OK
    1318055499.218114 "monitor"
    _

Credits
-------
gevent-redis is developed and maintained by [Phus Lu](mailto:phus.lu@gmail.com)

 * Inspiration: [tornado-redisclient](https://github.com/phus/tornado-redisclient)


License
-------
Apache License, Version 2.0

