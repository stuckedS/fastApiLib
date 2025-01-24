Развертывание FastAPI приложени
Требования
- [Docker](https://www.docker.com/products/docker-desktop) 
- [Docker Compose](https://docs.docker.com/compose/)
Шаги для развертывания
1. Клонируйте репозиторий: ```bash git clone https://github.com/yourusername/your-repository.git cd your-repository ```
2. Создайте и запустите контейнеры: ```bash docker-compose up --build ```
3. Выполните миграции базы данных с использованием Alembic: ```bash docker-compose exec app bash alembic upgrade head ``` 
4. Приложение будет доступно по адресу: ``` http://localhost:8000 ``` 
5. Чтобы остановить контейнеры: ```bash docker-compose down ```
Структура проекта
- **app/** — исходный код приложения -
- **docker-compose.yml** — конфигурация Docker Compose
- **Dockerfile** — инструкция для создания образа приложения
- **alembic.ini** — конфигурация Alembic
- **migrations/** — папка с миграциями Alembic
Примечания
- Убедитесь, что в `alembic.ini` указан правильный URI для подключения к базе данных. 
- Все миграции можно просматривать и применять через команду `alembic`.
