#Fix an Apache that is returning a 500 error

exec {'fix-wordpress':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
