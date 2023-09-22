# Create a manifest that kills a process named killmenow

exec { 'pkill killmenow':
  path    => ['/bin', '/usr/bin'],
  command => 'pkill killmenow',
}
