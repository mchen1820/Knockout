#Michael Chen
#Knockout

from cmu_graphics import *
from buttons import *
import math
import random

def onAppStart(app):
    app.stepsPerSecond = 100

    app.width = 800
    app.height = 700
    app.startBackgroundColor = 'skyBlue'
    app.gameBackgroundColor = 'lightSkyBlue'

    app.dragFrictionSlider = False #only for settings page; true if user dragging friction slider
    app.dragSpeedSlider = False
    app.dragp1MassSlider = False
    app.dragp2MassSlider = False
    app.speedMultiplier = 2
    app.friction = 2

    app.platformColor = 'lightCyan'
    app.platformLeft = 150
    app.platformTop = 100
    app.platformWidth = 500
    app.platformHeight = 500

    app.seals = []
    app.numP1Seals = 4
    app.p1Mass = 1
    app.numP2Seals = 4
    app.p2Mass = 1

    app.mode = '2p'
    app.p1Turn = True
    app.p2Turn = False
    app.bothReady = False
    app.actionPhase = False
    app.prepPhase = True

    app.win = ''

def start_redrawAll(app):
    drawRect(0,0, app.width, app.height, fill = app.startBackgroundColor)
    drawLabel('Knockout!', app.width/2, app.height/4, size = 140, fill = 'white', font = 'montserrat', bold = True)
    drawRect(app.width/2, app.height/2, app.width/3, 60, fill = 'lightSkyBlue', border = 'white', align = 'center')
    drawLabel('Instructions', app.width/2, app.height/2, size = 32, fill = 'white', font = 'montserrat', bold = True)
    drawRect(app.width/2, app.height*0.62, app.width/3, 60, fill = 'lightSkyBlue', border = 'white', align = 'center')
    drawLabel('Play', app.width/2, app.height*0.62, size = 32, fill = 'white', font = 'montserrat', bold = True)
    drawRect(app.width/2, app.height*0.74, app.width/3, 60, fill = 'lightSkyBlue', border = 'white', align = 'center')
    drawLabel('Settings', app.width/2, app.height*0.74, size = 32, fill = 'white', font = 'montserrat', bold = True)

def start_onMousePress(app, mouseX, mouseY):
    if pressedInstructions(app, mouseX, mouseY):
        setActiveScreen('instructions')
    elif pressedPlay(app, mouseX, mouseY):
        setActiveScreen('chooseMode')
    elif pressedSettings(app, mouseX, mouseY):
        setActiveScreen('settings')

def instructions_redrawAll(app):
    drawRect(0,0, app.width, app.height, fill = app.startBackgroundColor)
    drawLabel('Instructions', app.width/2, app.height/6, size = 50, fill = 'white', font = 'montserrat', bold = True)
    drawRect(app.width/2, app.height/2, app.width*3/4, app.height/2, fill = 'lightSkyBlue', border = 'white', align = 'center')
    instructionParagraph = '''
         Welcome to Knockout! In this game, there are two teams
    of seals competing to be the last ones standing on an icy
    platform. In the PVP mode, first find a friend to play with.
    You'll take turns with the computer during the planning
    phase, strategically dragging arrows from your seals that
    represent how they'll slide (hopefully knocking off opposing
    seals!). Hide the screen while you're dragging the arrows!
    When you're done, press Ready. Once both of you are done
    and have pressed Ready, press Launch to see the seals
    slide and collide in the action phase! The bot mode is the
    same, except you play against a bot that automatically
    finishes its planning phase after you press Ready. The game
    continues until all of one team's seals have been knocked off!
    '''
    
    lineCounter = 0
    for line in instructionParagraph.splitlines():
        drawLabel(line, app.width/8.5, app.height/3.54 + 22*lineCounter, size = 19, fill = 'white', bold = True, font = 'montserrat', align = 'left')
        lineCounter += 1

    drawRect(app.width/2, app.height*0.85, app.width/4, 50, fill = 'lightSkyBlue', border = 'white', align = 'center')
    drawLabel('Return', app.width/2, app.height*0.85, size = 30, fill = 'white', font = 'montserrat', bold = True)

def instructions_onMousePress(app, mouseX, mouseY):
    if pressedReturn(app, mouseX, mouseY, 'instr'):
        setActiveScreen('start')

