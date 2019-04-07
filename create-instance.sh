#!/usr/bin/env bash

instances=$1
node_type=$2
for instance_id in $(seq $instances)
do
	gcloud compute --project=chrome-ability-215704 \
	instances create $node_type-$instance_id --zone=asia-south1-c \
	--machine-type=n1-standard-2 --subnet=default \
	--network-tier=PREMIUM \
	--metadata=ssh-keys=eldo:ssh-rsa\ AAAAB3NzaC1yc2EAAAADAQABAAABAQDTsVTAeIiITpZ8egpb7dXJY6n02sGhIq9OAeDmUZvlxbXE4kRlIaKr4bHCz94Q\+Puf/2BHj77TLHp01HFrB2UMJPYSHErCV\+zclFrTljVKi4LF3CsJZAPA9WpGUIh4kEo2yy3nj1bvvcRyW0fP4uepuXdNAf3isuYXp53n4YwSDBxedmV42at5mj7P0KM7hUb/Tjpn9V59DL/FFk/5HMQkFPP/wWcuFIrXl9nSEpSY5eIhBXEawozELLxK7y8woDuv5Tc0NEsWAC917MzgTPk1IWhbmnJjnULMz7s8ok6vRwsDQLeH5j9SKkeCR8LolGPm2g1UI7fSXVVKxMWMHv3v\ eldo \
	--maintenance-policy=MIGRATE \
	--service-account=602780638703-compute@developer.gserviceaccount.com \
	--scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append \
	--image=centos-7-v20190312 --image-project=centos-cloud --boot-disk-size=10GB \
	--boot-disk-type=pd-standard --boot-disk-device-name=$node_type-$instance_id \
	--tags=mynodes
done
