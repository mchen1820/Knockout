#This is all the button-press functions. Moved to a separate file since the 
#function names are self-explanatory and the functions take up too much space

def pressedInstructions(app, mouseX, mouseY):
    instrLeft = app.width/2 - app.width/6 #center x - half the width
    instrRight = app.width/2 + app.width/6
    instrTop = app.height/2 - 30 #center y - half height
    instrBottom = app.height/2 + 30
    return (instrLeft < mouseX < instrRight) and (instrTop < mouseY < instrBottom)

def pressedPlay(app, mouseX, mouseY):
    playLeft = app.width/2 - app.width/6 #center x - half the width
    playRight = app.width/2 + app.width/6
    playTop = app.height*0.62 - 30 #center y - half height
    playBottom = app.height*0.62 + 30
    return (playLeft < mouseX < playRight) and (playTop < mouseY < playBottom)

def pressedSettings(app, mouseX, mouseY):
    settingsLeft = app.width/2 - app.width/6 #center x - half the width
    settingsRight = app.width/2 + app.width/6
    settingsTop = app.height*0.74 - 30 #center y - half height
    settingsBottom = app.height*0.74 + 30
    return (settingsLeft < mouseX < settingsRight) and (settingsTop < mouseY < settingsBottom)

def pressedReturn(app, mouseX, mouseY, screen):
    returnLeft = app.width/2 - app.width/4/2 #center x - half width
    returnRight = app.width/2 + app.width/4/2
    if screen == 'instr':
        returnTop = app.height*0.85 - 25 #center y - half height
        returnBottom = app.height*0.85 + 25
    elif screen == 'end':
        returnTop = app.height*0.75 - 25
        returnBottom = app.height*0.75 + 25
    elif screen == 'settings':
        returnLeft = app.width/2 - app.width/5/2 
        returnRight = app.width/2 + app.width/5/2
        returnTop = app.height*0.93 - 25
        returnBottom = app.height*0.93 + 25
    return (returnLeft < mouseX < returnRight) and (returnTop < mouseY < returnBottom)

def clickedFrictionSlider(app, mouseX, mouseY):
    sliderLeft = app.friction * app.width/4 - 7.5 
    sliderRight = sliderLeft + 15 #left + width
    sliderTop = app.height*0.24 - 15 #center - half height
    sliderBottom = sliderTop + 30
    return (sliderLeft < mouseX < sliderRight) and (sliderTop < mouseY < sliderBottom)

def clickedSpeedSlider(app, mouseX, mouseY):
    sliderLeft = app.speedMultiplier * app.width/4 - 7.5
    sliderRight = sliderLeft + 15
    sliderTop = app.height*0.42 - 15
    sliderBottom = sliderTop + 30
    return (sliderLeft < mouseX < sliderRight) and (sliderTop < mouseY < sliderBottom)

def clickedp1MassSlider(app, mouseX, mouseY):
    sliderLeft = app.p1Mass * app.width/4 - 7.5
    sliderRight = sliderLeft + 15
    sliderTop = app.height*0.6 - 15
    sliderBottom = sliderTop + 30
    return (sliderLeft < mouseX < sliderRight) and (sliderTop < mouseY < sliderBottom)

def clickedp2MassSlider(app, mouseX, mouseY):
    sliderLeft = app.p2Mass * app.width/4 - 7.5
    sliderRight = sliderLeft + 15
    sliderTop = app.height*0.77 - 15
    sliderBottom = sliderTop + 30
    return (sliderLeft < mouseX < sliderRight) and (sliderTop < mouseY < sliderBottom)

def pressed2Player(app, mouseX, mouseY):
    twoPLeft = app.width/2 - app.width/6 
    twoPRight = app.width/2 + app.width/6
    twoPTop = app.height/2 - 30 
    twoPBottom = app.height/2 + 30
    return (twoPLeft < mouseX < twoPRight) and (twoPTop < mouseY < twoPBottom)

def pressedPVB(app, mouseX, mouseY):
    pvbLeft = app.width/2 - app.width/6 
    pvbRight = app.width/2 + app.width/6
    pvbTop = app.height*0.62 - 30 
    pvbBottom = app.height*0.62 + 30
    return (pvbLeft < mouseX < pvbRight) and (pvbTop < mouseY < pvbBottom)

def pressedReady(app, mouseX, mouseY):
    if not app.bothReady:
        readyLeft = app.width/2 - 60
        readyTop = app.height - 75
        readyRight = app.width/2 + 120
        readyBottom = app.height - 25
        return (readyLeft < mouseX < readyRight) and (readyTop < mouseY < readyBottom)
    
def pressedLaunch(app, mouseX, mouseY):
    if app.bothReady:
        launchLeft = app.width/2 - 60
        launchTop = app.height - 75
        launchRight = app.width/2 + 120
        launchBottom = app.height - 25
        return (launchLeft < mouseX < launchRight) and (launchTop < mouseY < launchBottom)