def settings_redrawAll(app):
    drawRect(0,0, app.width, app.height, fill = app.startBackgroundColor)
    drawRect(app.width/2, app.height/2, app.width*3/4, app.height*3/4, fill = 'lightSkyBlue', border = 'white', align = 'center')
    drawLabel('Settings', app.width/2, 50, size = 40, fill = 'white', font = 'montserrat', bold = True)
    #Friction slider:
    drawLabel('Friction Multiplier: affects how fast the seals slow down', app.width*0.5, app.height*0.18, size = 20, fill = 'white', font = 'montserrat', bold = True)
    drawLine(app.width/4, app.height*0.24, app.width*3/4, app.height*0.24, lineWidth = 5, fill = 'white')
    drawRect(app.width/4 * app.friction, app.height*0.24, 15, 30, align = 'center', fill =  app.startBackgroundColor, border = 'white')
    drawRect(app.width/2, app.height*0.3, 75, 25, align = 'center', fill = 'white')
    drawLabel(f'x{app.friction}', app.width/2, app.height*0.3, size = 18, fill = 'black', font = 'montserrat')
    #Speed slider:
    drawLabel('Speed Multiplier: affects the speed seals start with', app.width*0.5, app.height*0.36, size = 20, fill = 'white', font = 'montserrat', bold = True)
    drawLine(app.width/4, app.height*0.42, app.width*3/4, app.height*0.42, lineWidth = 5, fill = 'white')
    drawRect(app.width/4 * app.speedMultiplier, app.height*0.42, 15, 30, align = 'center', fill =  app.startBackgroundColor, border = 'white')
    drawRect(app.width/2, app.height*0.48, 75, 25, align = 'center', fill = 'white')
    drawLabel(f'x{app.speedMultiplier}', app.width/2, app.height*0.48, size = 18, fill = 'black', font = 'montserrat')
    #Player 1 Seal Mass slider:
    drawLabel('Player 1: Mass of Each Seal', app.width*0.5, app.height*0.54, size = 20, fill = 'white', font = 'montserrat', bold = True)
    drawLine(app.width/4, app.height*0.6, app.width*3/4, app.height*0.6, lineWidth = 5, fill = 'white')
    drawRect(app.width/4 * app.p1Mass, app.height*0.6, 15, 30, align = 'center', fill =  app.startBackgroundColor, border = 'white')
    drawRect(app.width/2, app.height*0.65, 75, 25, align = 'center', fill = 'white')
    drawLabel(app.p1Mass, app.width/2, app.height*0.65, size = 18, fill = 'black', font = 'montserrat')
    #Player 2 Seal Mass slider:
    drawLabel('Player 2: Mass of Each Seal', app.width*0.5, app.height*0.71, size = 20, fill = 'white', font = 'montserrat', bold = True)
    drawLine(app.width/4, app.height*0.77, app.width*3/4, app.height*0.77, lineWidth = 5, fill = 'white')
    drawRect(app.width/4 * app.p2Mass, app.height*0.77, 15, 30, align = 'center', fill =  app.startBackgroundColor, border = 'white')
    drawRect(app.width/2, app.height*0.82, 75, 25, align = 'center', fill = 'white')
    drawLabel(app.p2Mass, app.width/2, app.height*0.82, size = 18, fill = 'black', font = 'montserrat')
    #Return Button
    drawRect(app.width/2, app.height*0.93, app.width/5, 50, fill = 'lightSkyBlue', border = 'white', align = 'center')
    drawLabel('Return', app.width/2, app.height*0.93, size = 30, fill = 'white', font = 'montserrat', bold = True)

def settings_onMousePress(app, mouseX, mouseY):
    if pressedReturn(app, mouseX, mouseY, 'settings'):
        setActiveScreen('start')

