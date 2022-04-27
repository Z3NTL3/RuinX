from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import concurrent.futures
import sys
import os.path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import psutil
import random

''' 
Programmed by Z3NTL3
'''

block = ['http','://','www','https']
timeout = 15
usedNames = ["Z3NTL3"]
try:
    sys.argv[1]
except:
    sys.exit("Usage -> python ruin.py name")
class XPATH(object):
    def __init__(self,xpath,driver):
        self.driverwait = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    
    def Click(self):
        self.driverwait.click()

    def Send(self,key):
        self.driverwait.send_keys(key)
    
def LessonUp(**info):
    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.lessonup.com/site/nl")  

    JobsToDo = [
        "//input[@placeholder='000-000']",
        "//img[@src='/site/img/arrow-right.svg']",
        "//input[@id='player-name']",
        "//div[@class='button cw']"
    ]
    XPATH("//*[@id='__next']/div/div[2]/div/div[2]/button", driver).Click()
    for Jobs in enumerate(JobsToDo):
        if Jobs[0] == 0:
            XPATH(Jobs[1], driver).Send(info['code'])
        elif Jobs[0] == 1:
            XPATH(Jobs[1], driver).Click()
        elif Jobs[0] == 2:
            XPATH(Jobs[1], driver).Send(info['name'])
        elif Jobs[0] == 3:
            XPATH(Jobs[1], driver).Click()
        else:
            driver.quit()
    
    
def WebsiteBot(**info):
    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get("https://kahoot.it/")

    JobsToDo = [
        "//input[@id='game-input']",
        "//button[@type='submit']",
        "//input[@id='nickname']",
        "//button[@type='submit']"
    ]

    for Jobs in enumerate(JobsToDo):
        if Jobs[0] == 0:
            XPATH(Jobs[1], driver).Send(info['code'])
        elif Jobs[0] == 1:
            XPATH(Jobs[1], driver).Click()
        elif Jobs[0] == 2:
            XPATH(Jobs[1], driver).Send(info['name'])
        elif Jobs[0] == 3:
            XPATH(Jobs[1], driver).Click()
        else:
            driver.quit()
    

def Logo():
    print(f"""
\t\t\t   \033[38;5;206m╦═╗╦ ╦╦╔╗╔  
\t\t\t   \033[38;5;207m╠╦╝║ ║║║║║  
\t\t\t   \033[38;5;219m╩╚═╚═╝╩╝╚╝  
                          \033[38;5;219m╔════\033[38;5;206m═══\033[38;5;207m═══╗
                          \033[38;5;219m║ \033[38;5;206mRuinX \033[38;5;207mv2 \033[38;5;219m║
                          \033[38;5;219m╚════\033[38;5;206m══════\033[38;5;207m╝

              \033[38;5;219m╔════\033[38;5;207m════════\033[38;5;219m════════\033[38;5;207m═══════\033[38;5;206m═════╗
              ║ \033[38;5;206mProgrammed and ran by \033[38;5;207mZ3N\033[38;5;219mTL3\033[0m 🤖
              \033[38;5;219m╚════\033[38;5;206m═════\033[38;5;207m════\033[38;5;206m══════\033[38;5;219m══════\033[38;5;207m═══════╝

                 \033[38;5;219m"\033[38;5;206mYour \033[38;5;207mTeacher Ruining \033[38;5;206mFriend\033[38;5;219m" \033[38;5;219m
                            \033[38;5;290m@\033[38;5;207mz3ntl3

 \033[38;5;206m╔═══════════════\033[38;5;207m══════════════════════════════════════════\033[38;5;219m════╗
 \033[38;5;206m║ \033[38;5;207mOptions
 \033[38;5;206m║
 \033[38;5;206m║ \033[38;5;207mkahoot \033[38;5;219m- \033[38;5;219mspam kahoot [\033[32mProgrammed\033[38;5;206m]
 ║ \033[38;5;207mlessonup - \033[38;5;219mspam lessonup very fastly [\033[32mProgrammed\033[38;5;206m]
 ║ \033[38;5;207mexit - \033[38;5;219mDelete all ongoing tasks and \033[32mSIGKILL\033[0m \033[38;5;206m BOT
 \033[38;5;206m║
 \033[38;5;206m╚═════\033[38;5;207m═════\033[38;5;219m═════\033[38;5;207m═══════════════════════════════════════════════╝\033[0m

                       \033[38;5;219mYour Name: \033[0m{sys.argv[1]}
""")

