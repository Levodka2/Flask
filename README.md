# Flask project for ProductStar. 
# "Creating REST API providing blogging capabilities"

Для работы с проектом, откройте редактор и установите виртуальное окружение. Для этого введите в терминале python -m venv venv. В результате будет создан каталог venv/ содержащий копию интерпретатора Python, стандартную библиотеку и другие вспомогательные файлы. Все новые пакеты будут устанавливаться в venv/lib/python3.x/site-packages/. Чтобы начать пользоваться виртуальным окружением, необходимо его активировать: путь "venv\Scripts\activate.bat" - для Windows; "source venv/bin/activate" - для Linux и MacOS. Source выполняет bash-скрипт без запуска дополнительного bash-процесса. Проверить успешность активации можно по приглашению оболочки. Она будет выглядеть так: (venv) root@purplegate:/var/test# (в терминале). Также новый путь до библиотек можно увидеть выполнив команду: python -c "import site; print(site.getsitepackages())" (в терминале).

В проекте обязательно наличие установленного Flask 3. Для его установки откройте терминал, в нем напишите команду pip install flask и запустите.
Все зависимости проекта "Creating REST API providing blogging capabilities" находятся в файле requiments.txt, можете установить их с помощью команды pip install -r requirements.txt.

Для начала работы в проекте откройте файл main.py и запустите сервер (к примеру с терминала командой python main.py). В файле main.py есть связи с файлами user.py и twit.py (сущности в блоге).

Файл main.py реализует операции, представленные в виде HTTP методов:

1) POST /twit/add HTTP/1.1
@app.route('/twit', methods=['POST'])  #  Функция создание твита
def create_twit():
    pass

2) PUT /twit/1 HTTP/1.1
@app.route('/twit/', methods=['PUT'])  # Функция изменения твита
def update_twit():
    pass

3) GET /twit/1 HTTP/1.1
@app.route('/twit', methods=['GET'])  #Функция на просмотр всех твитов
def read_twit():
    pass

4) DELETE /twit/1 HTTP/1.1
@app.route('/twit/', methods=['DELETE']) # Функция удаления твита
def delete_twit():
    pass

# Тестирование: 

1) POST http://127.0.0.1:5000/twit
   
   REQUESTS:
   {"id": 1, "body": "body 1", "author": "@levodka2"}
   {"id": 2, "body": "body 2", "author": "@levodka2"}
   
   RESPONSES:
   {
    "status": "success"
   }
   
   {
    "status": "success"
   }


2) GET  http://127.0.0.1:5000/twit
   
   RESPONSE:
   {
    "twits": [
        {
            "author": "@levodka2",
            "body": "body 2",
            "id": 2
        },
        {
            "author": "@levodka2",
            "body": "body 1",
            "id": 1
        }
    ]
}

3) PUT http://127.0.0.1:5000/twit
   
   REQUEST:

   {"id": 1, "body": "NEW BODY", "author": "@levodka2"}

  RESPONSE:
  {
    "status": "success"
  }

4) DELETE http://127.0.0.1:5000/twit

  REQUEST:
   
   {"id": 1, "body": "NEW BODY", "author": "@levodka2"}
   
  RESPONSE:
  
  {
    "status": "success"
  }

5)  GET  http://127.0.0.1:5000/twit
   
   RESPONSE: 
   
   {
    "twits": [
        {
            "author": "@levodka2",
            "body": "body 2",
            "id": 2
        }
    ]
}
