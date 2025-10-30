'''The game 2048 is a simple game in which you combine tiles by sliding them up, down, left, or right with the arrow keys. You can actually get a fairly high score by sliding tiles in random directions. Write a program that will open the game at https://play2048.co and keep sending up, right, down, and left keystrokes to automatically play the game.'''


from playwright.sync_api import sync_playwright
import random
import time

playwright =sync_playwright().start()
browser = playwright.firefox.launch(headless = False)
page = browser.new_page()
page.goto('https://play2048.co/')
    #click 

while page.inner_text != "Game Over":
    number = random.randint(0,3)
    if number == 0:
        page.locator('html').press('ArrowRight')
        
    if number ==1:
        page.locator('html').press('ArrowDown')
    if number == 2:
        page.locator('html').press('ArrowLeft')
    
    if number == 3:
        page.locator('html').press('ArrowUp')
        
if page.locator("button:has-text('Play Again')").is_visible():
    page.locator("button:has-text('Play Again')").click()
browser.close()
playwright.stop()
        

    
    

    