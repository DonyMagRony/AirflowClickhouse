import os

CLICKHOUSE_HOST = os.getenv('CLICKHOUSE_HOST', 'http://localhost:8123')
CLICKHOUSE_USER = os.getenv('CLICKHOUSE_USER', 'default')
CLICKHOUSE_PASSWORD = os.getenv('CLICKHOUSE_PASSWORD', '')
CLICKHOUSE_DB = os.getenv('CLICKHOUSE_DB', 'default')
