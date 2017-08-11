# Pack Command

A C extension to optimize Redis format for redis-py.

# PATCHED VERSION
This version is a fast patch by @WydD in order to be compatible with recent versions of redis-py and on py3.
It does not support encoding other than utf-8 and may be improved upon. Code is directly ported from the dead PR in
https://github.com/andymccurdy/redis-py/pull/372 by the creator of credis @yihuang. It was mostly done for internal
purposes.

Fact of the matter is: a MGET with 1000 keys cpu cost is roughly divided by 40.

# Usage

```python
import redis
import pack_command

class MyConnection(redis.Connection):
    pack_command = pack_command.pack_command

pool = redis.ConnectionPool(connection_class=MyConnection)

conn = redis.StrictRedis(connection_pool=pool)
print conn.exists('foo')
```

# Note about redis-py version

Only works with redis-py>=2.10 with py3
