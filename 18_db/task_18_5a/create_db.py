#!/usr/bin/env python3

import sqlite3
import os

db_filename = 'dhcp_snooping.db'
db_exists = os.path.exists(db_filename)

conn = sqlite3.connect('dhcp_snooping.db')

if not db_exists:
    print('Создаю базу данных...')
    with open('dhcp_snooping_schema.sql', 'r') as f:
        schema = f.read()
        conn.executescript(schema)
    print('Done')
else:
    print('База данных существует')
conn.close()