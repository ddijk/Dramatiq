https://medium.com/wealthy-bytes/the-easiest-way-to-use-a-python-virtual-environment-with-git-401e07c39cde

Note: commands below assume that Redis is running on localhost on default port.
# Start workers
dramatiq count_words

# start client
python    # start console
from count_words import count_words
count_words.send("https://www.google.com")

# Run test program to push to queue
python push_worker.py JAAP

# Run worker that listens to queue
python /Users/dick/Library/Python/3.8/bin/dramatiq -t 1 push_worker  --verbose
