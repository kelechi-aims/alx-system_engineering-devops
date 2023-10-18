#!/usr/bin/env bash
# Installs MySQL server version 5.7.x
#Save it in a file on your machine i.e. signature.key and then
sudo apt-key add './mysql-5.7_signature.key'
# add the apt repo
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'
# update apt
sudo apt-get update
# now check your available versions:
sudo apt-cache policy mysql-server
# Now install mysql 5.7
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
