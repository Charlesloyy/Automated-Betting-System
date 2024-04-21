from selenium import webdriver
import numpy as np
import pandas as pd
import re
import sys
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, TimeoutException, MoveTargetOutOfBoundsException


class SportyBot():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.round_no = None
        self.bet_amount = 25
        self.bet_counter = []
        self.bet_purple = []
        self.combine = [[""]]
        self.false_blue = False
        self.df = pd.DataFrame(columns=["Round", "Time", "Payout"])
    def open_tinder(self):
        self.driver.get('https://www.sportybet.com/ng/m/games/sportygames?game=turbo-games/aviator')
        self.action = ActionChains(self.driver)
        sleep(5)

    def login(self, phone_number, password):
        no = self.driver.find_element('xpath', "//input[@placeholder='Mobile Number']")
        # no = self.driver.find_element('name', 'Mobile Number')
        no.send_keys(phone_number)
        pas = self.driver.find_element('xpath', "//input[@placeholder='Password']")
        # pas = self.driver.find_element('name', 'Password')
        pas.send_keys(password)
        sleep(1)
        signin = self.driver.find_element('xpath', "//button[@class='af-button login-btn af-button--primary']")
        signin.click()

    def aviator(self):
        sleep(5)
        global round_no, my_data, new_arrays
        
        self.driver.switch_to.frame("turbo-games/aviator")
        self.driver.switch_to.frame(0)

    def history(self):
            sleep(1)
            auto_status = True
            odd_status = True
            odd_button_status = True
            # Now, you can click the button
            # autoDiv = self.driver.find_element('xpath', '/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div')
            action = ActionChains(self.driver)
            while auto_status:
                try:
                    auto = self.driver.find_element('xpath', '/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/app-navigation-switcher/div/button[2]')
                    self.action.move_to_element(auto).click().perform()
                    print("done")
                    auto_status = False
                except:
                    continue
            #     sleep(2)
            #     self.action.move_to_element(auto).click().perform()

            auto_bt = self.driver.find_element('xpath', '/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/div[3]/div[2]/div[1]/app-ui-switcher/div')
            while odd_button_status:
                try:
                    
                    self.action.move_to_element(auto_bt).click().perform()
                    odd_button_status = False
                except:
                    continue
            #     self.action.move_to_element(auto_bt).click().perform()
            # except:
            #     sleep(2)
            #     self.action.move_to_element(auto_bt).click().perform()

            auto_odd = self.driver.find_element('xpath', '/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/div[3]/div[2]/div[2]/div/app-spinner/div/div[2]/input')
            while odd_status:
                try:
                    self.action.move_to_element(auto_odd).click().perform()
                    auto_odd.send_keys(Keys.BACKSPACE)
                    auto_odd.send_keys(Keys.BACKSPACE)
                    auto_odd.send_keys(Keys.BACKSPACE)
                    auto_odd.send_keys(Keys.BACKSPACE)
                    auto_odd.send_keys(Keys.BACKSPACE)
                    auto_odd.send_keys("2.")
                    odd_status = False
                    # auto_odd.clear()
                except:
                    continue
                # sleep(2)
                # self.action.move_to_element(auto_odd).click().perform()
                # auto_odd.send_keys(Keys.BACKSPACE)
                # auto_odd.send_keys(Keys.BACKSPACE)
                # auto_odd.send_keys(Keys.BACKSPACE)
                # auto_odd.send_keys(Keys.BACKSPACE)
                # auto_odd.send_keys("2.")

                # auto_odd.clear()
            get_time_status = True
            while get_time_status:
                try:
                    get_time = self.driver.find_element('xpath', '/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[1]/div/app-bubble-multiplier[1]')
                    get_time.click()
                    get_time_status = False
                except:
                    sleep(1)
                    continue
            sleep(1)

            try:
                round_data = self.driver.find_element('xpath', '/html/body/ngb-modal-window/div/div/app-fairness/div[1]/span')

            except:
                print("working")
                sleep (1)
                get_time = self.driver.find_element('xpath', '/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[1]/div/app-bubble-multiplier[1]')
                get_time.click()
                round_data = self.driver.find_element('xpath', '/html/body/ngb-modal-window/div/div/app-fairness/div[1]/span')
            print (round_data.text)
            sleep (1)
            
            try:
                p = round_data.text
                pt = re.split("\s", p)
                self.round_no = int(pt[1])
                print(self.round_no)
                
                get_time_close = self.driver.find_element('xpath', '/html/body/ngb-modal-window/div/div/app-fairness/div[1]/button')
                get_time_close.click()
            except IndexError:
                get_time_close = self.driver.find_element('xpath', '/html/body/ngb-modal-window/div/div/app-fairness/div[1]/button')
                get_time_close.click()

    def stimulation(self):
        global my_2nd_data
        aps = True
        self.bet_status = False
        limit = 20000
        current_value = 0
        a = []
        
        b = np.array(a)
        new = self.round_no
        
        df = pd.DataFrame(columns=["Round", "Time", "Payout"])
        while aps:
            app = "True"
            bet_store = []
            try:
                while app == "True":
                    get_status = True
                    get_2nd_time = self.driver.find_element('xpath', '/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[1]/div/app-bubble-multiplier[1]')
                    # self.action.move_to_element(get_2nd_time).click().perform()
                    get_2nd_time.click()
                    get_status = False
                    sleep(0.15)
                    time_data = self.driver.find_element('xpath', '/html/body/ngb-modal-window/div/div/app-fairness/div[1]/div/div[2]')
                    time_value = time_data.text
                    round_2nd_data = self.driver.find_element('xpath', '/html/body/ngb-modal-window/div/div/app-fairness/div[1]/span')
                    round_value = round_2nd_data.text
                    p2 = round_2nd_data.text
                    pt2 = re.split("\s", p2)
                    round_2nd_no = int(pt2[1])
                    
                    
                    get_2nd_time_close = self.driver.find_element('xpath', '/html/body/ngb-modal-window/div/div/app-fairness/div[1]/button')
                    get_2nd_time_close.click()
                    
                        
                    if new != round_2nd_no:
                        history = get_2nd_time.text
                        break
                       
                re_history = re.sub('x', '0', history)
                a.append(float(re_history))
                try:
                    self.saveCsv(round_value, time_value, re_history)
                except:
                    print("error")
                if float(re_history) < 2 and new != round_2nd_no:
                    self.bet_counter.append("true")
                    self.bet_purple = []
                else:
                    if float(re_history) < 10:
                        self.bet_purple.append("true")
                    else:
                        self.bet_purple = []
                    self.bet_counter = []
                print(f"Blue: {self.bet_counter}")
                print(f"Purple: {self.bet_purple}")

                #  BETTING
                if self.bet_status == True:
                    if float(re_history) > 2:
                        self.stake()
                        self.betting()
                        sleep(4.5)
                    else:
                        self.bet_status = False
                        self.bet_amount = 25
                        self.stake()
                        self.false_blue = False
                        bet_counter = []
                if len(self.bet_purple) == 4 and new != round_2nd_no:
                    self.betting()
                    self.false_blue = True
                    sleep(4.5)
                if len(self.bet_counter) == 4 and new != round_2nd_no and self.false_blue == False:
                    self.betting()
                    sleep(4.5)
                if float(re_history) > 10 and float(re_history) < 25:
                    self.betting()
                    self.false_blue = True
                    sleep(4.5)
                    
                d = np.transpose(a).shape
                
                # Making Bet
                bet_store.append(float(re_history))
                
                # Increment
                current_value = current_value + 1
                new = round_2nd_no
                # Saving rounds
                
                
                # Exiting the Loop
                if limit == current_value:
                    aps = False
            except:
                
                # get_2nd_time_close = self.driver.find_element('xpath', '/html/body/ngb-modal-window/div/div/app-fairness/div[1]/button')
                # get_2nd_time_close.click()
                
                # try:
                #     if len(self.bet_counter) >= 4 and new != round_2nd_no and self.bet_status == False:
                #         self.betting()
                    
                # except:
                #     continue
                
                continue
        # Saving the dataset
        

    def saveCsv(self, round_value, time_value, re_history):
        new_df = pd.DataFrame([{"Round":round_value, "Time":time_value, "Payout":float(re_history)}])
        self.df = pd.concat([self.df, new_df], ignore_index=True)
        print(self.df)
        self.df.to_csv("mynewdata2.csv")


    def stake(self):
        n_stake = self.driver.find_element('xpath', '/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/div[1]/div[1]/app-spinner/div/div[2]/input')
        working = True
        while working:
            try:
                self.action.move_to_element(n_stake).click().perform()
                n_stake.send_keys(Keys.BACKSPACE)
                n_stake.send_keys(Keys.BACKSPACE)
                n_stake.send_keys(Keys.BACKSPACE)
                n_stake.send_keys(Keys.BACKSPACE)
                n_stake.send_keys(Keys.BACKSPACE)
                n_stake.send_keys(f"{self.bet_amount}.")
                working = False
            except:
                continue
            
        

    def betting(self):
        cal = True
        self.true = True
        # self.bet_status = True
        bet = self.driver.find_element('xpath', '/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/div[1]/div[2]/button/span/label[1]')
        while cal:
            try:
                self.action.move_to_element(bet).click().perform()
                cal = False
            except:
                continue
        self.bet_status = True
        self.bet_amount = self.bet_amount + self.bet_amount

    

def main():
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python your_automation_script.py <phone_number> <password>")
        sys.exit(1)

    phone_number = sys.argv[1]
    password = sys.argv[2]
    bot = SportyBot()
    bot.open_tinder()
    bot.login(phone_number, password)
    bot.aviator()
    bot.history()
    bot.stake()
    bot.stimulation()

    # Use the phone_number and password in your automation script
    # print("Phone number:", phone_number)
    # print("Password:", password)

    # Add your automation logic here

if __name__ == "__main__":
    main()
