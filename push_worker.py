import dramatiq
import requests
import sys

from dramatiq.brokers.redis import RedisBroker

redis_broker = RedisBroker(host="localhost")
dramatiq.set_broker(redis_broker)

@dramatiq.actor(queue_name="pjq")
#@dramatiq.actor
def unified_push_notification_job_processor(post_msg):
    print(f"This was posted {post_message}")

def main():
    naam = sys.argv[1] if len(sys.argv)>1 else 'japie'
    handle.send({'naam': naam})

if __name__ == '__main__':
    main()
