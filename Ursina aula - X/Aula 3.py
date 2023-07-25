from ursina import *

app = Ursina()

ground = Entity(model='cube', color=color.green, texture="grass", scale_x=60, scale_y=1, position=(0,-4,0))
# criamos uma var para o chão
# model cubo
# color é a cor
# texture é a variavel de textura, na própria biblioteca do ursina tem texturas de modelo
# scale_x é o tamanho do cubo no eixo x
# scale_y é o tamanho do cubo no eixo y
# position é a posição do cubo

app.run()