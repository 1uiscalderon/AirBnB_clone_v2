#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static
apt-get update
apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "Testing" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/listen 80 default_server;/a \ \tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n}" /etc/nginx/sites-available/default
service nginx restart
