#!/usr/bin/env python3
"""
Seed script to populate the transactions table with 100 random test records.
Run this after the database is up, e.g.:
    python3 scripts/seed-data.py
"""
import psycopg2
import random
import datetime

# Connection parameters – adjust if you change credentials or ports
conn = psycopg2.connect(
    dbname="treasury",
    user="treasury",
    password="treasury123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Clean up existing test data (optional)
cur.execute("DELETE FROM transactions;")

statuses = ['PENDING', 'COMPLETED', 'FAILED']
currencies = ['USD', 'EUR', 'GBP', 'RUB']

for _ in range(100):
    amount = round(random.uniform(1.0, 9999.99), 2)
    currency = random.choice(currencies)
    status = random.choice(statuses)
    created_at = datetime.datetime.now() - datetime.timedelta(days=random.randint(0, 30))
    cur.execute(
        "INSERT INTO transactions (amount, currency, status, created_at) VALUES (%s, %s, %s, %s)",
        (amount, currency, status, created_at)
    )

conn.commit()
cur.close()
conn.close()
print("Seeded 100 test transactions.")