#! /bin/bash
apt-get update
apt-get install -y apache2
sudo apt-get --assume-yes install mysql-server
#sudo mysql_secure_installation

curl https://gist.githubusercontent.com/coderua/5592d95970038944d099/raw/98c2ffabc1fd9db73650acbf44ce7b349831f7b8/my
sql_secure.sh > secure.sh
chmod 777 secure.sh 
sudo ./secure.sh 

cat <<EOF > /var/www/html/index.html
<html><body><h1>Hello My Bank World</h1>
<p>This page was created from a simple startup script!</p>
</body></html>

EOF
