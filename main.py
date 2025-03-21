from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from function import handle_text
import os
import urllib.parse
import pymysql

TOKEN = os.getenv("TOKEN")


def get_db_connection():
    try:
        mysql_public_url = os.getenv("MYSQL_PUBLIC_URL")
        if not mysql_public_url:
            raise ValueError("MYSQL_PUBLIC_URL не определён в переменных окружения")

        parsed_url = urllib.parse.urlparse(mysql_public_url)
        user = parsed_url.username
        password = parsed_url.password
        host = parsed_url.hostname
        port = parsed_url.port or 3306
        database = parsed_url.path[1:]

        conn = pymysql.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )

        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_name VARCHAR(255),
                user_id VARCHAR(20) PRIMARY KEY,
                first_name VARCHAR(255),
                last_name VARCHAR(255)
            )
        """)
        conn.commit()

        return conn
    except Exception as e:
        raise


def start_func(update, context):
    user = update.message.from_user
    user_id = str(user.id)
    first_name = user.first_name
    last_name = user.last_name
    user_name = user.username
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT user_id FROM users WHERE user_id = %s", (user_id,))
            if not cursor.fetchone():
                cursor.execute("""
                    INSERT INTO users (user_id, user_name, first_name, last_name)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, user_name, first_name, last_name))
                conn.commit()
                print(f"Добавлен пользователь: {user_id}, {first_name}")
    except Exception as e:
        print(f"Ошибка при записи в базу: {e}")
        update.message.reply_text("Произошла ошибка. Попробуйте позже.")
        return
    update.message.reply_text(
        text="Salom bu botga ism yozing(uzbekchada) bot sizga yozgan ismingizni manosini topib beradi! (15000-ta ism ichidan)")

updater = Updater(token=f"{TOKEN}")
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_func))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))
updater.start_polling()
updater.idle()
