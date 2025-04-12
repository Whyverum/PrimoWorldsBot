# BotLibrary/system/db_class.py
# Создание базы данных
import os
import sqlite3
from datetime import datetime, timedelta, timezone
from aiogram import types
from typing import Optional, List, Tuple
from ProjectsFiles import BotVar

# Настройка экспорта в модули
__all__ = ("Database",)

class Database:
    """Класс для управления базой данных пользователей чата с использованием SQLite3."""

    def __init__(self, db_name: str = BotVar.bd_path) -> None:
        """Инициализация класса с именем базы данных."""
        self.db_name = db_name

    # --- Основные методы из предоставленных функций ---

    def create_db(self) -> None:
        """Создание базы данных и таблиц с начальными данными."""
        # Создание директории, если её нет
        db_directory = os.path.dirname(self.db_name)
        if db_directory and not os.path.exists(db_directory):
            os.makedirs(db_directory)

        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()

            # Таблица пользователей
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                tg_id INTEGER NOT NULL UNIQUE,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                role TEXT DEFAULT NULL,
                status TEXT DEFAULT 'active',
                user TEXT DEFAULT 'user'
            );''')

            # Таблица сообщений пользователей
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_messages (
                user_id INTEGER PRIMARY KEY,
                last_message TEXT,
                last_message_id INTEGER,
                last_message_time TEXT,
                messages_per_day INTEGER DEFAULT 0,
                messages_per_week INTEGER DEFAULT 0,
                messages_per_month INTEGER DEFAULT 0,
                total_messages INTEGER DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
            );''')

            # Таблица персонажей Genshin Impact
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS characters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                region TEXT NOT NULL,
                name TEXT NOT NULL,
                status TEXT DEFAULT 'Свободно',
                user_id INTEGER DEFAULT NULL,
                comment TEXT DEFAULT '',
                FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE SET NULL
            );''')

            # Таблица персонажей Honkai: Star Rail
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS characters_hsr (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                region TEXT NOT NULL,
                name TEXT NOT NULL,
                status TEXT DEFAULT 'Свободно',
                user_id INTEGER DEFAULT NULL,
                comment TEXT DEFAULT '',
                FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE SET NULL
            );''')

            # Начальные данные для characters (Genshin Impact)
            characters_genshin: list[tuple[str, str, str, str]] = [
                # Мондштадт
                ("Мондштадт", "Венти", "Свободно", ""),
                ("Мондштадт", "Кэйа", "Свободно", ""),
                ("Мондштадт", "Альбедо", "Свободно", ""),
                ("Мондштадт", "Дилюк", "Свободно", ""),
                ("Мондштадт", "Мика", "Свободно", ""),
                ("Мондштадт", "Беннет", "Свободно", ""),
                ("Мондштадт", "Рэйзор", "Свободно", ""),
                ("Мондштадт", "Эола", "Свободно", ""),
                ("Мондштадт", "Мона", "Свободно", ""),
                ("Мондштадт", "Джинн", "Свободно", ""),
                ("Мондштадт", "Диона", "Свободно", ""),
                ("Мондштадт", "Лиза", "Свободно", ""),
                ("Мондштадт", "Ноэлль", "Свободно", ""),
                ("Мондштадт", "Сахароза", "Свободно", ""),
                ("Мондштадт", "Розария", "Свободно", ""),
                ("Мондштадт", "Эмбер", "Свободно", ""),
                ("Мондштадт", "Фишль", "Свободно", ""),
                ("Мондштадт", "Барбара", "Свободно", ""),

                # Ли Юэ
                ("Ли Юэ", "Чжун Ли", "Свободно", ""),
                ("Ли Юэ", "Сяо", "Свободно", ""),
                ("Ли Юэ", "Син Цю", "Свободно", ""),
                ("Ли Юэ", "Чун Юнь", "Свободно", ""),
                ("Ли Юэ", "Бай Чжу", "Свободно", ""),
                ("Ли Юэ", "Е Лань", "Свободно", ""),
                ("Ли Юэ", "Шень Хэ", "Свободно", ""),
                ("Ли Юэ", "Гань Юй", "Свободно", ""),
                ("Ли Юэ", "Ци Ци", "Свободно", ""),
                ("Ли Юэ", "Кэ Цин", "Свободно", ""),
                ("Ли Юэ", "Янь Фэй", "Свободно", ""),
                ("Ли Юэ", "Нин Гуан", "Свободно", ""),
                ("Ли Юэ", "Бэй Доу", "Свободно", ""),
                ("Ли Юэ", "Яо Яо", "Свободно", ""),
                ("Ли Юэ", "Ка Мин", "Свободно", ""),
                ("Ли Юэ", "Сянь Юнь", "Свободно", ""),
                ("Ли Юэ", "Юнь Цзинь", "Свободно", ""),
                ("Ли Юэ", "Ху Тао", "Свободно", ""),
                ("Ли Юэ", "Лань Янь", "Свободно", ""),

                # Инадзума
                ("Инадзума", "Итто", "Свободно", ""),
                ("Инадзума", "Горо", "Свободно", ""),
                ("Инадзума", "Аято", "Свободно", ""),
                ("Инадзума", "Хэйдзо", "Свободно", ""),
                ("Инадзума", "Тома", "Свободно", ""),
                ("Инадзума", "Кадзуха", "Свободно", ""),
                ("Инадзума", "Кирара", "Свободно", ""),
                ("Инадзума", "Кудзё Сара", "Свободно", ""),
                ("Инадзума", "Ёимия", "Свободно", ""),
                ("Инадзума", "Аяка", "Свободно", ""),
                ("Инадзума", "Сангономия Кокоми", "Свободно", ""),
                ("Инадзума", "Яэ Мико", "Свободно", ""),
                ("Инадзума", "Райдэн Эи", "Свободно", ""),
                ("Инадзума", "Саю", "Свободно", ""),
                ("Инадзума", "Куки Синобу", "Свободно", ""),
                ("Инадзума", "Мидзуки", "Свободно", ""),

                # Сумеру
                ("Сумеру", "Аль-Хайтам", "Свободно", ""),
                ("Сумеру", "Кавех", "Свободно", ""),
                ("Сумеру", "Сайно", "Свободно", ""),
                ("Сумеру", "Тигнари", "Свободно", ""),
                ("Сумеру", "Сетос", "Свободно", ""),
                ("Сумеру", "Нилу", "Свободно", ""),
                ("Сумеру", "Нахида", "Свободно", ""),
                ("Сумеру", "Лайла", "Свободно", ""),
                ("Сумеру", "Кандакия", "Свободно", ""),
                ("Сумеру", "Дори", "Свободно", ""),
                ("Сумеру", "Дэхья", "Свободно", ""),
                ("Сумеру", "Коллеи", "Свободно", ""),
                ("Сумеру", "Фарузан", "Свободно", ""),

                # Фонтейн
                ("Фонтейн", "Лини", "Свободно", ""),
                ("Фонтейн", "Ризли", "Свободно", ""),
                ("Фонтейн", "Невиллет", "Свободно", ""),
                ("Фонтейн", "Фремине", "Свободно", ""),
                ("Фонтейн", "Линетт", "Свободно", ""),
                ("Фонтейн", "Эмилия", "Свободно", ""),
                ("Фонтейн", "Клоринда", "Свободно", ""),
                ("Фонтейн", "Навия", "Свободно", ""),
                ("Фонтейн", "Шарлотта", "Свободно", ""),
                ("Фонтейн", "Фурина", "Свободно", ""),
                ("Фонтейн", "Тиори", "Свободно", ""),
                ("Фонтейн", "Сиджвин", "Свободно", ""),

                # Натлан
                ("Натлан", "Кинич", "Свободно", ""),
                ("Натлан", "Оророн", "Свободно", ""),
                ("Натлан", "Муалани", "Свободно", ""),
                ("Натлан", "Ситлали", "Свободно", ""),
                ("Натлан", "Шилонен", "Свободно", ""),
                ("Натлан", "Иансан", "Свободно", ""),
                ("Натлан", "Мавуика", "Свободно", ""),
                ("Натлан", "Часка", "Свободно", ""),

                # Фатуи
                ("Фатуи", "Тарталья", "Свободно", ""),
                ("Фатуи", "Панталоне", "Свободно", ""),
                ("Фатуи", "Дотторе", "Свободно", ""),
                ("Фатуи", "Капитано", "Свободно", ""),
                ("Фатуи", "Пьеро", "Свободно", ""),
                ("Фатуи", "Пульничелла", "Свободно", ""),
                ("Фатуи", "Синьора", "Свободно", ""),
                ("Фатуи", "Арлекино", "Свободно", ""),
                ("Фатуи", "Коломбина", "Свободно", ""),
                ("Фатуи", "Царица", "Свободно", ""),
                ("Фатуи", "Странник", "Свободно", ""),

                # Иные персонажи
                ("Иные персонажи", "Итэр", "Свободно", ""),
                ("Иные персонажи", "Люмин", "Свободно", ""),
                ("Иные персонажи", "Элой", "Свободно", ""),
                ("Иные персонажи", "Паймон", "Свободно", ""),
                ("Иные персонажи", "Дайнслейф", "Свободно", ""),
            ]

            # Начальные данные для characters_hsr (Honkai: Star Rail)
            characters_hsr: list[tuple[str, str, str, str]] = [
                # Ярило-6
                ("Ярило-6", "Броня", "Свободно", ""),
                ("Ярило-6", "Гепард", "Свободно", ""),
                ("Ярило-6", "Зеле", "Свободно", ""),
                ("Ярило-6", "Клара", "Свободно", ""),
                ("Ярило-6", "Лука", "Свободно", ""),
                ("Ярило-6", "Наташа", "Свободно", ""),
                ("Ярило-6", "Пела", "Свободно", ""),
                ("Ярило-6", "Рысь", "Свободно", ""),
                ("Ярило-6", "Сампо", "Свободно", ""),
                ("Ярило-6", "Сервал", "Свободно", ""),
                ("Ярило-6", "Хук", "Свободно", ""),

                # Станция «Герта»
                ("Станция «Герта»", "Арлан", "Свободно", ""),
                ("Станция «Герта»", "Аста", "Свободно", ""),
                ("Станция «Герта»", "Великая Герта", "Свободно", ""),
                ("Станция «Герта»", "Кукла «Герта»", "Свободно", ""),
                ("Станция «Герта»", "Жуань Мэй", "Свободно", ""),

                # Пенакония
                ("Пенакония", "Авантюрин", "Свободно", ""),
                ("Пенакония", "Ахерон", "Свободно", ""),
                ("Пенакония", "Галлахер", "Свободно", ""),
                ("Пенакония", "Зарянка", "Свободно", ""),
                ("Пенакония", "Миша", "Свободно", ""),
                ("Пенакония", "Мистер Река", "Свободно", ""),
                ("Пенакония", "Раппа", "Свободно", ""),
                ("Пенакония", "Чёрный Лебедь", "Свободно", ""),
                ("Пенакония", "Яшма", "Свободно", ""),
                ("Пенакония", "Воскресенье", "Свободно", ""),

                # Звёздный Экспресс
                ("Звёздный Экспресс", "Вельт", "Свободно", ""),
                ("Звёздный Экспресс", "Келус", "Свободно", ""),
                ("Звёздный Экспресс", "Стелла", "Свободно", ""),
                ("Звёздный Экспресс", "Дань Хэн", "Свободно", ""),
                ("Звёздный Экспресс", "Март 7", "Свободно", ""),
                ("Звёздный Экспресс", "Химеко", "Свободно", ""),
                ("Звёздный Экспресс", "Пом Пом", "Свободно", ""),

                # Галактика
                ("Галактика", "Аргенти", "Свободно", ""),
                ("Галактика", "Блэйд", "Свободно", ""),
                ("Галактика", "Бутхилл", "Свободно", ""),
                ("Галактика", "Доктор Рацио", "Свободно", ""),
                ("Галактика", "Кафка", "Свободно", ""),
                ("Галактика", "Светлячок", "Свободно", ""),
                ("Галактика", "Искорка", "Свободно", ""),
                ("Галактика", "Серебряный Волк", "Свободно", ""),
                ("Галактика", "Топаз", "Свободно", ""),

                # Амфореус
                ("Амфореус", "Аглая", "Свободно", ""),
                ("Амфореус", "Мидей", "Свободно", ""),
                ("Амфореус", "Трибби", "Свободно", ""),

                # Альянс Сяньчжоу
                ("Альянс Сяньчжоу", "Байлу", "Свободно", ""),
                ("Альянс Сяньчжоу", "Гуйнайфей", "Свободно", ""),
                ("Альянс Сяньчжоу", "Линша", "Свободно", ""),
                ("Альянс Сяньчжоу", "Лоча", "Свободно", ""),
                ("Альянс Сяньчжоу", "Моцзэ", "Свободно", ""),
                ("Альянс Сяньчжоу", "Пожиратель Луны", "Свободно", ""),
                ("Альянс Сяньчжоу", "Сушан", "Свободно", ""),
                ("Альянс Сяньчжоу", "Сюзи", "Свободно", ""),
                ("Альянс Сяньчжоу", "Фуга", "Свободно", ""),
                ("Альянс Сяньчжоу", "Фэйсяо", "Свободно", ""),
                ("Альянс Сяньчжоу", "Ханья", "Свободно", ""),
                ("Альянс Сяньчжоу", "Хохо", "Свободно", ""),
                ("Альянс Сяньчжоу", "Цзин Юань", "Свободно", ""),
                ("Альянс Сяньчжоу", "Цзиннлю", "Свободно", ""),
                ("Альянс Сяньчжоу", "Цзяоцю", "Свободно", ""),
                ("Альянс Сяньчжоу", "Цинцюэ", "Свободно", ""),
                ("Альянс Сяньчжоу", "Юйкун", "Свободно", ""),
                ("Альянс Сяньчжоу", "Юньли", "Свободно", ""),
                ("Альянс Сяньчжоу", "Яньцин", "Свободно", ""),
            ]

            # Заполнение таблиц начальными данными, если они пусты
            cursor.execute("SELECT COUNT(*) FROM characters")
            if cursor.fetchone()[0] == 0:
                cursor.executemany('INSERT INTO characters (region, name, status, comment) VALUES (?, ?, ?, ?)',
                                   characters_genshin)

            cursor.execute("SELECT COUNT(*) FROM characters_hsr")
            if cursor.fetchone()[0] == 0:
                cursor.executemany('INSERT INTO characters_hsr (region, name, status, comment) VALUES (?, ?, ?, ?)',
                                   characters_hsr)

            db.commit()

    def add_user(self, tg_id: int, username: str, first_name: str, last_name: str, role: str, status: str,
                 user: str) -> None:
        """Добавление нового пользователя в базу данных."""
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()

            # Проверка на существование пользователя
            cursor.execute("SELECT user_id FROM users WHERE tg_id = ?", (tg_id,))
            if cursor.fetchone():
                return  # Пользователь уже существует

            # Определение нового user_id
            cursor.execute("SELECT MAX(user_id) FROM users")
            max_id = cursor.fetchone()[0]
            new_user_id = 1 if max_id is None else max_id + 1

            # Вставка пользователя
            cursor.execute('''
            INSERT INTO users (user_id, tg_id, username, first_name, last_name, role, status, user)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (new_user_id, tg_id, username, first_name, last_name, role, status, user))

            # Создание записи в user_messages
            cursor.execute('INSERT INTO user_messages (user_id) VALUES (?)', (new_user_id,))
            db.commit()

    def get_user(self, tg_id: int) -> Optional[Tuple]:
        """Получение информации о пользователе по tg_id."""
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE tg_id = ?", (tg_id,))
            return cursor.fetchone()

    def update_user(self, tg_id: int, username: Optional[str] = None, first_name: Optional[str] = None,
                    last_name: Optional[str] = None, role: Optional[str] = None, user: Optional[str] = None) -> None:
        """Обновление данных о пользователе."""
        updates = []
        params = []

        if username:
            updates.append("username = ?")
            params.append(username)
        if first_name:
            updates.append("first_name = ?")
            params.append(first_name)
        if last_name:
            updates.append("last_name = ?")
            params.append(last_name)
        if role:
            updates.append("role = ?")
            params.append(role)
        if user:
            updates.append("user = ?")
            params.append(user)

        if updates:
            query = f"UPDATE users SET {', '.join(updates)} WHERE tg_id = ?"
            params.append(tg_id)
            with sqlite3.connect(self.db_name) as db:
                cursor = db.cursor()
                cursor.execute(query, params)
                db.commit()

    def update_user_messages(self, message: types.Message) -> None:
        """Обновление статистики сообщений пользователя."""
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            tg_id = message.from_user.id

            # Получение user_id
            cursor.execute("SELECT user_id FROM users WHERE tg_id = ?", (tg_id,))
            result = cursor.fetchone()
            if not result:
                return  # Пользователь не найден
            user_id = result[0]

            # Проверка существующей записи в user_messages
            cursor.execute(
                "SELECT last_message_time, messages_per_day, messages_per_week, messages_per_month, total_messages "
                "FROM user_messages WHERE user_id = ?", (user_id,))
            result = cursor.fetchone()

            # Время сообщения в московском часовом поясе
            now = message.date.astimezone(timezone(timedelta(hours=3)))
            today = now.date()
            start_of_week = today - timedelta(days=today.weekday())
            current_month = now.month
            current_year = now.year

            last_message = message.text or "Н/Д"  # Замените на type_msg(message) при необходимости
            last_message_id = message.message_id

            if result:
                last_message_time, messages_per_day, messages_per_week, messages_per_month, total_messages = result
                if last_message_time:
                    last_message_time = datetime.fromisoformat(last_message_time).astimezone(
                        timezone(timedelta(hours=3)))
                    last_date = last_message_time.date()
                    last_week = last_date - timedelta(days=last_date.weekday())
                    last_month = last_message_time.month
                    last_year = last_message_time.year

                    # Обнуление счетчиков при смене периода
                    if last_date != today:
                        messages_per_day = 0
                    if last_week != start_of_week:
                        messages_per_week = 0
                    if last_month != current_month or last_year != current_year:
                        messages_per_month = 0
                else:
                    messages_per_day, messages_per_week, messages_per_month = 0, 0, 0

                # Увеличение счетчиков
                messages_per_day += 1
                messages_per_week += 1
                messages_per_month += 1
                total_messages += 1
            else:
                messages_per_day, messages_per_week, messages_per_month, total_messages = 1, 1, 1, 1
                cursor.execute('''
                INSERT INTO user_messages (user_id, last_message, last_message_id, last_message_time, 
                                          messages_per_day, messages_per_week, messages_per_month, total_messages)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (user_id, last_message, last_message_id, now.isoformat(), messages_per_day,
                      messages_per_week, messages_per_month, total_messages))
                db.commit()
                return

            # Обновление записи
            cursor.execute('''
            UPDATE user_messages
            SET last_message = ?, last_message_id = ?, last_message_time = ?, 
                messages_per_day = ?, messages_per_week = ?, messages_per_month = ?, 
                total_messages = ?
            WHERE user_id = ?
            ''', (last_message, last_message_id, now.isoformat(), messages_per_day,
                  messages_per_week, messages_per_month, total_messages, user_id))
            db.commit()

    def get_user_status(self, message: types.Message) -> str:
        """Получение статуса пользователя."""
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute("SELECT user FROM users WHERE tg_id = ?", (message.from_user.id,))
            row = cursor.fetchone()
            status_map = {
                "ban": "Забанен",
                "user": "Пользователь",
                "moderator": "Модератор",
                "admin": "Администратор",
                "so-owner": "Совладелец",
                "owner": "Владелец",
            }
            return status_map.get(row[0], "Ошибка!") if row else "Пользователь не найден"

    # --- Новые и улучшенные методы ---

    def delete_user(self, tg_id: int) -> None:
        """Удаление пользователя из базы данных."""
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM users WHERE tg_id = ?", (tg_id,))
            db.commit()

    def get_all_users(self) -> List[Tuple]:
        """Получение списка всех пользователей."""
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()

    def get_user_messages(self, tg_id: int) -> Optional[Tuple]:
        """Получение статистики сообщений пользователя."""
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute("SELECT user_id FROM users WHERE tg_id = ?", (tg_id,))
            result = cursor.fetchone()
            if not result:
                return None
            user_id = result[0]
            cursor.execute("SELECT * FROM user_messages WHERE user_id = ?", (user_id,))
            return cursor.fetchone()

    def ban_user(self, tg_id: int) -> None:
        """Блокировка пользователя."""
        self.update_user(tg_id, user="ban")

    def unban_user(self, tg_id: int) -> None:
        """Разблокировка пользователя."""
        self.update_user(tg_id, user="user")

    def promote_user(self, tg_id: int, new_role: str) -> None:
        """Изменение роли пользователя."""
        valid_roles = ["user", "moderator", "admin", "so-owner", "owner"]
        if new_role in valid_roles:
            self.update_user(tg_id, user=new_role)

    def get_top_active_users(self, limit: int = 10) -> List[Tuple]:
        """Получение самых активных пользователей по количеству сообщений."""
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute('''
            SELECT u.tg_id, u.username, um.total_messages
            FROM users u
            JOIN user_messages um ON u.user_id = um.user_id
            ORDER BY um.total_messages DESC
            LIMIT ?
            ''', (limit,))
            return cursor.fetchall()

    def assign_character(self, tg_id: int, character_id: int, game: str = "genshin") -> bool:
        """Назначение персонажа пользователю."""
        table = "characters" if game == "genshin" else "characters_hsr"
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute(f"SELECT user_id FROM {table} WHERE id = ?", (character_id,))
            result = cursor.fetchone()
            if result and result[0] is not None:
                return False  # Персонаж уже занят

            cursor.execute("SELECT user_id FROM users WHERE tg_id = ?", (tg_id,))
            user_id = cursor.fetchone()
            if not user_id:
                return False  # Пользователь не найден

            cursor.execute(f"UPDATE {table} SET user_id = ?, status = 'Занят' WHERE id = ?", (user_id[0], character_id))
            db.commit()
            return True

    def free_character(self, character_id: int, game: str = "genshin") -> None:
        """Освобождение персонажа."""
        table = "characters" if game == "genshin" else "characters_hsr"
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute(f"UPDATE {table} SET user_id = NULL, status = 'Свободно' WHERE id = ?", (character_id,))
            db.commit()

    def get_user_characters(self, tg_id: int, game: str = "genshin") -> List[Tuple]:
        """Получение списка персонажей пользователя."""
        table = "characters" if game == "genshin" else "characters_hsr"
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute("SELECT user_id FROM users WHERE tg_id = ?", (tg_id,))
            user_id = cursor.fetchone()
            if not user_id:
                return []
            cursor.execute(f"SELECT * FROM {table} WHERE user_id = ?", (user_id[0],))
            return cursor.fetchall()

    def search_users(self, query: str) -> List[Tuple]:
        """Поиск пользователей по имени или юзернейму."""
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute("""
            SELECT * FROM users 
            WHERE username LIKE ? OR first_name LIKE ? OR last_name LIKE ?
            """, (f"%{query}%", f"%{query}%", f"%{query}%"))
            return cursor.fetchall()

    def get_character_by_name(self, name: str, game: str = "genshin") -> Optional[Tuple]:
        """Поиск персонажа по имени."""
        table = "characters" if game == "genshin" else "characters_hsr"
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM {table} WHERE name = ?", (name,))
            return cursor.fetchone()
