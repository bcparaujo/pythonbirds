class Pessoa:
    olhos = 2 #Atributo de classe

    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Mulher(Pessoa):
    def cumprimentar(self):
        cumprimentar_classe_pai = super().cumprimentar() #Acessa os atributos da classe pai
        return f'{cumprimentar_classe_pai}. Beijo na bochecha.'

class Homem(Pessoa):
    def cumprimentar(self):
        return 'Aperto de mão.'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    lorenzo = Homem(nome='Lorenzo', idade=3)
    bruna = Mulher(lorenzo,nome='Bruna', idade=24)
    cleo = Mutante(nome = 'Cleo', idade = 46)
    print()
    print(Pessoa.cumprimentar(bruna))
    print()
    print(f'Nome da Mãe: {bruna.nome} - Idade da Mãe: {bruna.idade}\nNome do Filho: {lorenzo.nome} - Idade do Filho: {lorenzo.idade}')
    print()
    for filho in bruna.filhos:
        print(f'Filhos do(a) {bruna.nome}:\n{filho.nome}')
    print()
    bruna.sobrenome =  'Araujo' #Incluir atributo em tempo de execução (dinâmico)
    del bruna.filhos #Remover atributo em tempo de execução (dinâmico)
    bruna.olhos = 1
    del bruna.olhos
    print(bruna.__dict__) #Apenas atributos de instância
    print(lorenzo.__dict__) #Apenas atributos de instância
    print()
    print(f'As pessoas possuem  {Pessoa.olhos} olhos')
    print(Pessoa.metodo_estatico(), bruna.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), bruna.nome_e_atributos_de_classe())
    print()
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(bruna, Pessoa))
    print(isinstance(bruna, Mulher))
    print()
    print(f'A(o) {cleo.nome} possue {cleo.olhos} olhos')
    print()
    print(bruna.cumprimentar())
    print(lorenzo.cumprimentar())
    print(cleo.cumprimentar())
