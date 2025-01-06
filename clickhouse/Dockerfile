FROM clickhouse/clickhouse-server:latest

# Copy SQL files to the container
COPY schema.sql /docker-entrypoint-initdb.d/01-schema.sql
COPY data.sql /docker-entrypoint-initdb.d/02-data.sql

# Expose necessary ports
EXPOSE 8123 9000
