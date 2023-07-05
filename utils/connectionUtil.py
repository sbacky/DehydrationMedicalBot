import psycopg
import configparser

config: configparser.ConfigParser = configparser.ConfigParser()
config.read('resources/config.ini')

dbname: str = config['DEFAULT']['dbname']
user: str = config['DEFAULT']['user']
password: str = config['DEFAULT']['password']
host: str = config['DEFAULT']['host']
port: str = config['DEFAULT']['port']

def getConnection() -> psycopg.Connection:
    conn = psycopg.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    conn.autocommit = True
    return conn