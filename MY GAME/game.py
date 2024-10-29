from enemies import *
from data import *
import random
battles = 0
max_battles = 15
weights = [0.3 for _ in enemies]
while IBRAGIM["hp"] > 0 and battles < max_battles:
    enemy = random.choices(enemies, weights=weights, k = 1)[0] 
    attach(enemy)
     
    battles += 1
    time.sleep(2)
      

print("Игра кончилась")





            
               
               
