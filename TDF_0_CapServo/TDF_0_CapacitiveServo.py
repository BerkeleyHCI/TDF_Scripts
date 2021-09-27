#Today we'll be working
#with Raspberry Pi and Python3 to control servos
#and introduce three basic concepts into your toolkit
#These lines import the key libraries we need for this
#script - in order to control the crickit and keep track
#of time:

import time
from adafruit_crickit import crickit

def motor_wait():
#this function moves the servo to original angle, 0
#and increments its position by two 90 degree steps
#before rotating back to 0 degrees.
#crickit.servo_1.angle sets the angle of your stepper motor
#time.sleep() asks the processor to wait before executing
       
    print("Moving servo #1: motor_wait()")
    crickit.servo_1.angle = 0      # right
    time.sleep(1)
    crickit.servo_1.angle = 90     # middle
    time.sleep(1)
    crickit.servo_1.angle = 180    # left
    time.sleep(1)
    crickit.servo_1.angle = 90     # middle
    time.sleep(1)
    crickit.servo_1.angle = 0     # right

def motor_conditional():
    #conditionals in python are easy! and, with crickit - fun.
    #this function checks whether the capacitive touch field
    #number one on the crickit board has been activated.
    #if it is, the motor rotates by 180 degrees.
    #if not, you get a message telling you as much :)

    crickit.touch_1.value
    print("Press the Capactive Touch button 1: motor_conditional()")
    time.sleep(3)
    print(crickit.touch_1.value)
    
    if crickit.touch_1.value:
        crickit.servo_1.angle = 180      # right
        time.sleep(2)
        crickit.servo_1.angle = 0 
    else:
        print("No button push detected.")
        
def motor_while():
    #in this while loop, two conditions need to be met:
    #the capacitive button must be pressed, and the motor must
    #not have reached 180 degrees in turning. As long as these
    #conditions are satisfied, the motor turns, incremented by
    #3 degrees every tenth of a second. 
    
    crickit.touch_1.value
    print("Hold the Capactive Touch button to keep running the motor: motor_while()")
    time.sleep(3)
        
    motor_angle = 1
    
    while crickit.touch_1.value and motor_angle < 180:
        crickit.servo_1.angle = motor_angle
        motor_angle += 3
        time.sleep(0.1)

def motor_for():
    #in this for loop, the motor steps by 30 degrees
    #five times.
    #range(x,y,z) specifies the bounds on the for loop,
    #with x being the initial value, y being the final value
    #not to be exceeded, and z being the increment.
    
    print("For Loop Engaged!: motor_for()")
        
    motor_angle = 1
    
    for x in range (0, 181, 30):
        crickit.servo_1.angle = x
        time.sleep(0.5)

def cap_hold():
    #This code incorporates skills learned in several of Vivek's examples above,
    #and is designed to illustrate nested for- and while-loops that cause a servo
    #to exhibit curious and furious behaviors ONLY when the capacitive sensor is
    #being held continuously. Make sure to read comments if the flow is unclear.
    
    print("while holding the sensor, do curious until furious!")#let's get started!
    crickit.servo_1.angle = 0 #initializing our servo at 0
    time.sleep(2) #sleeping for a few seconds after initializing
    
    anger_count = 0 #keep track of how many curious gestures we've exhibited
    while True: #meaning "keep doing everything indented below forever"
        while crickit.touch_1.value: #while capacitive touch sensor is being engaged:
            if crickit.servo_1.angle < 30: #if the servo's angle is less than 30
                for p in range (0, 40, 4): #counting by 4s from 0 to 40 ("p" is arbitrary)
                    crickit.servo_1.angle = p #make the servo's angle equal to the # "p"
                    time.sleep(.1) #sleep a very short time, then repeat this loop until we hit 40
                print("just finished going to 40") #tell us what you did, servo!
                anger_count += 1 #keep track of our anger level by adding +1 to "anger_count"
                print(anger_count) #tell us current anger level so we know how angry we're getting
            elif crickit.servo_1.angle >= 30: #if the servo's angle is more than 30
                for p in range (40, 0, -4): #counting backwards by 4s from 40 to 0
                    crickit.servo_1.angle = p #make the servo's angle = "p" again, this time decreasing
                    time.sleep(.1) #sleep again for a short bit
                print("made it back to 0") #tell us what you did, servo
                anger_count += 1 #getting angrier by 1!
                print(anger_count) #update us on how angry you are

                if anger_count >= 8: #if the anger_count counter gets too big...
                    while crickit.touch_1.value: #and as long as we're /still/ pressing the sensor...
                        crickit.servo_1.angle = 110 #get angry and go to 110!
                        time.sleep(.5) #and try to do it in a half second
                        print("went to 110 more angrier") #report on your rage
                        crickit.servo_1.angle = 0 #now return angerly to 0!
                        time.sleep(.5) #quickly now
                        print("went to 0 more angrier") #report again on your rage!
                
        else:
            print("nothing touching") #oops, we let go of the sensor
            anger_count = 0 #servo calms down, and anger level is reduced to zero
            time.sleep(1) #sleep for a beat


def main():
    # runs code by default!   
  
    print("Hello! TDF Servo test: Starting!")  #print something nice!
    crickit.servo_1.angle = 0                      #set motor to angle '0'
#    motor_wait()
#    motor_conditional()
#    motor_while()
#    motor_for()
    cap_hold()


# the below 'if' statement helps python distinguish the main function.
if __name__ == '__main__':
    main()
