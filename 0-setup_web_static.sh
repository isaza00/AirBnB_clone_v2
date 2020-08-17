#!/usr/bin/env bash
#install nginx and folders in server
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/
echo "I am working" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
link_file="/data/web_static/current"
config="/etc/nginx/sites-enabled/default"
sed -i "11i \\\\tlocation /hbnb_static/ {\n\t\talias $link_file/;\n\t\tautoindex off;\n\t}\n" "$config"
service nginx restart
