# users, todos
# 1. get -> one, all
# 2. create -> поля для заполнения
# 3. update -> поля для обновления опредленного пользователя
# 4. delete -> удаляем определенного пользователя
# рефакторинг
import texts
from crud.users import UserService
from database.db import Connection

db = Connection('todos.db')
user_service = UserService()

while True:
    work_with = input(texts.INTRO_TEXT)

    if work_with == 'users':
        print(texts.USERS_INTRO_TEXT)
        command = input(texts.USERS_COMMANDS_TEXT)
        if command == '1':  # get
            print(texts.USER_SELECTED_COMMAND_TEXT[command])
            command_get = input(texts.USER_COMMAND_GET_TEXT)
            if command_get == '1':
                print()
            elif command_get == '2':
                users = user_service.read(db, all=True)
                for user_id, username in users:
                    print(f'''==========
ID: {user_id}
USERNAME: {username}
==========
''')
        elif command == '2':  # create
            print(texts.USER_SELECTED_COMMAND_TEXT[command])
            command_create = input(texts.USER_COMMAND_CREATE_TEXT)
            user_service.create(db, username=command_create)
        elif command == '3':  # update
            print(texts.USER_SELECTED_COMMAND_TEXT[command])
            command_update = input(texts.USER_COMMAND_UPDATE_TEXT)
        elif command == '4':  # delete
            print(texts.USER_SELECTED_COMMAND_TEXT[command])
            command_delete = input(texts.USER_COMMAND_DELETE_TEXT)

# этот файл в гите

# ssh-keygen - генерирует ключ для соединения с репозиторием
# git init - инициализиует гит в проекте
# git add . - добавляет все файлы проекта для прослушивания гитом
# git commit -m "commit message" - добавляет для добавленных файлов сообщение о том что мы сделали
# git status - показывает состояние текущих файлов

# todo ИПОЛЬЗУЮТСЯ ПРИ ПЕРВОМ ПОДКЛЮЧЕНИИ ГИТА
# git branch -M master - создает главную ветку с названием master
# git remote add origin <ссылка до репозитория> - соединяет репозиторий и инициализированный гит
# git push -u origin master - добавляет файлы в репозиторий
