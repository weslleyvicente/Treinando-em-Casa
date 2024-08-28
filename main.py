nome = input("Digite seu nome: ")
idade =  int (input("Digite sua idade: "))
altura = float (input("Digite sua altura: "))
peso = float (input("Digite seu peso: "))

print(nome)
print(idade)
print(type (altura))
print(type( peso))




## Informações do meu personagem
## alt + shift e setinha pra baixo, faz copiar as linhas

PLAYER ={
    "nome": "Sync",
    "level": 10,
    "hp": 340,
    "exp": 1040,
    "dano": 500
}

##informações dos inimigos

npcs = [
    
    { "nome": "Monstrinho", "dano": 2, "hp": 50, "exp": 5},
    { "nome": "Monstro", "dano": 5, "hp": 100, "exp": 10},
    { "nome": "Monstrão", "dano": 10, "hp": 150, "exp": 15},
    { "nome": "Chefão", "dano": 25, "hp": 200, "exp": 20}
]





for index in range(1, 50, 2):
    print(index)