def NameGenerator(username):
    numbers = [str(x) for x in range(99)]
    chars = ["!","@","#","$","%","^","&","*","(",")","_","-","=","+"]

    Mn = True
    while Mn:
        username = f"{random.choice(numbers) + random.choice(chars) + random.choice(username) + random.choice(numbers)}--{username}"
        for names in usedNames:
            if names != username:
                usedNames.append(username)
                Mn = False
                break
    return username

def Main():
    global valid,menuexit, kahoot, lessonup
    valid = False
    menuexit = False
    kahoot = False
    lessonup = False
    while True:
        choose = input("\033[38;5;206m->\033[0m ")
        if choose.lower() == "kahoot":
            gamecode = input("\033[38;5;206m[GameCode]->\033[0m ")
            threads = int(input("\033[38;5;206m[Threads]->\033[0m "))
            print("\033[38;5;206mPlease d\033[38;5;207mont touch\033[38;5;219m anyth\033[38;5;206ming will open and spam \033[38;5;207shortly in mult\033[38;5;206mi thre\033[38;5;219maded way\033[0m")
            if threads > 30:
                print("\033[38;5;206mThreads more than 30 are not allowed yet, try again\033[0m")
            else:
                valid = True
                kahoot = True
                break
        elif choose.lower() == "lessonup":    
            gamecode = input("\033[38;5;206m[GameCode]->\033[0m ")
            threads = int(input("\033[38;5;206m[Threads]->\033[0m "))
            print("\033[38;5;206mPlease d\033[38;5;207mont touch\033[38;5;219m anyth\033[38;5;206ming will open and spam \033[38;5;207mshortly in mult\033[38;5;206mi thre\033[38;5;219maded way\033[0m")
            if threads > 30:
                print("\033[38;5;206mThreads more than 30 are not allowed yet, try again\033[0m")
            else:
                lessonup = True
                valid = True
                break
        elif choose.lower() == "exit":
            print("\033[38;5;206m[\033[31mExiting\033[38;5;206m]\033[0m ")
            menuexit = True
            break
    if valid and kahoot:
        pool = concurrent.futures.ProcessPoolExecutor(max_workers=61)
        futures = [pool.submit(WebsiteBot,code=gamecode,name=NameGenerator(sys.argv[1])) for x in range(threads)]
    
    elif valid and lessonup:
        pool = concurrent.futures.ProcessPoolExecutor(max_workers=61)
        futures = [pool.submit(LessonUp,code=gamecode,name=NameGenerator(sys.argv[1])) for x in range(threads)]
    
    elif menuexit:
        sys.exit()
    # exitor menu
    menu = True
    while menu:
        choose = input("\033[38;5;206m->\033[0m ")
        if choose.lower() == "exit":
            print("\033[38;5;206mPlease pr\033[38;5;207mess nothing o\033[38;5;219mn, cance\033[38;5;206mlling ongoi\033[38;5;207mng tasks plea\033[38;5;219mse wait.\033[0m")
            try:
                pool.shutdown(wait=False,cancel_futures=True)
                for future in concurrent.futures.as_completed(futures):
                    future.cancel()
            except RuntimeError:
                pass
            driverName = "chrome.exe"
            try:
                for proc in psutil.process_iter():
                    if proc.name() == driverName:
                        for x in range(len(futures)):
                            proc.kill()
            except:
                pass
                
            menu = False
        else:
            print("\033[38;5;206m[\033[31mCommands\033[0m\033[38;5;206m] \033[38;5;207m-\033[38;5;219m>\033[0m \033[31mexit\033[0m")
    if future.done():
        print("\033[38;5;206mTerminated the threads\033[0m")
    return
                
if __name__ == '__main__':
    Logo()
    Main()
    
