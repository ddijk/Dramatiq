
Note: commands below assume that Redis is running on localhost on default port.

# Run test program to push to queue
`python push_worker.py some-data`

# Run worker that listens to queue
`python /Users/dick/Library/Python/3.8/bin/dramatiq -t 1 push_worker  --verbose`
`python /Users/dick/Library/Python/3.8/bin/dramatiq push_worker`

# Commands to reset state
## reset last channel post id
`bash reset_chpst_id.s`

## reset timestamp used by post_push_job
`bash reset_lut.sh`

# Show messages currently in queue
`bash log_messages.sh`

# Execute a Redis cli command
`bash cli.sh <command>` e.g.  `bash cli.sh KEYS \*`

## Venv
https://medium.com/wealthy-bytes/the-easiest-way-to-use-a-python-virtual-environment-with-git-401e07c39cde

# Dramatiq example
## Start workers
`dramatiq count_words`

## start client ( using Python REPL)
```
python    
from count_words import count_words 
count_words.send("https://www.google.com")
```