def settings_onMouseDrag(app, mouseX, mouseY):
    if clickedFrictionSlider(app, mouseX, mouseY):
        app.dragFrictionSlider = True
    elif clickedSpeedSlider(app, mouseX, mouseY):
        app.dragSpeedSlider = True
    elif clickedp1MassSlider(app, mouseX, mouseY):
        app.dragp1MassSlider = True
    elif clickedp2MassSlider(app, mouseX, mouseY):
        app.dragp2MassSlider = True

    if app.dragFrictionSlider:
        app.friction = mouseX / (app.width/4)
        if app.friction < 1:
            app.friction = 1
        if app.friction > 3:
            app.friction = 3
    elif app.dragSpeedSlider:
        app.speedMultiplier = mouseX / (app.width/4)
        if app.speedMultiplier < 1:
            app.speedMultiplier = 1
        if app.speedMultiplier > 3:
            app.speedMultiplier = 3
    elif app.dragp1MassSlider:
        app.p1Mass = mouseX / (app.width/4)
        if app.p1Mass < 1:
            app.p1Mass = 1
        if app.p1Mass > 3:
            app.p1Mass = 3
    elif app.dragp2MassSlider:
        app.p2Mass = mouseX / (app.width/4)
        if app.p2Mass < 1:
            app.p2Mass = 1
        if app.p2Mass > 3:
            app.p2Mass = 3

def settings_onMouseRelease(app, mouseX, mouseY):
    app.dragFrictionSlider = False
    app.dragSpeedSlider = False
    app.dragp1MassSlider = False
    app.dragp2MassSlider = False

def chooseMode_redrawAll(app):
    drawRect(0,0, app.width, app.height, fill = app.startBackgroundColor)
    drawLabel('Choose a Game Mode!', app.width / 2, app.height / 3, fill = 'white', size = 50, font = 'montserrat', bold = True)
    drawRect(app.width/2, app.height/2, app.width/3, 60, fill = 'lightSkyBlue', border = 'white', align = 'center')
    drawLabel('2-Player', app.width/2, app.height/2, size = 32, fill = 'white', font = 'montserrat', bold = True)
    drawRect(app.width/2, app.height*0.62, app.width/3, 60, fill = 'lightSkyBlue', border = 'white', align = 'center')
    drawLabel('Player vs. Bot', app.width/2, app.height*0.62, size = 32, fill = 'white', font = 'montserrat', bold = True)

def chooseMode_onMousePress(app, mouseX, mouseY):
    if pressed2Player(app, mouseX, mouseY):
        app.mode = '2p'
        app.seals = []
        #at least 50 away from edge
        spawnSeals(app, app.numP1Seals, 'blue', app.platformLeft + 50, app.platformLeft + app.platformWidth - 50, app.platformTop + 50, app.platformTop + app.platformHeight - 50, app.seals)
        spawnSeals(app, app.numP2Seals, 'red', app.platformLeft + 50, app.platformLeft + app.platformWidth - 50, app.platformTop + 50, app.platformTop + app.platformHeight - 50, app.seals)
        setActiveScreen('game')
    elif pressedPVB(app, mouseX, mouseY):
        app.mode = 'bot'
        app.seals = []
        #at least 50 away from edge
        spawnSeals(app, app.numP1Seals, 'blue', app.platformLeft + 50, app.platformLeft + app.platformWidth - 50, app.platformTop + 50, app.platformTop + app.platformHeight - 50, app.seals)
        spawnSeals(app, app.numP2Seals, 'red', app.platformLeft + 50, app.platformLeft + app.platformWidth - 50, app.platformTop + 50, app.platformTop + app.platformHeight - 50, app.seals)
        setActiveScreen('game')

#GAME SCREEN--------------

