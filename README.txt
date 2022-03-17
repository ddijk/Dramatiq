https://medium.com/wealthy-bytes/the-easiest-way-to-use-a-python-virtual-environment-with-git-401e07c39cde

# Start workers
dramatiq count_words

# start client
python    # start console
from count_words import count_words
count_words.send("https://www.google.com")

