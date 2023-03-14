#! python3
# Prettified Stopwatch.py - A simple stopwatch program

import time, pyperclip

# Display the program's instrucions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.Press Ctrl-C to quit.')
input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime # the start and last time are initially the same but starttime remains contstant while lasttime changes
lapNum = 1 # initiate lap number at 1
output = ''

# Start tracking the lap times
#"%0.2f" to print a float to 2 decimal places even if e.g. 1.5 print 1.50

try:
    while True:
        input()
        lapTime = "%0.2f" % round(time.time() - lastTime, 2) 
        totalTime = "%0.2f" % round(time.time() - startTime, 2)
        # (%s)string variable
        currentoutput = 'Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totalTime).rjust(5), str(lapTime).rjust(6))
        print(currentoutput,end='')
        output = output + currentoutput + '\n'
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Crtl-C exception to keep its error message from displaying and instead print "Done"
    pyperclip.copy(output) # copies all laptime into clipboard
    print('\nDone.')





