/opt/homebrew/Cellar/redis/6.2.6/bin/redis-cli KEYS \* | grep msgs | while read queue; do
    echo "queue $queue";
    /opt/homebrew/Cellar/redis/6.2.6/bin/redis-cli HGETALL $queue
    echo "===="
done
