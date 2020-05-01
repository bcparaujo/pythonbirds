class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())
    p.nome = 'Bruna'
    p.idade = '24'
    print(f'Nome: {p.nome} - Idade: {p.idade}')