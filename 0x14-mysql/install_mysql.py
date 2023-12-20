#!/usr/bin/python3
""" A fabfile to install mysql web_01 and web_02 server instances"""
from fabric.api import *
from fabric.utils import warn


env.user = 'ubuntu'
env.hosts = ['54.209.202.246', '54.237.71.136']
env.key_filename = '~/.ssh/school'

def host_info():
    run('uname -a')

def check_mysql():
    sudo('service mysql status')

def apt_get(*packages):
    sudo('apt-get -y --no-upgrade install %s' % ' '.join(packages), shell=False)

def uninstall_mysql():
    sudo('apt --fix-broken install')
    sudo('apt remove --purge mysql-server mysql-client mysql-common')
    sudo('apt autoremove')
    sudo('rm -rf /var/lib/mysql')
    sudo('rm -rf /etc/mysql')

def install_mysql():
    """ Installs mysql server to server nodes """
    with settings(hide('warnings', 'stderr'), warn_only=True):
        result = sudo('dpkg-query --show mysql-server')
    if result.failed is False:
        warn('MySQL is already installed')
        return
    sudo('apt update -y')
    sudo('apt-get install -y libtinfo5')
    run('wget https://downloads.mysql.com/archives/get/p/23/file/mysql-server_5.7.29-1ubuntu18.04_amd64.deb-bundle.tar')
    run('tar xaf mysql-server_5.7.29-1ubuntu18.04_amd64.deb-bundle.tar')
    sudo('apt install libaio1 libmecab2 python libjson-perl')
    sudo('dpkg -i mysql-common_5.7.29-1ubuntu18.04_amd64.deb')
    sudo('dpkg -i libmysqlclient20_5.7.29-1ubuntu18.04_amd64.deb')
    sudo('dpkg -i libmysqlclient-dev_5.7.29-1ubuntu18.04_amd64.deb')
    sudo('dpkg -i libmysqld-dev_5.7.29-1ubuntu18.04_amd64.deb')
    sudo('dpkg -i mysql-community-source_5.7.29-1ubuntu18.04_amd64.deb')
    sudo('dpkg -i mysql-community-client_5.7.29-1ubuntu18.04_amd64.deb')
    sudo('dpkg -i mysql-client_5.7.29-1ubuntu18.04_amd64.deb')
    sudo('dpkg -i mysql-community-server_5.7.29-1ubuntu18.04_amd64.deb')
    sudo('dpkg -i mysql-server_5.7.29-1ubuntu18.04_amd64.deb')
    sudo('dpkg -i mysql-community-test_5.7.29-1ubuntu18.04_amd64.deb')
    sudo('dpkg -i mysql-testsuite_5.7.29-1ubuntu18.04_amd64.deb')
    run('rm *.deb')
    run('rm mysql-server_5.7.29-1ubuntu18.04_amd64.deb-bundle.tar')

def let_us_in():
    """ Creates a mysql user to allow ALX checker to access replication client for verifcation and correctnesss"""
    put('./let_us_in.sql', '/home/ubuntu/let_us_in.sql')
    sudo('mysql -uroot -p < /home/ubuntu/let_us_in.sql')

def prepare_replica_db():
    """ Prepare a sample db and table with one record to create replica"""
    put('sample_db.sql', '/home/ubuntu/sample_db.sql')
    sudo('mysql -uroot -p < /home/ubuntu/sample_db.sql')

def create_replication_user():
    """ Creates A user to use during database server replication"""
    put('replica_user.sql', '/home/ubuntu/replica_user.sql')
    sudo('mysql -uroot -p < /home/ubuntu/replica_user.sql')
