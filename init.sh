sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo -s ln -sf /home/box/web/etc/gunicorn.conf  /etc/gunicorn.d/gunicorn.conf
sudo -s ln -sf /home/box/web/etc/django_gunicorn.conf  /etc/gunicorn.d/django_gunicorn.conf
sudo /etc/init.d/gunicorn restart
