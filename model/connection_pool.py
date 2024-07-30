from pymysql.pool import Pool
from dotenv import load_dotenv
import os

load_dotenv()
#Initialize RDS connection
rds_host = os.getenv('RDS_HOST')
rds_user = os.getenv('RDS_USER')
rds_password = os.getenv('RDS_PASSWORD')
rds_db = os.getenv('RDS_DB')

pool = Pool(
    host = rds_host,
    user = rds_user,
    password = rds_password,
    db = rds_db,
    autocommit = True,
    max_connections = 10
    )

pool.init()

def get_connection():
    return pool.get_conn()