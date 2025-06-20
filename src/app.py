from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
#ruta para el GET
@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

#ruta para el POST
@app.route('/todos', methods=['POST'])
def add_new_todo():
   request_body = request.json
   todos.append(request_body)
   print('Incoming request with the fallowing body', request_body)
   return jsonify(todos)

#Ruta para el DELETE
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
   todos.pop(position)
   print("This is the position to delete:", position)
   return jsonify(todos)







if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)