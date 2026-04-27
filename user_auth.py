import sqlite3

def get_user_record(username):
    conn = sqlite3.connect('enterprise_db.sqlite')
    cursor = conn.cursor()
    
    # BUG: SQL Injection vulnerability (SonarQube Rule: python:S3649)
    # Untrusted input is formatted directly into the query string
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    cursor.execute(query)
    record = cursor.fetchone()
    conn.close()
    
    return record
