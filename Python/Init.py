import bge, random

# Frequently used variables
curScene = bge.logic.getCurrentScene()
curCont = bge.logic.getCurrentController()
player = curScene.objects["Player"]
seed = 256    #256

# Add the HUD if in FpView
if curScene.active_camera.name == "FpView":
    if player["HUD"]:
        Scene = player.actuators["Scene"]
        Scene.mode = 4
        Scene.scene = "HUD"
        curCont.activate("Scene")

# Get the Objects
Eikenboom001 = curScene.objectsInactive["Eikenboom001"]
Eikenboom002 = curScene.objectsInactive["Eikenboom002"]
BessenStruik001 = curScene.objectsInactive["BessenStruik001"]
OPE = curScene.objectsInactive["ObjectPlacementEmpty"]

# Init the pseudo-random number generator
random.seed(seed)

# Place Eikenboom001
for x in range(0, 1024):
    OPEPosition = [random.uniform(-128, 128), random.uniform(-128, 128), 99]
    
    OPE.position = OPEPosition
    
    hit, point, normal = OPE.rayCast([OPEPosition[0], OPEPosition[1], 0], OPEPosition, 100)

    if hit:
        if hit["Type"] == "Grond":
            OPE.position = (OPEPosition[0], OPEPosition[1], point[2]+2)
            OPE.orientation = (0, 0, random.randint(0, 360))
            curScene.addObject(Eikenboom001, OPE, 0)

# Place Eikenboom002
for x in range(0, 512):
    OPEPosition = [random.uniform(-128, 128), random.uniform(-128, 128), 99]
    
    OPE.position = OPEPosition
    
    hit, point, normal = OPE.rayCast([OPEPosition[0], OPEPosition[1], 0], OPEPosition, 100)

    if hit:
        if hit["Type"] == "Grond":
            OPE.position = (OPEPosition[0], OPEPosition[1], point[2]+2)
            OPE.orientation = (0, 0, random.randint(0, 360))
            curScene.addObject(Eikenboom002, OPE, 0)

# Place BessenStruik001
for x in range(0, 32):
    OPEPosition = [random.uniform(-128, 128), random.uniform(-128, 128), 99]
    
    OPE.position = OPEPosition
    
    hit, point, normal = OPE.rayCast([OPEPosition[0], OPEPosition[1], 0], OPEPosition, 100)

    if hit:
        if hit["Type"] == "Grond":
            OPE.position = (OPEPosition[0], OPEPosition[1], point[2]+0.75)
            OPE.orientation = (0, 0, random.randint(0, 360))
            curScene.addObject(BessenStruik001, OPE, 0)