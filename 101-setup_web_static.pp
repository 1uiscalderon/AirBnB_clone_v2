# Configure an Nginx server using Puppet instead of Bash

package { 'nginx':
  ensure => installed,
}
exec { 'Setup':
  command  => 'sudo mkdir -p /date/web_static/releases/test
  sudo mkdir -p /data/web_static/shared
  sudo echo "Testing" | sudo tee /data/web_static/releases/test/index.html
  sudo ln -sf /data/web_static/releases/test /data/web_static/current
  sudo chown -R ubuntu:ubuntu /data/
  sed -i "/listen 80 default_server;/a \ \tlocation \/hbnb_static {\n\t\talias 
  \/data\/web_static\/current\/;\n}" /etc/nginx/sites-available/default
  sudo service nginx restart',
  provider => 'shell'
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
