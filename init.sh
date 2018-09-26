
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd ~/web/ask/ask
sudo gunicorn ask.wsgi:application --bind 0.0.0.0:8000
