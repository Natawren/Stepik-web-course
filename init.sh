
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -b 0.0.0.0:8080 --pythonpath /home/box/web/ hello:application     
gunicorn -b 0.0.0.0:8000 --pythonpath /home/box/web/ask ask.wsgi:application 
