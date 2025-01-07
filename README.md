Airflow & ClickHouse Project

This project demonstrates the integration of Apache Airflow and ClickHouse using Docker Compose. It is organized into two main directories:

ClickHouse Directory

Airflow Directory

Each directory serves a specific purpose, and the setup is designed for ease of deployment and testing.

Project Structure

.
├── clickhouse/           # ClickHouse configuration and setup
│   ├── docker-compose.yml # Docker Compose file for ClickHouse services
│   ├── configs/           # Configuration files for ClickHouse (optional)
│   └── init/              # Initialization scripts for database setup
├── airflow/              # Apache Airflow configuration and DAGs
│   ├── docker-compose.yml # Docker Compose file for Airflow services
│   ├── dags/              # Directory containing Airflow DAGs
│   └── plugins/           # Optional custom plugins for Airflow
└── README.md             # Documentation of the project

Prerequisites

Ensure the following tools are installed on your system:

Docker

Docker Compose

Git

ClickHouse Directory

The clickhouse/ directory contains everything needed to set up a ClickHouse database environment.

Key Components

docker-compose.yml: Defines the ClickHouse service with configurations for the server and optional client tools.

configs/: Contains configuration files for customizing ClickHouse behavior (e.g., users.xml, config.xml).

init/: Includes SQL scripts or commands for initial database setup, such as creating tables or inserting data.

Running ClickHouse

To start the ClickHouse service:

cd clickhouse
docker-compose up -d

You can access ClickHouse via its HTTP interface or use the native client.

Airflow Directory

The airflow/ directory manages the Apache Airflow environment and contains DAGs for orchestrating workflows.

Key Components

docker-compose.yml: Defines the Airflow services, including the webserver, scheduler, worker, and backend database.

dags/: Contains Python scripts defining Directed Acyclic Graphs (DAGs) to manage workflows.

plugins/: Optional directory for custom plugins, operators, or hooks to extend Airflow's functionality.

Running Airflow

To start the Airflow services:

cd airflow
docker-compose up -d

Access the Airflow web UI at http://localhost:8080 (default credentials: airflow/airflow).

How It Works

Data Flow:

ClickHouse serves as the backend database for storing and analyzing data.

Airflow orchestrates workflows, automating data processing tasks.

Integration:

Airflow DAGs interact with ClickHouse using SQL commands or via Python libraries like clickhouse-driver.
