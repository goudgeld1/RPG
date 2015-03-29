import bge, math, random

# Frequently used variables
curScene = bge.logic.getCurrentScene()
curCont = bge.logic.getCurrentController()
scenes = bge.logic.getSceneList()

forwardSpeed = 0.06     #0.08
backwardSpeed = 0.04    #0.06
leftSpeed = 0.02        #0.04
rightSpeed = 0.02       #0.04

# Get the Objects
fpView = curScene.objects["FpView"]
tpView = curScene.objects["TpView"]
player = curScene.objects["Player"]
rayVector = curScene.objects["RayVector"]

# Get keyboard input
aKeyDown = bge.logic.keyboard.events[bge.events.AKEY] == bge.logic.KX_INPUT_ACTIVE
aKeyJustUp = bge.logic.keyboard.events[bge.events.AKEY] == bge.logic.KX_INPUT_JUST_RELEASED

dKeyDown = bge.logic.keyboard.events[bge.events.DKEY] == bge.logic.KX_INPUT_ACTIVE
dKeyJustUp = bge.logic.keyboard.events[bge.events.DKEY] == bge.logic.KX_INPUT_JUST_RELEASED

eKeyDown = bge.logic.keyboard.events[bge.events.EKEY] == bge.logic.KX_INPUT_ACTIVE
eKeyJustUp = bge.logic.keyboard.events[bge.events.EKEY] == bge.logic.KX_INPUT_JUST_RELEASED

qKeyJustDown = bge.logic.keyboard.events[bge.events.QKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED

sKeyDown = bge.logic.keyboard.events[bge.events.SKEY] == bge.logic.KX_INPUT_ACTIVE
sKeyJustUp = bge.logic.keyboard.events[bge.events.SKEY] == bge.logic.KX_INPUT_JUST_RELEASED

vKeyJustDown = bge.logic.keyboard.events[bge.events.VKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED

wKeyDown = bge.logic.keyboard.events[bge.events.WKEY] == bge.logic.KX_INPUT_ACTIVE
wKeyJustUp = bge.logic.keyboard.events[bge.events.WKEY] == bge.logic.KX_INPUT_JUST_RELEASED

shiftKeyDown = bge.logic.keyboard.events[bge.events.LEFTSHIFTKEY] == bge.logic.KX_INPUT_ACTIVE

spaceKeyDown = bge.logic.keyboard.events[bge.events.SPACEKEY] == bge.logic.KX_INPUT_ACTIVE
spaceKeyJustDown = bge.logic.keyboard.events[bge.events.SPACEKEY] == bge.logic.KX_INPUT_JUST_ACTIVATED

# Get mouse input
lMouseDown = bge.logic.mouse.events[bge.events.LEFTMOUSE] == bge.logic.KX_INPUT_ACTIVE

# Change the camera view when pressing the v key
if vKeyJustDown:
    if curScene.active_camera.name == "FpView":
        curScene.active_camera = tpView
        # Remove the HUD
        if player["HUD"]:
            Scene = player.actuators["Scene"]
            Scene.mode = 6
            Scene.scene = "HUD"
            curCont.activate("Scene")
    elif curScene.active_camera.name == "TpView":
        curScene.active_camera = fpView
        # Add the HUD
        if player["HUD"]:
            Scene = player.actuators["Scene"]
            Scene.mode = 4
            Scene.scene = "HUD"
            curCont.activate("Scene")
        
# Activate the neutral animation
curCont.activate("Neutral")

# Movement logic
# Move forwards
if wKeyDown and shiftKeyDown:
    player.applyMovement((0, forwardSpeed*2, 0),True)
    curCont.activate("Walk")
elif wKeyDown:
    player.applyMovement((0, forwardSpeed, 0),True)
    curCont.activate("Walk")
else:
    curCont.deactivate("Walk")

# Move backwards
if sKeyDown and shiftKeyDown:
    player.applyMovement((0, -backwardSpeed*2, 0),True)
    curCont.activate("Walk")
elif sKeyDown:
    player.applyMovement((0, -backwardSpeed, 0),True)
    curCont.activate("Walk")
else:
    curCont.deactivate("Walk")

# Move left
if aKeyDown and shiftKeyDown:
    player.applyMovement((-leftSpeed*2, 0, 0),True)
    curCont.activate("Sideways")
elif aKeyDown:
    player.applyMovement((-leftSpeed, 0, 0),True)
    curCont.activate("Sideways")
else:
    curCont.deactivate("Sideways")

# Move right
if dKeyDown and shiftKeyDown:
    player.applyMovement((rightSpeed*2, 0, 0),True)
    curCont.activate("Sideways")
elif dKeyDown:
    player.applyMovement((rightSpeed, 0, 0),True)
    curCont.activate("Sideways")
else:
    curCont.deactivate("Sideways")

# Jump
if curCont.sensors["GroundCollision"].positive and curCont.sensors["Jump"].positive:
    curCont.activate("Jump")
curCont.deactivate("Jump")

# Drop the wood you collected
if qKeyJustDown and player["hout"] > 0:
    Eikenhout001 = curScene.objectsInactive["Eikenhout001"]
    OPE = curScene.objectsInactive["ObjectPlacementEmpty"]

    OPE.position = rayVector.position

    OPE.orientation = (random.randint(0, 360), random.randint(0, 360), random.randint(0, 360))
    curScene.addObject(Eikenhout001, OPE, 0)
    player["hout"] -= 1


# Correct gravity for the player
if curCont.sensors["GroundCollision"].positive:
    player.applyForce([0, 0, 9.8 * player.mass], False)
else:
    player.applyForce([0, 0, -9.8 * player.mass], False)

#start ray caster
rayVector.localPosition = [0, 0, -3]

hit, point, normal = fpView.rayCast(rayVector, None, 3)

q = fpView.position

if hit:
    player["lookingAt"] = hit.name
    player["d"] = math.sqrt(math.pow(point[0]-q[0], 2)+math.pow(point[1]-q[1], 2)+math.pow(point[2]-q[2], 2))
    
    if hit["Type"] == "Boom":
        
        scenes[1].objects["ToolTip"].text = "Left Mouse to cut tree"
        
        if lMouseDown:
            Eikenboomstronk001 = curScene.objectsInactive["Eikenboomstronk001"]
            Eikenhout001 = curScene.objectsInactive["Eikenhout001"]
            OPE = curScene.objectsInactive["ObjectPlacementEmpty"]
            
            OPE.position = hit.position
            
            hit2, point2, normal2 = OPE.rayCast([OPE.position[0], OPE.position[1], 0], OPE.position, 3, "Grond", 1, 1)
            
            if hit2:
                hit.endObject()
                OPE.orientation = (random.randint(0, 360), random.randint(0, 360), random.randint(0, 360))
                curScene.addObject(Eikenhout001, OPE, 0)
                OPE.position = (OPE.position[0], OPE.position[1], point2[2]+0.1)
                OPE.orientation = (0, 0, random.randint(0, 360))
                curScene.addObject(Eikenboomstronk001, OPE, 0)
    elif hit["Type"] == "Hout":
        
        scenes[1].objects["ToolTip"].text = "Press E to take the wood"
        
        if eKeyDown:
            hit.endObject()
            player["hout"] += 1
    elif hit["Grond"]:
        scenes[1].objects["ToolTip"].text = ""
else:
    player["lookingAt"] = ""
    player["d"] = 0
    
    try:
        scenes[1].objects["ToolTip"].text = ""
    except:
        pass