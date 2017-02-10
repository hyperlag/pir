#!/bin/bash
for i in $@;do
	irsend SEND_ONCE 3100 KEY_$i
	sleep .15
done
