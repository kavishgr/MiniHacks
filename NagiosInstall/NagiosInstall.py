from os import system as sh
#import subprocess as sp
from requests import get 
from requests.auth import HTTPBasicAuth
#import sys

confFile = '/etc/nagios/nagios.test'
confDir = '/etc/nagios/'

## Install Nagios on Centos/RHEL:

sh('yum update -y ; yum install nagios -y')

## Install Nagios-Plugins and nrpe:
packages = ['nagios-plugins', 'nrpe', 'nagios-plugins-nrpe']

for p in packages:
	sh(f'yum install -y {p}')

plugins = ['users', 'uptime', 'ssh', 'ping', 'procs', 'load', 'http', 'swap', 'disk']

for pl in plugins:
    sh(f'yum install nagios-plugins-{pl} -y')	

## Start and enable httpd and nrpe:
services = ['httpd', 'nagios' 'nrpe']

for s in services:
	sh(f'systemctl start {s}.service') and sh(f'systemctl enable {s}.service')

## set password for nagiosadmin

pswd = '/tmp/nagiospass'

sh(f'touch {pswd} | chmod 600 {pswd} | echo "nagios" >> {pswd}') #password as 'nagios':- change it.

sh(f'htpasswd -i /etc/nagios/passwd nagiosadmin < {pswd}') 

sh (f'rm -f {pswd}')

## add firewall rule for http on port 80

sh('firewall-cmd --zone=public --add-port=80/tcp')
sh('firewall-cmd --zone=public --add-port=80/tcp --permanent')

## The reload command will drop all runtime configurations and applies only the permanent configuration.
## It won't break existing connections. 

## In a testing environment it's not important.

# sh('firewall-cmd --reload') 

## create an index.html for the check_http plugin to work properly

sh('echo "<h1> Apache is UP and RUNNING. </h1>" > /var/www/html/index.html') 


# # # apache and nagios status code

if get('http://localhost').status_code == 200:
	print("Apache is up and running.")
	print('*' * 50)

if get('http://localhost/nagios', auth=HTTPBasicAuth('nagiosadmin', 'nagios')).status_code == 200:
	print('Nagios is running')
	print('*' * 50) 
    sh('nagiostats | grep "^Services Ok"')

# # # For customization, uncomment the following lines and write your own definitions. ()

# # # Directories to create
# directories = ['commands', 'timeperiods', 'contacts', 'contactgroups', 'hosts', 'hostgroups', 'services', 'servicegroups']
# fullpath = []

# for d in directories:
#     fullpath.append(f"/etc/nagios/{d}") 


# ## Creating directories
# for i in fullpath:
#     sh(f'mkdir {i}')


# ##remove entries from nagios.cfg
# entries = ['cfg_file', '#cfg_dir']

# for e in entries:
#     sh(f'sed -i "/{e}/d" {confFile}')

# # Changing directory
# os.chdir(f'{confDir}')

# ## New entries in nagios.cfg

# for new in fullpath:
#     sh(f"sed -i '/^# directive* /a cfg_dir={new}' /etc/nagios.cfg") 

# sh('cp /etc/nagios/objects/commands.cfg /etc/nagios/commands/defaults.cfg')







