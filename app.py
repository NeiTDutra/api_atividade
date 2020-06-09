from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoa, Atividade, Usuario
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# USUARIOS = {
#     'admin':'123',
#     'root':'321'
# }

@auth.verify_password
def verifica(login, senha):
    if not (login, senha):
        return False
    return Usuario.query.filter_by(login=login, senha=senha).first()

class Pessoap(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoa.query.filter_by(nome=nome).first()
        response = {
            'nome':pessoa.nome,
            'idade':pessoa.idade,
            'id':pessoa.id
        }
        return response

    def put(self, nome):
        pessoa = Pessoa.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

    def delete(self, nome):
        pessoa = Pessoa.query.filter_by(nome=nome).first()
        mensagem = 'Registro de {} deletado'.format(pessoa.nome)
        pessoa.delete()
        return { 'status':'Sucesso', 'mensagem':mensagem}

class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoa.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoa(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

class ListaAtividades(Resource):
    @auth.login_required
    def get(self):
        atividades = Atividade.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoa.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividade(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa':atividade.pessoa.nome,
            'atividade':atividade.nome,
            'id':atividade.id
        }
        return response

api.add_resource(Pessoap, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)