from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers = [
    {
     'id': 0,
     'name': 'Robert',
     'skills': ['Python',
                'Flask',
                'Django',
                'API',
                'HTML5',
                'CSS3',
                'JavaScript',
                'MySQL',
                'UX/UI']},
    {
     'id': 1,
     'name': 'Vinicius',
     'skills': ['C',
                'C#',
                'Java',
                'HTML5',
                'CSS3',
                'Angular.js',
                'Node.js',
                'UX/UI',
                'JavaScript',
                'Figma']},
    {
     'id': 2,
     'name': 'Aryane',
     'skills': ['JavaScript',
                'CSS3',
                'Angular.js',
                'Node.js',
                'TypeScript',
                'React',
                'UX/UI']},
]


#
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def dev(id):
    """
    :param id: Recebe o id de um dev e com isso é possível alterar skills ou deletar o dev
    :return: retorna os dados com o nome e as habilidades de um dev
    """
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            response = {'status': 'negado', 'mensagem': 'Indice inexistente'}
        return jsonify(response)
    elif request.method == 'PUT':
        info_dev = json.loads(request.data)
        developers[id] = info_dev
        return jsonify(info_dev)
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluído'})


@app.route('/dev/', methods=['POST', 'GET'])
def developers_list():
    """
    :return: Retorna um arquivo json com os dados do novo dev que foi inserido
    """
    if request.method == 'POST':
        new_dev = json.loads(request.data)
        position = len(developers)
        new_dev['id'] = position
        developers.append(new_dev)
        return jsonify(developers[position])
    elif request.method == 'GET':
        return jsonify(developers)


if __name__ == '__main__':
    app.run(debug=True)
