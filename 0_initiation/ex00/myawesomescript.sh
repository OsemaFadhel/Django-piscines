#!/bin/sh

if [ -z "$1" ]; then
	echo "Usage: ./myawesomescript.sh <bit.ly/...>"
	exit 1
elif [ $# -gt 1 ]; then
	echo "Usage: ./myawesomescript.sh <bit.ly/...>"
	exit 1
fi

curl -s -o /dev/null -w "%{url_effective}\n" -L $1
