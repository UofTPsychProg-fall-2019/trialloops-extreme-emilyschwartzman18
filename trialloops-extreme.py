#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
@author: katherineduncan
"""
#setup
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

#window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

#clock
trialClock = core.Clock()

#shutdown key
event.globalKeys.add(key='q',func=core.quit)

#note that image stimuli files are 'face1.jpg','face2.jpg','face3.jpg'

#text stimuli
question=visual.TextStim(win,pos=(0,.6),color=(-1,-1,-1),text="Man or Woman?")
resp1=visual.TextStim(win,pos=(-.33,-.45),color=(-1,-1,-1),text='Man')
respE=resp1_1=visual.TextStim(win,pos=(-.33,-.6),color=(-1,-1,.9),text='E')
resp2=visual.TextStim(win,pos=(.33,-.45),color=(-1,-1,-1),text='Woman')
respI=resp1_1=visual.TextStim(win,pos=(.33,-.6),color=(-1,-1,.9),text='I')
end=visual.TextStim(win,pos=(0,0),color=(-1,-1,-1),text='COMPLETE')
corfb=visual.TextStim(win,pos=(0,-.5),color=(-1,.9,-.5),text='CORRECT')
incorfb=visual.TextStim(win,pos=(0,-.5),color=(.9,-1,-1),text='INCORRECT')

#trial loop
trialnum=[1,2,3]
for t in trialnum:
    #trial stimulus
    face=visual.ImageStim(win,pos=(0,0),size=(.71,.71),image=('face'+str(t)+'.jpg'))
    #draw & flip stimulus, text
    face.draw()
    question.draw()
    resp1.draw()
    respE.draw()
    resp2.draw()
    respI.draw()
    win.flip()
    #clear clock & events
    trialClock.reset()
    event.clearEvents()
    #define response inputs
    keys=event.waitKeys(keyList=['e','i'],timeStamped=trialClock)
    #evaluate response, select feedback
    if keys[0][0]=='i'and t==1:
        accuracy='CORRECT'
        feedback=corfb
    elif keys[0][0]=='e'and t==2:
        accuracy='CORRECT'
        feedback=corfb
    elif keys[0][0]=='i'and t==3:
        accuracy='CORRECT'
        feedback=corfb
    else:
        accuracy='INCORRECT'
        feedback=incorfb
    #display feedback
    feedback.draw()
    win.flip()
    core.wait(1)
    #print summary
    print('TRIAL '+str(t)+':')
    print(keys)
    print(accuracy)
    
#completion message
end.draw()
win.flip()
    
#end experiment
core.wait(2)
win.close()
