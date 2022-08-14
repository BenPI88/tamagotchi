import os
import time
os.system("clear")
print("Tamagotchi Remade By BenPI88 (https://github.com/BenPI88)")
input("")
def clearscreen:
  os.system("clear")
clearscreen
print("Setting Up Folders")
dir = "~/BenPI/tamagotchi/"
os.system("cd ~ && mkdir BenPI && cd BenPI && mkdir tamagotchi")
print("Done.")
time.sleep(1)
print("Copying Files...")
os.system("cd ~ && git clone https://github.com/BenPI88/tamagotchi-files && cp ~/tamagotchi-files/tamagotchi.py " + dir + " && rm -rf ~/tamagotchi-files")
print("Done")
time.sleep(1)
print("Setup Is Completed! Installed To " + dir)
