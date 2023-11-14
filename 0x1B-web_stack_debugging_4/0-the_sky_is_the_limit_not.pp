# Changes the request limit to 4096

exec { 'adjust_nginx_request_limit':
  command => 'sudo sed -i s/15/4096/ /etc/default/nginx',
  path    => ['/bin', '/usr/bin'],
}

# Restart Nginx service after adjusting the request limit
exec {'restart_nginx':
  command     => 'sudo service nginx restart',
  path        => ['/bin', '/usr/bin'],
}