def game_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill = app.gameBackgroundColor)
    #drawing the semi-3d sides of the platform:
    drawPolygon(app.platformLeft, app.platformTop + app.platformHeight, app.platformLeft + 5, app.platformTop + app.platformHeight + 5,
        app.platformLeft + app.platformWidth + 5, app.platformTop + app.platformHeight + 5,
        app.platformLeft + app.platformWidth + 5, app.platformTop + 5, app.platformLeft + app.platformWidth, app.platformTop,
        app.platformLeft + app.platformWidth, app.platformTop + app.platformHeight, fill = 'paleTurquoise')
    drawRect(app.platformLeft, app.platformTop, app.platformWidth, app.platformHeight, fill = app.platformColor)
    
    if app.prepPhase:
        drawLabel('Planning Phase', 105, 25, fill = 'white', size = 25, bold = True)
        if not app.bothReady:
            if app.p1Turn:
                drawRect(app.width/2 - 60, app.height - 75, 120, 50, fill = 'blue', border = 'white', borderWidth = 2)
                drawLabel("Player 1's Turn", 100, 55, fill = 'blue', size = 25, bold = True)
                drawLabel('P1 Ready', app.width/2, app.height - 50, fill = 'white', size = 16, bold = True)
            else:
                drawRect(app.width/2 - 60, app.height - 75, 120, 50, fill = 'red', border = 'white', borderWidth = 2)
                drawLabel("Player 2's Turn", 100, 55, fill = 'red', size = 25, bold = True)
                drawLabel('P2 Ready', app.width/2, app.height - 50, fill = 'white', size = 16, bold = True)
        elif app.bothReady:
            drawRect(app.width/2 - 60, app.height - 75, 120, 50, fill = 'blue', border = 'white', borderWidth = 2)
            drawLabel('Launch!', app.width/2, app.height - 50, fill = 'white', size = 16, bold = True)
    else:
        drawLabel('Action Phase', 105, 25, fill = 'white', size = 25, bold = True)

    for seal in app.seals:
        seal.draw()
    
    for seal in app.seals: #separate loop so that all seals are drawn before arrows; so that arrows go on top of seals not vice versa
        if seal.lineStartX and seal.lineEndX: #if both not None
            if app.bothReady or (app.p1Turn and seal.borderColor == 'blue') or (app.p2Turn and seal.borderColor == 'red'):
                drawLine(seal.lineStartX, seal.lineStartY, seal.lineEndX, seal.lineEndY, fill = seal.borderColor, lineWidth = 5, arrowEnd = True)

        if app.actionPhase:
            seal.lineStartX = None
            seal.lineStartY = None
            seal.lineEndX = None
            seal.lineEndY = None
    
    drawLabel('Knockout!', app.width - 120, 30, size = 40, fill = 'white', font = 'montserrat', bold = True)
    if app.mode == '2p':
        drawLabel('P1 vs P2', app.width - 120, 60, size = 20, fill = 'white', font = 'montserrat', bold = True)
    else:
        drawLabel('P1 vs Bot', app.width - 120, 60, size = 20, fill = 'white', font = 'montserrat', bold = True)
    
# only needed for debugging, shortcuts
def game_onKeyPress(app, key):
    if key == 't': #temp: spawn random seals
        spawnSeals(app, app.numP1Seals, 'blue', app.platformLeft + 50, app.platformLeft + app.platformWidth - 50, app.platformTop + 50, app.platformTop + app.platformHeight - 50, app.seals)
        spawnSeals(app, app.numP2Seals, 'red', app.platformLeft + 50, app.platformLeft + app.platformWidth - 50, app.platformTop + 50, app.platformTop + app.platformHeight - 50, app.seals)
    elif key == 'a':
        app.actionPhase = True
        app.prepPhase = False
    elif key == 'c':
        app.prepPhase = True
        app.actionPhase = False
    elif key == 'p':
        print(f'prepPhase: {app.prepPhase}, actionPhase: {app.actionPhase}')
    elif key == 'd':
        print(sealsDoneMoving(app.seals))
    elif key == 'v':
        for seal in app.seals:
            print(app.seals.index(seal), seal.xv, seal.yv)
            print(f'underwater: {seal.underWater}')

def game_onMousePress(app, mouseX, mouseY):
    if pressedLaunch(app, mouseX, mouseY):
        if app.bothReady:
            app.bothReady = False
            app.prepPhase = False
            app.actionPhase = True
    if pressedReady(app, mouseX, mouseY):
        if app.p1Turn:
            app.p1Turn = False
            if app.mode == 'bot':
                arrows = botActions(app)
                for seal in app.seals:
                    if seal.borderColor == 'red':
                        seal.lineEndX, seal.lineEndY = arrows[0]
                        arrows.pop(0)
                        seal.lineStartX = seal.cx
                        seal.lineStartY = seal.cy
                        seal.xv = (seal.lineEndX - seal.lineStartX) / (12.5) * app.speedMultiplier/4 / seal.mass
                        seal.yv = (seal.lineEndY - seal.lineStartY) / (12.5) * app.speedMultiplier/4 / seal.mass
                app.bothReady = True
            else:
                app.p2Turn = True
        else:
            app.bothReady = True
    for seal in app.seals:
        if app.prepPhase:
            if app.p1Turn: #player 1 can only control blue seals 
                if seal.borderColor == 'blue' and distance(mouseX, mouseY, seal.cx, seal.cy) <= seal.bodyRadius:
                    seal.clickedInSeal = True
                    seal.lineStartX = seal.cx
                    seal.lineStartY = seal.cy
            elif app.p2Turn and app.mode == '2p': #player 2 controls red
                if seal.borderColor == 'red' and distance(mouseX, mouseY, seal.cx, seal.cy) <= seal.bodyRadius:
                    seal.clickedInSeal = True
                    seal.lineStartX = seal.cx
                    seal.lineStartY = seal.cy

