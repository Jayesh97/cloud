import sys
import subprocess
import os
import random

#22d8294d83dd4717b63b7fc2392f7e83

c1 = sys.argv[1]
ip1 = sys.argv[2]
c2 = sys.argv[3]
ip2 = sys.argv[4]

res = subprocess.check_output(["sudo","docker","inspect","--format","{{.State.Pid}}",c1])
pid1 = res.strip('\n')
res = subprocess.check_output(["sudo","docker","inspect","--format","{{.State.Pid}}",c2])
pid2 = res.strip('\n')
print("process id - "+c1+" - "+pid1)
print("process id - "+c2+" - "+pid2)

#creating veth pair
if1 = c1+c2+"_if1"
if2 = c1+c2+"_if2"
print("interface-1- "+if1+"\ninterface-2- "+if2)
res = subprocess.check_output(["sudo","ip","link","add",if1,"type","veth","peer","name",if2])

#apt get update
res = subprocess.check_output(["sudo","docker","exec","-it",c1,"apt-get","update"])
res = subprocess.check_output(["sudo","docker","exec","-it",c2,"apt-get","update"])

#apt get upgrade
res = subprocess.check_output(["sudo","docker","exec","-it",c1,"apt-get","-y","upgrade"])
res = subprocess.check_output(["s:r0udo","docker","exec","-it",c2,"apt-get","-y","upgrade"])

#install ip route2
res = subprocess.check_output(["sudo","docker","exec","-it",c1,"apt-get","-y","install","iproute2"])
res = subprocess.check_output(["sudo","docker","exec","-it",c2,"apt-get","-y","install","iproute2"])

#install iputils ping
res = subprocess.check_output(["sudo","docker","exec","-it",c1,"apt-get","-y","install","iputils-ping"])
res = subprocess.check_output(["sudo","docker","exec","-it",c1,"apt-get","-y","install","iputils-ping"])

#pushing veth pairs
res = subprocess.check_output(["sudo","ip","link","set","netns",pid1,"dev",if1,"up"])
res = subprocess.check_output(["sudo","ip","link","set","netns",pid2,"dev",if2,"up"])

#adding ip to interface
res = subprocess.check_output(["sudo","docker","exec","--privileged",c1,"ip","addr","add",ip1+'/24',"dev",if1])
res = subprocess.check_output(["sudo","docker","exec","--privileged",c2,"ip","addr","add",ip2+'/24',"dev",if2])


#sudo docker rm $(sudo docker container ls -aq)
#sudo docker exec --privileged n1 ip link del n1_if1

docker swarm init --advertise-addr 34.70.246.33 

    docker swarm join --token SWMTKN-1-3eclahii9eo0ajidyuplfpksq4r7lw9u3p70slmgpxg49beuic-1dtmtt30drzv0qvqyjdogyy79 35.225.85.177:2377

    docker service ls

    docker node ls


sudo docker service create --name my_web --replicas 3 --mount type=volume,source=vol1,destination=/usr/share/nginx/html--mount type=volume,source=vol2,destination=/usr/share/nginx/css --publish 8085:80 nginx-hw3

sudo docker run --name lb -v /home/jayes/cloud_computing/nginx.conf:/etc/nginx/conf.d/default.conf -d -p 9000:80 nginx


sudo docker service create --name lb --replicas 1 --mount type=bind,source=/home/jayes/cloud_computing/nginx.conf,destination=/etc/nginx/conf.d/default.conf -d -p 9000:80 nginx


docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -itd mysql:tag

docker volume create vol1

sudo docker run --name n2 -itd --mount source=vol1,destination=/usr/share/nginx/html/ -p 6005:80 nginx

sudo apt-get install mysql\*

mysql -uroot -pmypassword -h127.0.0.1 -P 9000

34.70.246.33 

sudo docker run --name n1 -itd -v /home/jayes/cloud_computing/web1:/usr/share/nginx/html -p 9000:80 nginx


