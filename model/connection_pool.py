from mysql.connector import pooling
from dotenv import load_dotenv
import os

load_dotenv()

# 初始化 RDS 连接配置
db_config = {
    "host": os.getenv('RDS_HOST'),
    "port": 3306,  # 默认 MySQL 端口
    "user": os.getenv('RDS_USER'),
    "password": os.getenv('RDS_PASSWORD'),
    "database": os.getenv('RDS_DB')
}

# 创建连接池
connection_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=10,
    **db_config
)

def get_connection():
    return connection_pool.get_connection()
