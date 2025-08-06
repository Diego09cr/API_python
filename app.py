from flask import Flask, jsonify, request
app = Flask(__name__)
usuarios = {}
usuarios_id = 1

@app.route('/home', methods=['GET'])
def show():
    return jsonify({'API': 'ON'})

@app.route('/usuario', methods=['POST'])
def pega_usu():
    global usuarios_id
    dados = request.get_json()
    usuario = {
        'id': usuarios_id,
        'nome': dados.get('nome'),
        'email': dados.get('email')
    }
    usuarios[usuarios_id] = usuario
    usuarios_id += 1
    return jsonify(usuario), 201

@app.route('/usuario/<int:id>', methods=['GET'])
def get_id(id):
    usuario = usuarios.get(id)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'Erro': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)