import dramatiq
import requests
import sys

from dramatiq.brokers.redis import RedisBroker

redis_broker = RedisBroker(host="localhost", namespace="")
dramatiq.set_broker(redis_broker)

@dramatiq.actor(queue_name="pjq")
#@dramatiq.actor
def unified_push_notification_job_processor(post_msg):
    print(f"This was posted {post_msg}")

@dramatiq.actor(queue_name="pjq")
def handle(post_msg):
    print(f"This was posted HANDLE {post_msg}")

def main():
    naam = sys.argv[1] if len(sys.argv)>1 else 'japie'
    output = unified_push_notification_job_processor.send({'naam': naam})
    print(f'zegt {output}')	

if __name__ == '__main__':
    main()
