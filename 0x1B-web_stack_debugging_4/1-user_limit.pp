# Change the OS configuration so that it is possible to login with
# the holberton user and open a file without any error message.

exec { 'update_limits_5':
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  provider => shell,
}

exec { 'update_limits_4':
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
  provider => shell,
  require  => Exec['update_limits_5']
}
