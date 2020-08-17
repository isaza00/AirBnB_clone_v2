#!/usr/bin/env bash
#install nginx and folders in server

apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
service nginx start
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/
echo "I am working" > /data/web_static/releases/test/index.html
rm -f /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
grep -q "location /hbnb_static" /etc/nginx/sites-available/default || sed -i '/error_page/ i location /hbnb_static \{\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
service nginx restart
