sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/django_gunicorn.conf /etc/gunicorn.d/test-django
sudo /etc/init.d/gunicorn restart
