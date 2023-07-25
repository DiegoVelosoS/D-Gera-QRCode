from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

ground = Entity(model='cube',
                color=color.green,
                texture="grass",
                scale_x=60,
                scale_y=1,
                position=(0,-4,0),
                collider='box')

player = PlatformerController2d(scale_y=2,
                                position=(0,-1,0))


app.run()