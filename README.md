# hr_nti_bot

В этом репозитории находится бот, созданный для адаптации и помощии сотрудникам Платформы НТИ и Университета 2035. 

## Инструкция по настройке
Для того, чтобы запустить бота - вам необходимо иметь сервер PostgreSQL.

После клонирования репозитория создайте файл token_telegram.py.
Поместите в этот файл токен и информацию для подключения к базе данных.

```
token = "ваш токен"

PG_USER = 'user'

PG_PASS = 'password'

host = 'ip'

database = "postgres"
```

Затем запустите в консоли команду, чтобы подключиться к базе данных и создать разделы для бота (если они еще не были созданы):
```
python3 sql.py
```

После этого запустите команду для включения бота:
```
python3 bot.py
```

## Инструкция по автоматическому запуску бота на сервере

Создаем файл в корне системы bot.service:
```
cd /etc/systemd/system
sudo nano bot.service
```

И вписываем туда данное содержимое:
```
[Unit]
Description=Telegram bot adaptation NTI
After=syslog.target
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/название вашего юзера/название папки в которой лежит бот
ExecStart=/usr/bin/python3 /home/название вашего юзера/название папки в которой лежит бот/bot.py

RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target
```

А затем запустите команды:
```
sudo systemctl daemon-reload
sudo systemctl enable bot
sudo systemctl start bot
sudo systemctl status bot
```

Для перезагрузки бота после обновлений введите команды: 
```
sudo systemctl stop bot
sudo systemctl daemon-reload
sudo systemctl start bot
sudo systemctl status bot
```

## Содержимое файлов
>*misc.py* - подключение бота, базы данных для логов и базы данных Redis для текущего статуса юзера
>
>*bot.py* - запуск бота
>
>*sql.py* - подключение и запуск Postges базы данных
>
>*config.py* - некоторые конфиги
>
>*groups.py* - группы состояний (State) юзеров
>
>*keyboards.py* - всплывающие клавиатуры для различных состояний
>
>*reply_texts.py* - файл с текстами сообщений
>
>*token_telegram.py* - токен телеграма и информация для подключения к серверу Postgres (изначально отсутсвует)
>
>*/handlers/adaptation.py* - структура блока адаптации
>
>*/handlers/default_handlers.py* - стандартный обработчик и главное меню
>
>*/handlers/general_commands.py* - главные комманды, а также команды базы данных
>
>*/handlers/faq.py* - структура блока faq
>
>*/handlers/help.py* - структура блока с помощью от hr
>
>*/handlers/registration.py* - структура блока с регистрацией

## Содержимое базы данных (логи)
>*chat_id* - id чата с пользователем и ботом
>
>*date* - дата
>
>*time* - время
>
>*type* - в каком блоке главного меню находится пользователь
>
>*context* - в каком подблоке находится пользователь*
>
## Содержимое базы данных (пользователи)
>*chat_id* - id чата с пользователем и ботом
>
>*date* - дата
>
>*time* - время
>
>*username* - ФИ пользователя
>
>*nickname* - ник Telegram
>
>*department* - департамент
>
>*company* - организация

По возникающим вопросам пишите в Telegram @agoptar
