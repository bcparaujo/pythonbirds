class Pessoa:
    olhos = 2 #Atributo de classe

    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    lorenzo = Pessoa(nome='Lorenzo', idade=3)
    bruna = Pessoa(lorenzo,nome='Bruna', idade=24)
    print(bruna.cumprimentar(), bruna.nome)
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