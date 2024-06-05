Для запуска задания откройте файл main.py и запустите его. В нем есть связи с файлами user.py и twit.py (сущности в задании).
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
@app.route('/twit/', methods=['DELETE'])
def delete_twit():
    pass