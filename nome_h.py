# coding: utf-8
import random


def nome_h(nomeh):

  random.seed(nomeh)

  nome = random.randint(0,len(nomes))

  nomeh = nomes[nome]

  print(nomeh)

  return nomeh

nomes = [
  "Miguel",
  "Davi",
  "Arthur",
  "Pedro",
  "Gabriel",
  "Bernardo",
  "Lucas",
  "Matheus",
  "Rafael",
  "Heitor",
  "Enzo",
  "Guilherme",
  "Nicolas",
  "Lorenzo",
  "Gustavo",
  "Felipe",
  "Samuel",
  "João Pedro",
  "Daniel",
  "Vitor",
  "Leonardo",
  "Henrique",
  "Theo",
  "Murilo",
  "Eduardo",
  "Pedro Henrique",
  "Pietro",
  "Cauã",
  "Isaac",
  "Caio",
  "Vinicius",
  "Benjamin",
  "João",
  "Lucca",
  "João Miguel",
  "Bryan",
  "Joaquim",
  "João Vitor",
  "Thiago",
  "Antônio",
  "Davi Lucas",
  "Francisco",
  "Enzo Gabriel",
  "Bruno",
  "Emanuel",
  "João Gabriel",
  "Ian",
  "Davi Luiz",
  "Rodrigo",
  "Otávio",
  "Miguel",
  "Artur",
  "Gabriel",
  "Bernardo",
  "Guilherme",
  "Pedro",
  "Lucas",
  "Gustavo",
  "Bryan",
  "Henrique",
  "Rafael",
  "David",
  "Mateus",
  "Theo",
  "Enzo",
  "Nicolas",
  "Heitor",
  "Caio",
  "Felipe",
  "Victor",
  "Daniel",
  "Yuri",
  "Eduardo",
  "Benjamim",
  "Bruno",
  "Tiago",
  "João",
  "Samuel",
  "Lorenzo",
  "Leonardo",
  "Igor",
  "Diogo",
  "Hugo",
  "Vinicios",
  "Rodrigo",
  "Tomás",
  "Luis",
  "Diego",
  "Augusto",
  "Kevin",
  "André",
  "Filipe",
  "Emanuel",
  "Danilo",
  "Fernando",
  "Alexandre",
  "Pablo",
  "Renan",
  "Levi",
  "Joaquim",
  "Alan",
  "Octávio",
  "Kelvin",
  "Marcelo",
  "Ricardo",
  "Leandro",
  "Calebe",
  "Francisco",
  "Jonathan",
  "Vicente",
  "Wilian",
  "Paulo",
  "Júlio",
  "António",
  "Douglas",
  "Fabrício",
  "Martim",
  "Afonso",
  "Lourenço",
  "Fábio",
  "Carlos",
  "Marcos",
  "Frederico",
  "Renato",
  "José",
  "Ângelo",
  "Raul",
  "Manuel",
  "Santiago",
  "Valentim",
  "César",
  "Jonas",
  "Michael",
  "Maurício",
  "Cristiano",
  "Jorge",
  "Edgar",
  "Ramom",
  "Álvaro",
  "Juliano",
  "Aquiles",
  "Adriano",
  "Anderson",
  "Alexander",
  "Ivan",
  "Marco",
  "Duarte",
  "Muriel",
  "Flávio",
  "Aarã"
]


nome_h('joao costa')

nome_h('pedro arroba')