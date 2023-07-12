from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import concurrent.futures
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import psutil
import random
from multiprocessing import cpu_count

""" 
Made by Z3NTL3
"""

block = ["http", "://", "www", "https"]
timeout = 15
used_names = ["Z3NTL3"]
workers = (cpu_count() - 2) * 2

try:
    sys.argv[1]
except IndexError:
    sys.exit("Usage -> python ruin.py name")


class XPATH(object):
    def __init__(self, xpath, driver):
        self.driverwait = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

    def click(self):
        self.driverwait.click()

    def cend(self, key):
        self.driverwait.send_keys(key)


def lesson_up(**info):
    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.lessonup.com/site/nl")

    jobs_to_do = [
        "//input[@placeholder='000-000']",
        "//img[@src='/site/img/arrow-right.svg']",
        "//input[@id='player-name']",
        "//div[@class='button cw']",
    ]
    XPATH("//*[@id='__next']/div/div[2]/div/div[2]/button", driver).click()
    for jobs_index, jobs in enumerate(jobs_to_do):
        xpath_instance = XPATH(jobs, driver)
        match jobs_index:
            case 0:
                xpath_instance.send(info["code"])
            case 1:
                xpath_instance.click()
            case 2:
                xpath_instance.send(info["name"])
            case 3:
                xpath_instance.click()
            case other:
                driver.quit()


def WebsiteBot(**info):
    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get("https://kahoot.it/")

    jobs_to_do = [
        "//input[@id='game-input']",
        "//button[@type='submit']",
        "//input[@id='nickname']",
        "//button[@type='submit']",
    ]

    for jobs_index, jobs in enumerate(jobs_to_do):
        xpath_instance = XPATH(jobs, driver)
        match jobs_index:
            case 0:
                xpath_instance.send(info["code"])
            case 1:
                xpath_instance.click()
            case 2:
                xpath_instance.send(info["name"])
            case 3:
                xpath_instance.click()
            case other:
                driver.quit()


def name_generator(username):
    numbers = [str(x) for x in range(99)]
    chars = "!@#$%^&*()_-=+"

    on_runtime = True
    while on_runtime:
        username = f"{random.choice(numbers)}{random.choice(chars)}{random.choice(username)}{random.choice(numbers)}--{username}"
        for names in used_names:
            if names != username:
                used_names.append(username)
                on_runtime = False
                break

    return username


if __name__ == "__main__":
    print(
        f"""
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
"""
    )
    valid = False
    menuexit = False
    kahoot = False
    lessonup = False
    while True:
        choose = input("\033[38;5;206m->\033[0m ")
        if choose.lower() == "kahoot":
            gamecode = input("\033[38;5;206m[GameCode]->\033[0m ")
            threads = int(input("\033[38;5;206m[Threads]->\033[0m "))
            print(
                "\033[38;5;206mPlease d\033[38;5;207mont touch\033[38;5;219m anyth\033[38;5;206ming will open and spam \033[38;5;207shortly in mult\033[38;5;206mi thre\033[38;5;219maded way\033[0m"
            )
            if threads > 30:
                print(
                    "\033[38;5;206mThreads more than 30 are not allowed yet, try again\033[0m"
                )
            else:
                valid = True
                kahoot = True
                break
        elif choose.lower() == "lessonup":
            gamecode = input("\033[38;5;206m[GameCode]->\033[0m ")
            threads = int(input("\033[38;5;206m[Threads]->\033[0m "))
            print(
                "\033[38;5;206mPlease d\033[38;5;207mont touch\033[38;5;219m anyth\033[38;5;206ming will open and spam \033[38;5;207mshortly in mult\033[38;5;206mi thre\033[38;5;219maded way\033[0m"
            )
            if threads > 30:
                print(
                    "\033[38;5;206mThreads more than 30 are not allowed yet, try again\033[0m"
                )
            else:
                lessonup = True
                valid = True
                break
        elif choose.lower() == "exit":
            print("\033[38;5;206m[\033[31mExiting\033[38;5;206m]\033[0m ")
            menuexit = True
            break

    if valid and kahoot:
        pool = concurrent.futures.ProcessPoolExecutor(max_workers=int(workers))
        futures = [
            pool.submit(WebsiteBot, code=gamecode, name=name_generator(sys.argv[1]))
            for _ in range(threads)
        ]

    elif valid and lessonup:
        pool = concurrent.futures.ProcessPoolExecutor(max_workers=int(workers))
        futures = [
            pool.submit(lesson_up, code=gamecode, name=name_generator(sys.argv[1]))
            for x in range(threads)
        ]

    elif menuexit:
        sys.exit()

    menu = True
    ftrs = []

    while menu:
        choose = input("\033[38;5;206m->\033[0m ")
        if choose.lower() == "exit":
            print(
                "\033[38;5;206mPlease pr\033[38;5;207mess nothing o\033[38;5;219mn, cance\033[38;5;206mlling ongoi\033[38;5;207mng tasks plea\033[38;5;219mse wait.\033[0m"
            )
            try:
                pool.shutdown(wait=False, cancel_futures=True)
                for future in concurrent.futures.as_completed(futures):
                    ftrs.append(future)
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
            print(
                "\033[38;5;206m[\033[31mCommands\033[0m\033[38;5;206m] \033[38;5;207m-\033[38;5;219m>\033[0m \033[31mexit\033[0m"
            )
    ths = []
    for f in ftrs:
        if f.done():
            ths.append("yes")
    if len(ths) == len(ftrs):
        print("\033[38;5;206mTerminated the threads\033[0m")
