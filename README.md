# content_manager
## Простой телеграм бот, которого можно добавить в группу и он будет сохранять на Яндекс Диск публикуемые фото / видео / кружочки.  
### Также возможно отдельное добавление контента в личных сообщениях с боту.

### Процесс установки:
1) git clone https://github.com/Oleg-Pashchenko/content_manager.git
2) cd content_manager/
3) pip install -r requirements.txt
4) 
---  Настройка ключей доступа
1. Получите токен телеграм бота в @BotFather
2. Получите токен Яндекс Диска по [данной инструкции](https://yandex.ru/dev/id/doc/dg/oauth/concepts/about.html)
3. Вставьте их в файл .env (
cat > .env
TELEGRAM_TOKEN=<ваш_телеграм_токен>
YANDEX_DISK_TOKEN=<ваш_яндекс_токен>
)
---
4) python telegram_client.py
