
# setup dependencies
pip install -r requirements.txt

# ssl certificate
# if question is asked, enter dummy as common name

openssl genrsa 2048 > django.key
openssl req -new -x509 -nodes -sha256 -days 365 -key django.key > django.crt -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=dummy"

# run server
python3 manage.py runsslserver 0:8000 --certificate django.crt --key django.key