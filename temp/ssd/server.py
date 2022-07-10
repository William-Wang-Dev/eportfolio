import time
from flask import Flask, send_file
from flask import request as FlaskRequest
from werkzeug.datastructures import FileStorage

server = Flask(__name__)
# server['UPLOAD_FOLDER'] = r'D:\MyPrograms\MicroserviceWithFlask\server\temp'

@server.route('/')
def hello():
    return "hello, world!"

@server.route('/task/<task_name>')
def reply(task_name):
    print(f'task = {task_name}')
    print(f'receive task as {FlaskRequest.form}')
    print(f'args could be {FlaskRequest.args}')
    return r"I received your task."

@server.route('/upload/<arg>', methods=['POST', 'GET'])
def upload_file(arg):
    print(f"args = {arg}")
    print(r"receive upload request")

    if 'file' not in FlaskRequest.files:
        print(r"no file parameter in upload request.")
        return r"empty file", 400
    
    received_file = FlaskRequest.files['file']
    file_name = FlaskRequest.args.get('file_name')
    if not file_name:
        file_name = str(time.time_ns()) + ".save"
    
    # TODO: investigate why FileStorage cant be working
    # FileStorage(FlaskRequest.stream).save(f"D:\\MyPrograms\\MicroserviceWithFlask\\server\\{file_name}")
    # you can change where to save the received file
    received_file.save(f"D:\\MyPrograms\\MicroserviceWithFlask\\server\\{file_name}")
    return r'upload done!', 200


@server.route('/download/<file_name>', methods=['GET'])
def download_file(file_name):
    print(f"args = {file_name}")
    print(r"receive download request")
    # return r'download done!', 200
    return send_file(r'D:\MyPrograms\MicroserviceWithFlask\server\temp\eva.mp3')


if __name__ == "__main__":
    # server.run(host="127.0.0.1", port=8080, ssl_context='adhoc')
    server.run(host="127.0.0.1", port=8080, debug=True)