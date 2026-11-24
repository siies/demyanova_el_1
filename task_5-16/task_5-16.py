import psycopg2

try:
    # Устанавливаем соединение (используем ВАШИ данные)
    connection = psycopg2.connect(
        host="localhost",
        port="5435",              # ВАШ порт из docker-compose.yml
        user="postgres",
        password="student",       # ВАШ пароль
        database="student_task"   # ВАША база данных
    )
    print("Подключение к базе данных прошло успешно!")
    
    cursor = connection.cursor()

    # 1. Создаем тестовую таблицу (чтобы было что запрашивать)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS my_test_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50)
        );
    """)
    
    # 2. Вставляем данные
    cursor.execute("INSERT INTO my_test_table (name) VALUES ('Иван');")
    cursor.execute("INSERT INTO my_test_table (name) VALUES ('Мария');")
    
    # КРИТИЧЕСКИ ВАЖНО: сохраняем изменения в базе
    connection.commit()
    print("Данные успешно добавлены!")

    # 3. Выполняем SELECT-запрос (чтение данных)
    cursor.execute("SELECT id, name FROM my_test_table;")
    rows = cursor.fetchall()
    
    print("\nРезультат SQL-запроса:")
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}")

    # Закрываем курсор
    cursor.close()

except Exception as error:
    print(f"Ошибка при подключении или выполнении запроса: {error}")
    # Если произошла ошибка при изменении данных, откатываем изменения
    if 'connection' in locals():
        connection.rollback()

finally:
    # Закрываем соединение в любом случае
    if 'connection' in locals() and connection is not None:
        connection.close()
        print("\nСоединение с базой данных закрыто.")