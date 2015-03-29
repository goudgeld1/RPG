import bge, random, time

curScene = bge.logic.getCurrentScene()
curCont = bge.logic.getCurrentController()

Eikenboom001 = curScene.objectsInactive["Eikenboom001"]
OPE = curScene.objectsInactive["ObjectPlacementEmpty"]
    
OPE.position = [curCont.owner.position[0], curCont.owner.position[1], curCont.owner.position[2]]

OPE.position = (OPE.position[0], OPE.position[1], OPE.position[2]+1.9)
OPE.orientation = (0, 0, random.randint(0, 360))
curScene.addObject(Eikenboom001, OPE, 0)
curCont.owner.endObject()