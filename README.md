# Изменения в Odoo

К модели crm.lead добавлено поле employee(Выбор работника из числа всех сотрудников)
К модели hr.employee добавлено поле telegram_id(id телеграмма для отправки сообщения адреса к исполнителю. Можно получить прописав команду /get_id в боте.)
Сообщение с адресом к исполнителю отправляется при:
- создании нового lead
- смене хотя бы 1 одного пункта из адрес
- смене исполнителя lead("старому" исполнителю посылается сообщение об изменении исполнителя,"новому" посылается сообщение о его становлении новым исполнителем данного lead )
  
# Установка и запуск

Odoo
При запуске odoo (файл odoo-bin) нужно передать конфигурационный файл с параметром -c
Пример:
-c C:\Users\...\conf\odoo.conf ...
Telegram bot
Для работы бота необходимо установить библиотеку aiogram

pip install aiogram==3.4.1

При запуске бота (файл telegram_bot/main.py) также нужно передать файл конфигурации
Пример:
C:\Users\...\odoo.conf


# Кофигурация

Используются два конфигурационных файла:

- odoo.conf

db_host = localhost

db_port = 5432

db_user = ododo

db_password = odoo

addons_path = ... http_port = 8069

admin_passwd = ...
- config.py

ODOO_HOST = 'localhost'

ODOO_PORT = '8069'

ODOO_DB_NAME = 'postgres'

ODOO_LOGIN = ...

ODOO_PASSWORD = ...

TELEGRAM_TOKEN = ...


# Telegram_bot

Телеграмм бот имеет две встроенные комманды:
- /start - Знакомство с ботом
- /get_id - Получение id телеграмма для записи в поле telegram_id у hr.employee
Его возможности:
- Доставка сообщения исполнителю о lead
- Отправка сообщения в chatter lead по его id



Скриншот работы из Odoo:
![image](https://github.com/kkitami/hell/assets/149528561/302ae464-b5e4-4294-9ec4-3305ea31ec7c)


Скриншот работы бота:

![image](https://github.com/kkitami/hell/assets/149528561/03d8a6d4-0e72-4d01-988c-a33f9e93d10a)