def game_onMouseDrag(app, mouseX, mouseY):
    for seal in app.seals:
        if seal.clickedInSeal:
            prevlineEndX = seal.lineEndX
            prevlineEndY = seal.lineEndY
            seal.lineEndX = mouseX
            seal.lineEndY = mouseY

            xDist = seal.lineEndX - seal.lineStartX
            yDist = seal.lineEndY - seal.lineStartY
            totalDist = math.sqrt(xDist**2 + yDist**2)
            
            if totalDist > 125: #velocity divides by 25 and max velocity is 5
                ratio = 125/totalDist
                xDist = xDist * ratio
                yDist = yDist * ratio
                
                seal.lineEndX = seal.lineStartX + xDist
                seal.lineEndY = seal.lineStartY + yDist            

def game_onMouseRelease(app, mouseX, mouseY):
    for seal in app.seals:
        if seal.clickedInSeal and app.prepPhase:
            if seal.lineEndX != None and seal.lineStartX != None and seal.lineEndX - seal.lineStartX != 0: #prevent error from only clicking (not dragging) from seal
                seal.xv = (seal.lineEndX - seal.lineStartX) / (12.5) * app.speedMultiplier/4 / seal.mass #12.5 simply derived from testing values
            if seal.lineEndY != None and seal.lineStartY != None and  seal.lineEndY - seal.lineStartY != 0:
                seal.yv = (seal.lineEndY - seal.lineStartY) / (12.5) * app.speedMultiplier/4 / seal.mass #higher mass -> lower velocity
            seal.clickedInSeal = False

def game_onStep(app):
    app.platformLeft = (app.width - app.platformWidth)/2
    app.platformTop = (app.height - app.platformHeight)/2

    i = 0
    while i < len(app.seals):
        seal = app.seals[i]
        if app.actionPhase and (seal.xv != 0 or seal.yv != 0):
            seal.updateVelocities(app.friction / 125) #125 derived from testing out numbers; magic number?
        for otherSeal in app.seals:
            if otherSeal != seal and distance(seal.cx, seal.cy, otherSeal.cx, otherSeal.cy) < 2*seal.bodyRadius:
                seal.collideUpdate(otherSeal)
        if app.actionPhase and sealsDoneMoving(app.seals):
            app.actionPhase = False
            app.prepPhase = True
            app.bothReady = False
            app.p1Turn = True
            app.p2Turn = False
        if seal.underWater == False and seal.cx < app.platformLeft or seal.cx > app.platformLeft + app.platformWidth or seal.cy < app.platformTop or seal.cy > app.platformTop + app.platformHeight:
            seal.bodyRadius -= 1
            if seal.bodyRadius % 4 == 0: #reduce eye/pupil radius to keep proportions mostly right
                seal.eyeRadius -= 1
                seal.pupilRadius -= 1
            elif seal.bodyRadius < 18:
                seal.underWater = True
        if seal.underWater:
            seal.splashRadius += 1
            if seal.splashRadius > seal.bodyRadius:
                app.seals.pop(i)
                continue
        i += 1

    p1SealsRemaining = 0
    p2SealsRemaining = 0
    for seal in app.seals:
        if seal.borderColor == 'blue':
            p1SealsRemaining += 1
        else:
            p2SealsRemaining += 1
    
    if p1SealsRemaining == 0 or p2SealsRemaining == 0:
        if p2SealsRemaining == 0:
            app.win = 'PLAYER 1 WINS'
        elif p1SealsRemaining == 0:
            if app.mode == 'bot':
                app.win = 'BOT WINS'
            else: 
                app.win = 'PLAYER 2 WINS'
        setActiveScreen('end')

#Functions related to the Bot decision-making
def botActions(app):
    playerSeals = []
    botSeals = []
    actions = []
    closestSeals = []

    for seal in app.seals:
        if seal.borderColor == 'blue':
            playerSeals.append(seal)
        else:
            botSeals.append(seal)

    for botSeal in botSeals:
        target = closestSeal(botSeal, playerSeals, closestSeals)
        closestSeals.append(target)
        x, y = arrowsToward(botSeal, target)
        actions.append((x, y))

    return actions

