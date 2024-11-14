from vpython import *

scene = canvas(title="Particle Showcase")

boxed = box(length=10,height=10, width=10,
            opacity=0.5, color=color.white)

particle = 10
prt = []
for i in range(particle):
    prt.append(sphere(pos=vector.random()*5, radius=0.5, color=color.red))

for p in prt:
    p.velocity = vector.random()*2

l1 = local_light(pos=vector(5,5,5), color=color.yellow)
l2 = local_light(pos=vector(-5,-5,-5), color=color.cyan)
dt = 0.05
theta = 0
while True:
    rate(30)
    for p in prt:
        p.pos += p.velocity * dt
        if abs(p.pos.x) > boxed.length/2 - p.radius:
            p.velocity.x *= -1
        if abs(p.pos.y) > boxed.length/2 - p.radius:
            p.velocity.y *= -1
        if abs(p.pos.z) > boxed.length/2 - p.radius:
            p.velocity.z *= -1
    theta += 0.02
    scene.camera.pos = vector(12*cos(theta),12*(sin(theta)),12*cos(theta))
    scene.camera.axis = -scene.camera.pos