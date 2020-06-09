from models import Pessoa
from models import Usuario

def insere_pessoa(nome, idade):
    pessoa = Pessoa(nome=nome, idade=idade)
    pessoa.save()

def consulta_pessoa(nome):
    pessoa = Pessoa.query.all()
    print(pessoa)
    pessoa = Pessoa.query.filter_by(nome=nome).first()
    print(pessoa)

def altera_pessoa():
    pessoa = Pessoa.query.filter_by(nome='Nike').first()
    pessoa.nome = 'Nei'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoa.query.filter_by(nome='fulano').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuario(login=login, senha=senha)
    usuario.save()

def consulta_usuario():
    usuario = Usuario.query.all()
    print(usuario)

def exclui_usuario():
    usuario = Usuario.query.filter_by(nome='Dutra').first()
    usuario.delete()

if __name__ == '__main__':
    #insere_pessoa('Nethodu', '47')
    #consulta_pessoa('Nethodu')
    #altera_pessoa()
    #exclui_pessoa()
    #insere_usuario('fulano', '999')
    #consulta_usuario()
    #exclui_usuario()