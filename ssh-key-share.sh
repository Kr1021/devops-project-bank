#!/bin/bash
# Script to share SSH keys securely with a remote server

USER=$1
HOST=$2

if [[ -z "$USER" || -z "$HOST" ]]; then
  echo "Usage: $0 <user> <host>"
  exit 1
fi

ssh-copy-id ${USER}@${HOST}
echo "SSH key has been copied successfully."
