#! /bin/bash

grep --include='*.py' --include='*.html' --include='*.txt' -Roh -e 'word(u*"[^"]*"[,)]' -e "word(u*'[^']*'[,)]" | sed -e 's/word(u*"\(.*\)"[,)]/"\1": Null/' -e "s/word(u*'\(.*\)'[,)]/\"\1\": Null/" | sort | uniq
