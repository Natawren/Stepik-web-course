sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE djangobase;"
mysql -uroot -e "CREATE USER 'gdb@localhost' IDENTIFIED BY 'password';"
mysql -uroot -e "GRANT ALL ON djangobase.* TO 'gdb@localhost';"
