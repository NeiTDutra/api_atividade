from models import Pessoa

def insere():
    pessoa = Pessoa(nome='Nike', idade='47')
    pessoa.save()

def consulta():
    pessoa = Pessoa.query.all()
    print(pessoa)

if __name__ == '__main__':
    insere()
    consulta()