#!/usr/bin/env python3
"""filtering data"""
import re
from typing import List
import os
import mysql.connector
from datetime import datetime
import getpass
from mysql.connector import Error
import logging


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """filtering data"""
    pattern = rf'(?<={separator}|=)({"|".join(fields)})[^{separator}]+'
    return re.sub(pattern, '=' + redaction, message)

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError


def get_db():
    """Retrieve credentials from environment variables or use defaults
    and create connection to the database"""
    db_username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    db_password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    try:
        connection = mysql.connector.connect(
            user=db_username,
            password=db_password,
            host=db_host,
            database=db_name
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None

def main():
    """Get a database connection"""
    connection = get_db()

    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users;")
                rows = cursor.fetchall()

                filtered_fields = ["name", "email", "phone", "ssn", "password"]

                for row in rows:
                    row_data = "; ".join([f"{field}={row[field] if field in row else '***'}" for field in filtered_fields])
                    log_message = f"[HOLBERTON] user_data INFO {datetime.now()}: {row_data};"
                    print(log_message)

        except Error as e:
            print(f"Error: {e}")

        finally:
            connection.close()

if __name__ == "__main__":
    main()