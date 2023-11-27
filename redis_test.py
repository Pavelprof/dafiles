import redis

# redis cash db
# r = redis.Redis(host='localhost', port=6379, db=0)
#
# r.setex('my_key', 20, 'Hello, Redis!')
# r.setex('my_key1', 20, 'Hello, Redis!1')
#
# for key in r.scan_iter("*"):
#     print(key)

# redis mq db
r = redis.Redis(host='localhost', port=6379, db=1)

# r.setex('my_key', 20, 'Hello, Redis!')
# r.setex('my_key1', 20, 'Hello, Redis!1')

for key in r.scan_iter("*"):
    print(key)