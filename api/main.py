from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/<int:id>')
def pessoas(id):
    return jsonify({'id': id,
                    'nome': 'Joao',
                    'idade': '33',
                    'nacionalidade': 'Brasil'})


# @app.route('/soma/<int:valor1>/<int:valor2>')
# def soma(valor1, valor2):
#     return jsonify({'total': valor1 + valor2})


@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    else:
        total = 10 + 10
    return jsonify({'soma':total})


if __name__ == '__main__':
    app.run(debug=True)
