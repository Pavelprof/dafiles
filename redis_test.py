import redis

# redis cash db
rc = redis.Redis(host='localhost', port=6379, db=0)

# redis mq db
rq = redis.Redis(host='localhost', port=6379, db=1)

# refresh redis redis db
# rc.flushdb()
# rq.flushdb()


# rc.setex('my_key', 20, 'Hello, Redis!')
# rc.setex('my_key1', 20, 'Hello, Redis!1')
#
print('data in cash')
for key in rc.scan_iter("*"):
    value = rc.get(key)
    print(f"{key}: {value}")

print(' ')

# rq.setex('my_key', 20, 'Hello, Redis!')
# rq.setex('my_key1', 20, 'Hello, Redis!1')

print('data in mq')
for key in rq.scan_iter("*"):
    print(key)