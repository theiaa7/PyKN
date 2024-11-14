from numpy.ma.core import angle
from vpython import *

sub = sphere(
    pos=vector(0,0,0),
    radius=5,
    color=color.yellow
)

planet = sphere(
    pos=vector(45,0,0),
    radius=1,
    color=color.blue,
    make_trail=True
)

orbit_radius = mag(planet.pos)
orbit_speed = 0.05
orbit_angle = 90

while True:
    rate(100)
    planet.pos = vector(orbit_radius*cos(orbit_angle), orbit_radius*sin(orbit_angle),0)
    orbit_angle += orbit_speed