def closestSeal(seal, otherSeals, closestList):
    currX = seal.cx
    currY = seal.cy

    nearestSeal = None
    nearestDist = None
    for otherSeal in otherSeals:
        currDist = distance(otherSeal.cx, otherSeal.cy, currX, currY)
        if (otherSeal not in closestList or len(closestList) >= len(otherSeals)) and (nearestSeal == None or currDist < nearestDist):
            nearestDist = currDist
            nearestSeal = otherSeal

    return nearestSeal

def arrowsToward(seal1, seal2):
    xDif = seal2.cx-seal1.cx
    yDif = seal2.cy-seal1.cy 
    dist = distance(seal1.cx, seal1.cy, seal2.cx, seal2.cy)

    lineEndX = seal1.cx + 125 * xDif / dist #5 -> max power
    lineEndY = seal1.cy + 125 * yDif / dist

    return lineEndX, lineEndY

def spawnSeals(app, totalSeals, sealColor, xmin, xmax, ymin, ymax, otherSeals):
    numSeals = 0
    while numSeals < totalSeals:
        tempSeal = Seal(random.randrange(int(xmin), int(xmax)), random.randrange(int(ymin), int(ymax)), sealColor)
            
        canPlace = True
        for seal in otherSeals:
            if distance(tempSeal.cx, tempSeal.cy, seal.cx, seal.cy) <= seal.bodyRadius * 2 + 10:
                canPlace = False
                break
        if canPlace:
            if sealColor == 'red':
                tempSeal.mass = app.p2Mass
                otherSeals.insert(0, tempSeal) 
            else:
                tempSeal.mass = app.p1Mass
                otherSeals.append(tempSeal)
            numSeals += 1

def sealsDoneMoving(sealsList):
    noneMoving = True
    for seal in sealsList:
        if abs(seal.xv) > 0 or abs(seal.yv) > 0:
            noneMoving = False
            break
    return noneMoving

def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

