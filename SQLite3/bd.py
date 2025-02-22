# SQLite3/bd.py
# Файл для работы с базой данных пользователей бота

import sqlite3

# Функция создания базы данных
def create_user_db(bd_name : str = 'bd_user.db'):
    db = sqlite3.connect(bd_name)
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY, 
        tg_id INTEGER NOT NULL, 
        username TEXT, 
        first_name TEXT, 
        last_name TEXT, 
        status TEXT, 
        last_message TEXT, 
        last_message_time TIMESTAMP, 
        UNIQUE(tg_id)
    );''')
    db.commit()
    db.close()
