Начнем пожалуй с BotLibrary, я думаю после преобразовать его в пакет для ботов


Первый модуль analytics V
    type_chat.py - определяет тип чата type_chat(message):
        -Личный
        -Группы
        -Канал
    
    type_msg.py - определяет тип сообщения type_msg(message):
        -Текст
        -Фото
        -Стикер
        -...


    








Второй модуль loggers:
    logs.py - создает логгеры, три кастомных уровня и 4 обычных. Он может создавать
    -NEW_USER
    -LEAVE_USER
    -START показывает 
    














Последний модуль validators:
    email_valid.py - содержит проверку на почту, для будущих добавлений [valid_email(email)]
    normal_word.py - проводит к виду "Видообразование" [normal_words]
    url_valid.py - 