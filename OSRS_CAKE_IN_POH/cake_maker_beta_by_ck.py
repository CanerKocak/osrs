import pyautogui as py
import cv2
from time import sleep
import random

bot_speed = 12

def random_sleeps(sleep_count):
    for i in range(sleep_count)
        random_sleep()

def smooth_click(position):
    x = position[0] + random.randint(-(random.randint(1,8)),(random.randint(1,8)))
    y = position[1] + random.randint(-(random.randint(1,8)),(random.randint(1,8)))
    position = (x, y)
    random_sleeps(1)
    py.moveTo(position, duration=random.randint(1,10)/bot_speed)
    py.click(position)

def random_sleep():
    random_int = random.randint(0,1000)
    if random_int <= 980:
        sleep_time=random.randint(1,3)/bot_speed
    else:
        sleep_time = random.randint(1,70)/(bot_speed*1.5)
    sleep(sleep_time)

def get_positions(item,confidence_percent=.95):
    position = py.locateCenterOnScreen(item, confidence = confidence_percent)
    if position != None:
        x, y = position
        return x, y

def find_items(item, confidence_percent=.9):
    print(f"Looking for {item}...")
    found_bool = False
    while found_bool == False:
        position = get_positions(f"img/{item}.png", confidence_percent)
        if position != None:
            found_bool = True
            print(f"Found {item}!")
            print(position)
            return position, found_bool

def get_cake_supplies_pos():
    while True:
        print("Looking for supplies...")       
        supply_positions = []
        for item in ["egg", "bucket_of_milk", "pot_of_flour"]:
            while True:
                position, found_bool = find_items(item)
                supply_positions.append(position)
                if len(supply_positions) == 3:
                    return supply_positions
                random_sleeps(1)
                break
 
def click_on_oak_larder():
    for number in ["2", "3", "4"]:
        item_count = 6
        
        pos,bool = find_items("oak_larder",0.4)
        if number == "2":
            smooth_click(pos)
            random_sleeps(1)
            pos2, bool2 = find_items("option",0.95)
        pos,bool = find_items("oak_larder",0.4)
        py.moveTo(pos)
        for i in range(item_count):
            random_sleeps(3)
            py.click(pos)
            pos2, bool2 = find_items("option",0.95)
            random_sleeps(2)
            py.keyDown(number)
            random_sleeps(1)
            py.keyUp(number)
            
        
def find_items_to_drop(item, confidence_percent=.8):
    print(f"Looking for {item}...")
    position = get_positions(f"img/{item}.png", confidence_percent)
    if position == None:
        return None, False
    found_bool = True
    print(f"Found {item}!")
    return position, found_bool

def drop_items():
    for item in ["cake", "bucket", "pot", "egg"]:
        while True:
            py.keyDown("shift")
            position, found_bool = find_items_to_drop(item)
            if found_bool == True:
                py.moveTo(position)
                py.click(position)
                py.keyDown("shift")
                py.click(position)
                py.keyUp("shift")
            elif found_bool == False:
                py.keyUp("shift")
                break
    
def make_uncooked_cake(supply):
    print("Making uncooked cake...")
    cake_tin_position, found_bool = find_items("cake_tin")
    if found_bool == True:
        smooth_click(cake_tin_position)
        random_sleeps(1)
        smooth_click(supply)
        sleep(0.5)
    position3, found_bool3 = find_items("make_cake",0.7)
    if found_bool3 == True:
        py.press("space")
        sleep(random.randint(12,14))
        random_sleeps(1)
 
def cook_cake():
    print("Cooking cake...")
    while True:
        position, found_bool = find_items("uncooked_cake")
        if found_bool == True:
            smooth_click(position)
            random_sleeps(1)
            steel_range_pos, steel_range = find_items("steel_range",0.4)
        if steel_range == True:
            smooth_click(steel_range_pos)
            random_sleeps(1)
            make_cake_pos, make_cake = find_items("make_cake")
        if make_cake == True:
            py.press("space")
            sleep(random.randint(18,20))
            items_to_drop_pos, items_to_drop = find_items_to_drop("uncooked_cake")
        if items_to_drop == True:
            print("you leveled up!")
            uncooked_cake_pos, uncooked_cake = find_items("uncooked_cake")
        if uncooked_cake == True:
            smooth_click(uncooked_cake_pos)
        random_sleeps(1)
        position2, found_bool2 = find_items("steel_range1",0.4)
        if found_bool2 == True:
            smooth_click(position2)
            sleep(random.randint(5,10))
            py.press("space")
            sleep(random.randint(14,20))
                break

def bot():
    print("make sure the game is in focus...")
    click_on_oak_larder()
    supply_positions = get_cake_supplies_pos()
    make_uncooked_cake(random.choice(supply_positions))
    random_sleeps(1)
    cook_cake()
    drop_items()
    drop_items()
    random_sleeps(1)

while True:
    bot()
