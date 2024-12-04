import cyberpi
import event
import mbot2
import mbuild
import time
import random

DISTANCE_THRESHOLD = 23.0

def roll_di():
    number = random.randint(1, 6)
    cyberpi.display.show_label(number, 16, 'center')
    return number

def is_object_detected(within_a_distance):
    total_distance = 0
    for _ in range(3):
        total_distance += mbuild.ultrasonic2.get()
    average_distance = total_distance / 3
    return average_distance <= within_a_distance

def avoid_object():
    mbot2.forward(speed=0)
    cyberpi.console.print("Obstacle detected! Waiting for it to be cleared.")
    while is_object_detected(DISTANCE_THRESHOLD):
        time.sleep(0.5)
    cyberpi.console.print("Obstacle cleared! Resuming movement.")

@event.is_press('a')
def btn_is_pressed():
    number = roll_di()
    total_distance = 15 * number
    while total_distance > 0:
        if is_object_detected(DISTANCE_THRESHOLD):
            avoid_object()
        else:
            mbot2.straight(15, 20)
            total_distance -= 15