class Seal:
    def __init__(self, cx, cy, borderColor, mass = 1, bodyRadius = 28, eyeRadius = 8, pupilRadius = 4):
        self.cx = cx
        self.cy = cy
        self.xv = 0
        self.yv = 0
        self.mass = mass
        self.borderColor = borderColor
        self.bodyRadius = bodyRadius
        self.eyeRadius = eyeRadius
        self.pupilRadius = pupilRadius
        self.underWater = False
        self.splashRadius = 10

        #the following variables and the basics of the line drawing mechanics are based on the TA-led Physics/Collisions Mini-Lecture Recording
        self.lineStartX = None
        self.lineStartY = None
        self.lineEndX = None
        self.lineEndY = None
        self.clickedInSeal = False
        
    def draw(self):
        if self.underWater == False:
            drawCircle(self.cx, self.cy, self.bodyRadius, fill = 'white', border = self.borderColor, borderWidth = self.mass) #seal body
            drawCircle(self.cx - self.bodyRadius/2, self.cy - self.bodyRadius/2, self.eyeRadius, fill = 'black') #left eye
            drawCircle(self.cx + self.bodyRadius/2, self.cy - self.bodyRadius/2, self.eyeRadius, fill = 'black') #right eye
            drawCircle(self.cx - self.bodyRadius/2 - self.pupilRadius/2, self.cy - self.bodyRadius/2 - self.pupilRadius/2, self.pupilRadius, fill = 'white') #left pupil
            drawCircle(self.cx + self.bodyRadius/2 + self.pupilRadius/2, self.cy - self.bodyRadius/2 - self.pupilRadius/2, self.pupilRadius, fill = 'white') #right pupil
            
            drawLine(self.cx, self.cy, self.cx, self.cy+10)
            drawOval(self.cx, self.cy-2, 8, 12, rotateAngle = 90)
            drawArc(self.cx, self.cy+8, self.bodyRadius-1, self.bodyRadius-1, 180, 180, fill = 'black')
            drawCircle(self.cx, self.cy+16, 4, fill = 'pink')
        else:
            drawCircle(self.cx, self.cy, self.splashRadius, fill = None, border = 'white', borderWidth = 1)

    def updateVelocities(self, friction): #only gets called when velocity > 0
        if self.underWater == False:
            self.cx += self.xv 
            self.cy += self.yv

        if self.yv != 0:
            self.yv = self.yv*(1-friction)
        if self.xv != 0:
            self.xv = self.xv*(1-friction)

        if abs(self.xv) < 0.1:
            self.xv = 0
        if abs(self.yv) < 0.1:
            self.yv = 0

    def collideUpdate(self, other):
        prev_xv1 = self.xv
        prev_yv1 = self.yv
        prev_xv2 = other.xv
        prev_yv2 = other.yv

        self.xv = prev_xv1 - (2*other.mass)/(self.mass+other.mass) * (prev_xv1 - prev_xv2)
        self.yv = prev_yv1 - (2*other.mass)/(self.mass+other.mass) * (prev_yv1 - prev_yv2)
        other.xv = prev_xv2 - (2*self.mass)/(self.mass+other.mass) * (prev_xv2 - prev_xv1)
        other.yv = prev_yv2 - (2*self.mass)/(self.mass+other.mass) * (prev_yv2 - prev_yv1)

        #The following 20 lines are from the help of ChatGPT:----------
        # Calculate the overlap distance
        dx = self.cx - other.cx
        dy = self.cy - other.cy
        distance = (dx ** 2 + dy ** 2) ** 0.5
        min_distance = 2*self.bodyRadius 

        if distance < min_distance:
            # Calculate the overlap distance
            overlap = min_distance - distance

            # Move objects apart based on overlap and normal direction
            nx = dx / distance  # normal direction in x
            ny = dy / distance  # normal direction in y

            # Move both objects away from each other along the normal by half of the overlap
            self.cx += nx * overlap / 2
            self.cy += ny * overlap / 2
            other.cx -= nx * overlap / 2
            other.cy -= ny * overlap / 2
        #----------------------------------

        #prevent infinite collision at 0 velocity
        if (self.xv == 0 and self.yv == 0):
            if self.cx > other.cx:
                self.cx += 1
            else:
                self.cx -= 1
            if self.cy > other.cy:
                self.cy += 1
            else:
                self.cy -= 1
        if other.xv == 0 and other.yv == 0:
            if other.cx > self.cx:
                other.cx += 1
            else:
                other.cx -= 1
            if other.cy > self.cy:
                other.cy += 1
            else:
                other.cy -= 1

def end_redrawAll(app):
    drawRect(0,0, app.width, app.height, fill = app.gameBackgroundColor)
    drawLabel(app.win, app.width/2, app.height/10*4, size = 90, fill = 'white', font = 'montserrat', bold = True)
    drawRect(app.width/2, app.height*0.75, app.width/4, 50, fill = 'lightSkyBlue', border = 'white', align = 'center')
    drawLabel('Return', app.width/2, app.height*0.75, size = 30, fill = 'white', font = 'montserrat', bold = True)
    drawRect(app.width/2, app.height*0.65, app.width/4, 50, fill = 'lightSkyBlue', border = 'white', align = 'center')
    drawLabel('Play Again', app.width/2, app.height*0.65, size = 30, fill = 'white', font = 'montserrat', bold = True)

def end_onMousePress(app, mouseX, mouseY):
    if pressedReturn(app, mouseX, mouseY, 'end'):
        setActiveScreen('start')
    elif pressedAgain(app, mouseX, mouseY):
        app.seals = []
        spawnSeals(app, app.numP1Seals, 'blue', app.platformLeft + 50, app.platformLeft + app.platformWidth - 50, app.platformTop + 50, app.platformTop + app.platformHeight - 50, app.seals)
        spawnSeals(app, app.numP2Seals, 'red', app.platformLeft + 50, app.platformLeft + app.platformWidth - 50, app.platformTop + 50, app.platformTop + app.platformHeight - 50, app.seals)
        app.win = ''
        setActiveScreen('game')

def pressedAgain(app, mouseX, mouseY):
    againLeft = app.width/2 - app.width/8
    againRight = app.width/2 + app.width/8
    againTop = app.height*0.65 - 25
    againBottom = app.height*0.65 + 25
    return (againLeft < mouseX < againRight) and (againTop < mouseY < againBottom)

def main():
    runAppWithScreens(initialScreen='start')
main()