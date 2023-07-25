from ursina import *

app = Ursina()

# skybox = load_texture('local da imagem')

cenario = Entity(parent=camera.ui, model='quad', texture= 'sky_sunset', scale_x=camera.aspect_ratio, z=1)
# camera.ui é para ter uma camera no cenario
# quad é o quadrado
# texture é a variavel de textura, na própria biblioteca do ursina tem texturas de modelo
# camera.aspect_ratio é para termos uma tamanho correto
# z=1 é para ter uma distancia aceitavel para vermos

app.run()