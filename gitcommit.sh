#!/bin/bash
# GIT Commiter Script
#
# Usage: gitcommit.sh 'Description of Upload'
#
# Joel Leclerc

git commit -m "$@"
git push origin master
