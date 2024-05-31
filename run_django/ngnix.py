sudo apt-get update
sudo apt-get install nginx
pip install gunicorn
pip install django


gunicorn --workers 3 myproject.wsgi:application
sudo nano /etc/systemd/system/gunicorn.service
gunicorn --workers 3 myproject.wsgi:application
sudo nano /etc/systemd/system/gunicorn.service
[Unit]
Description=gunicorn daemon for Django project
After=network.target

[Service]
User=youruser
Group=www-data
WorkingDirectory=/path/to/your/project
ExecStart=/path/to/your/venv/bin/gunicorn --workers 3 --bind unix:/path/to/your/project/myproject.sock myproject.wsgi:application

[Install]
WantedBy=multi-user.target
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
server {
    listen 80;
    server_name example.com;  # Replace with your domain or IP address

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/myproject;  # Path to your project directory
    }

    location /media/ {
        root /home/ubuntu/myproject;  # Path to your project directory
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/myproject/myproject.sock;  # Path to your Gunicorn socket
    }
}
server {
        listen 80;
        server_name myapp.com;  # Replace with your actual domain

        location / {
            return 301 https://$host$request_uri;
        }
    }
}
