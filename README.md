# Quality Log Control

## Overview

This project implements a log ingestor and a query interface to manage and search logs from multiple APIs.

## Features

- Log ingestor to collect logs from multiple APIs.
- Query interface with filters for level, log string, timestamp, and source.
- Configurable logging levels and paths.
- Efficient search and retrieval of log data.

## Setup

### Requirements

- Python 3.x
- Flask
- Requests
- PyYAML

### Installation

1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
3.Configure the log ingestor in 'config.yaml'.

4.Run the log ingestor:

        python ingestor/log_ingestor.py
5.Run the query interface:

       python query_interface/app.py
6.Open your browser and navigate to http://127.0.0.1:5000 to access the query interface.
