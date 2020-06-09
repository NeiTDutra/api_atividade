from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoa, Atividade

app = Flask(__name__)
api = Api(app)

class Pessoap(Resource):
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
        pessoa = Pessoa.query.filter_by(nome=nome).firs()
        mensagem = 'Registro de {} deletado'.format(pessoa.nome)
        pessoa.delete()
        return { 'status':'Sucesso', 'mensagem':mensagem}

class ListaPessoas(Resource):
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