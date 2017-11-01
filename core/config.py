from flask import Flask

ENV = "DEV"
NLU_USER = "bda973a1-8840-4890-95ff-94eac8ef1c45"
NLU_PASS = "yd7k6tAx1ylU"
TONE_USER = "506440a1-b291-4e16-8ba4-828a4ad2f5a3"
TONE_PASS = "8lDShiiDZ4vf"
GOOGLE_TRANSLATE = "AIzaSyCD1wuMdQbPGKHzEhJiO3kznjcxFh0EebU"

### DEVELOPMENT ###

DEV_PORT = 9000
DEV_DEBUG = True
DEV_HOST = 'localhost'
DEV_GEOIP_URL = 'http://159.8.19.250'
DEV_GEOIP_PORT = '9092'

### PRODUCTION ###

PROD_PORT = 8080
PROD_DEBUG = False
PROD_HOST = '0.0.0.0'
PROD_GEOIP_URL = 'http://159.8.19.250'
PROD_GEOIP_PORT = '9092'
DB_USER_NAME = "admin"
DB_PASSWORD = "OFKSRECQKIQOKQWT"
DB_HOST = "sl-eu-lon-2-portal.0.dblayer.com:18539,sl-eu-lon-2-portal.4.dblayer.com"
DB_PORT = 18539
DB_SSL = True
DB_CERT_FILE = 'cert.crt'

app = Flask(__name__)
