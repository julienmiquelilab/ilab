#! /bin/bash
apt-get update

sudo apt-get --assume-yes install python3-pip
sudo apt-get --assume-yes install default-libmysqlclient-dev
pip3 --version
sudo pip3 install mysql_config
sudo pip3 install flask_mysqldb
curl https://raw.githubusercontent.com/julienmiquelilab/ilab/master/app-IN-cloud-TP1.py > app-IN-cloud-TP1.py
mkdir templates
curl https://raw.githubusercontent.com/julienmiquelilab/ilab/master/index.html > templates/index.html

python3 app-IN-cloud-TP1.py
