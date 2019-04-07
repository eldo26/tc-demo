#!/usr/bin/env bash
instance_zone=`gcloud compute instances list |awk '{print $2}' |sed '1d' |head -1`
for instance_id in $(gcloud compute instances list |awk '{print $1}' |sed '1d')
do
	gcloud compute instances delete $instance_id --zone=$instance_zone --quiet
done