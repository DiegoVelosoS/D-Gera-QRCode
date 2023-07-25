from ursina import *

app = Ursina()
# app é a tela na ursina

player = Entity(model="cube", color=color.orange, scale_y=2)
# player é a variavel q atribuimos
# movimentando para frente e p trás
# color é a cor
# scale_y é o tamanho do cubo no eixo y

def update():
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['a'] * time.dt

# update é para fazer atualizar a imagem em relação a tela
# Help_keys é para saber qual tecla foi pressionada
# time.dt é para manter a atualização refetente ao tempo

# fazendo o pulo
def input(key):
    if (key == 'space'):
        player.y += 1
        invoke (setattr, player, 'y', player.y-1, delay= .25)
# o player não sobe ou desce com coomandos, ele pula
# o if é a condição de execusão do comando
# invoke é para retornar outro comando 

app.run()
# app.run abre a tela