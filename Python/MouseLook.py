from bge import logic as g, render as r

c = g.getCurrentController()
o = c.owner

m = c.sensors["MouseLook"]

p = o.parent

w1 = r.getWindowHeight()
w2 = r.getWindowWidth()

h1 = w1//2
h2 = w2//2

s = 0.005

x, y = m.position

x = (h1 - x)*s
y = (h2 - y)*s

if x > 0.1:
    x = 0.1
elif x < -0.1:
    x = -0.1
if y > 0.1:
    y = 0.1
elif y < -0.1:
    y = -0.1

import mathutils
camOrient = o.localOrientation
camZ = [camOrient[0][2],camOrient[1][2],camOrient[2][2]]
vec1 = mathutils.Vector(camZ)
camParent = p
parentZ = [0,0,1]
vec2 = mathutils.Vector(parentZ)
rads = mathutils.Vector.angle(vec2, vec1)
angle = rads * (180.00 / 3.14)
capAngle = 160
moveY = y
if (angle > (90 + capAngle/2) and moveY > 0)   or (angle < (90 - capAngle/2) and moveY < 0)  == True:
    y = 0

o.applyRotation([y,0,0],True)
g.getCurrentScene().objects["Player"].applyRotation([0,0,x],False)

g.getCurrentScene().objects["TpRotationPoint"].applyRotation([y,0,0],True)
#g.getCurrentScene().objects["TpRotationPoint"]


r.setMousePosition(h1, h2)