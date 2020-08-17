#!/usr/bin/env bash
#install nginx and folders in server
if ! which nginx > /dev/null 2>&1; then
    apt-get -y update
    apt-get -y install nginx
    ufw allow 'Nginx HTTP'
fi
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/
echo "I am working" > /data/web_static/releases/test/index.html
rm -f /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/error_page/ i location /hbnb_static \{\n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
service nginx restart
