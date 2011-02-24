#!/bin/bash
# SVN Recursive file/directory adder
#
# Usage: ./svnradd.sh yourfile/dir
#
# Joel Leclerc

if [ -f "$1" ]
then
	svn add $1
fi

function rdirlsaddsvn() {
	for i in $1/*
	do
		if [ -e "$i" ]
		then
			if [ -d "$i" ]
			then
				echo -n "Adding directory $i... "
				svn add $i > /dev/null 2>&1
				if [ $? -eq 0 ]
				then
					echo "OK"
				else
					echo "FAIL"
				fi
				rdirlsaddsvn $i
			else
				echo -n "Adding file $i... "
				svn add $i > /dev/null 2>&1
				if [ $? -eq 0 ]
				then
					echo "OK"
				else
					echo "FAIL"
				fi
				echo "NOT $i" > /dev/null 2>&1
			fi
		fi
	done
}

rdirlsaddsvn $1
