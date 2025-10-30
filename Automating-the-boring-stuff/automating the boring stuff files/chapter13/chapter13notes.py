''' modules, which make it easy to scrape web pages in Python:

webbrowser Comes with Python and opens a browser to a specific page

requests Downloads files and web pages from the internet

Beautiful Soup (bs4) Parses HTML, the format that web pages are written in, to extract the information you want

Selenium Launches and controls a web browser, such as by filling in forms and simulating mouse clicks

Playwright Launches and controls a web browser; newer than Selenium and has some additional features'''



#The requests module lets you easily downlaod files from the web without having to worry about complicated issues such as network erros, connection routing and data comporession.

import requests
import bs4
from traitlets import All
'''

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
print(res.status_code == requests.codes.ok)

print(len(res.text))
print(res.text[:100])



#checking for errors
res =  requests.get('https://inventwithpython.com/page_that_does_not_exist')



try:
    res.raise_for_status() #if download fails, this line will raise an exception
except Exception as exc:
    print(f'There was a problem: {exc}')
    
    
    
#saving downloaded files to the hard drive
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
with open('RomeoAndJuliet.txt', 'wb') as playFile:
    for chunk in res.iter_content(100000):
        playFile.write(chunk)'''
        
        
        
#Call requests.get() to download the file.
#Call open() with 'wb' to create a new file in write binary mode.
#Loop over the Response object’s iter_content() method.
#Call write() on each iteration to write the content to the file.

#weather web scraping
'''import matplotlib.pyplot as plt

lat="52.19566"
long="0.12409"
start_date="2025-10-22"
end_date="2025-10-23"



pathtemp="https://api.open-meteo.com/v1/forecast\
?latitude="+lat+"&longitude="+long+"&hourly=\
temperature_2m&start_date="+start_date+"&end_date="+end_date

pathwind="https://api.open-meteo.com/v1/forecast\
?latitude="+lat+"&longitude="+long+"&hourly=\
wind_speed_10m&start_date="+start_date+"&end_date="+end_date

pathhumid="https://api.open-meteo.com/v1/forecast\
?latitude="+lat+"&longitude="+long+"&hourly=\
relative_humidity_2m&start_date="+start_date+"&end_date="+end_date



temp=requests.get(pathtemp)
wind = requests.get(pathwind)
humid = requests.get(pathhumid)





data_time=temp.json()['hourly']['time']
data_temp=temp.json()['hourly']['temperature_2m']
data_wind =wind.json()['hourly']['wind_speed_10m']
data_humid =humid.json()['hourly']['relative_humidity_2m']



# set figure size before plotting
fig, ax = plt.subplots(figsize=(15, 6))

# set titles and labels
ax.set_title("temperaturesovertime")
ax.set_xlabel("time")
ax.set_ylabel("temperature")

# rotate x-ticks
plt.xticks(rotation=90)

# plot the data
ax.plot(data_time, data_temp)

# show the plot
plt.show()


fig, ax = plt.subplots(figsize = (15,6))
ax.set_title("windovertime")
ax.set_xlabel("time")
ax.set_ylabel("windmagnitude")

# rotate x-ticks
plt.xticks(rotation=90)

# plot the data
ax.plot(data_time, data_wind)

# show the plot
plt.show()




fig, ax = plt.subplots(figsize = (15,6))
ax.set_title("humidityovertime")
ax.set_xlabel("time")
ax.set_ylabel("humiditymagnitude")

# rotate x-ticks
plt.xticks(rotation=90)

# plot the data
ax.plot(data_time, data_humid)

# show the plot
plt.show()'''





#Using HTML


#print hello world in HTML
#<b>Hello, World!</b>


#dont use regex to parse HTML, because HTML is not a regular language and regex will fail on many valid HTML documents.

#intro to Beautiful Soup


#if you need to get info off a webs doesnt have an API, you can use web scraping to extract the info you need directly from the HTML of the web page.


res = requests.get('https://autbor.com/example3.html')
res.raise_for_status()
example_soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(example_soup))


#you can also open html files stored on your hard drive by passing a file object to BeautifulSoup instead of a string of HTML.
#example_file = open('example.html')
#example_soup = bs4.BeautifulSoup(example_file, 'html.parser')
#type(example_soup)



#Finding an element with the select() method
#The select() method returns a list of Tag objects, even if there is only one object

#soup.select('div')

#All elements named <div>

#soup.select('#author')

#The element with an id attribute of author

#soup.select('.notice')

#All elements that use a CSS class attribute named notice

#soup.select('div span')

#All elements named <span> that are within an element named <div>

#soup.select('div > span')

#All elements named <span> that are directly within an element named <div>, with no other element in between

#soup.select('input[name]')

#All elements named <input> that have a name attribute with any value

#soup.select('input[type="button"]')

#All elements named <input> that have an attribute named type with the value button


#example usage of select()
'''example_file = open('example3.html')
example_soup = bs4.BeautifulSoup(example_file, 'html.parser')
elems = example_soup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(str(elems[0]))
print(elems[0].getText())
print(elems[0].attrs)'''


'''
p_elems = example_soup.select('p')

print(str(p_elems[0]))
#'<p>This <p> tag puts <b>content</b> into a <i>single</i> paragraph.</p>'

print(p_elems[0].getText()
'This <p> tag puts content into a single paragraph.'
print(str(p_elems[1])
'<p> <a href="https://inventwithpython.com/”>This text is a link</a> to books by
<span id="author">Al Sweigart</span>.</p>'
print(p_elems[1].getText())''
'This text is a link to books by Al Sweigart.'
print(str(p_elems[2]))
'<p><img alt="Close-up of my cat Zophie." src="wow_such_zophie_thumb.webp"/></p>'
print(p_elems[2].getText())
'''


#This time, select() gives us a list of three matches,
# which we store in p_elems. Using str() on p_elems[0], p_elems[1], and p_elems[2] shows you each element as a string, 
# and using gettext() on each element shows you its text.

#Getting data from an element's attributes

# the get() method on a Tag object retrieves the value of an attribute, such as href or src.
'''example_file = open('example3.html')
example_soup = bs4.BeautifulSoup(example_file, 'html.parser')
link_elem = example_soup.select('a')[0]
print(link_elem.get('href'))
print(link_elem.get('id'))# author
print(link_elem.get('class'))# ['external', 'link']'''




#controlling a web browser with selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com  ')


#browser.back()
#browser.forward()
#browser.refresh()
#browser.quit()
browser.quit()

'''By.CLASS_NAME

Elements that use the CSS class name

By.CSS_SELECTOR

Elements that match the CSS selector

By.ID

Elements with a matching id attribute value

By.LINK_TEXT

<a> elements that completely match the text provided

By.PARTIAL_LINK_TEXT

<a> elements that contain the text provided

By.NAME

Elements with a matching name attribute value

By.TAG_NAME

Elements with a matching tag name (case-insensitive; an <a> element is matched by 'a' and 'A')'''



'''tag_name

The tag name, such as 'a' for an <a> element.

get_attribute(name)

The value for the element’s name attribute, like href in an <a> element.

get_property(name)

The value for the element’s property, which does not appear in the HTML code. Some examples of HTML properties are innerHTML and innerText.

text

The text within the element, such as 'hello' in the following: <span>hello </span>

clear()

For text field or text area elements, clears the text entered into it.

is_displayed()

Returns True if the element is visible; otherwise, returns False.

is_enabled()

For input elements, returns True if the element is enabled; otherwise, returns False.

is_selected()

For checkbox or radio button elements, returns True if the element is selected; otherwise, returns False.

location

A dictionary with keys 'x' and 'y' for the position of the element in the page.

size

A dictionary with keys 'width' and 'height' for the size of the element in the page'''

from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get('https://autbor.com/example3.html')
elems = browser.find_elements(By.CSS_SELECTOR, 'p')
print(elems[0].text)
print(elems[0].get_property('innerHTML'))


browser.quit()

#clicking elements on a page
browser = webdriver.Firefox()

browser.get('https://autbor.com/example3.html')
link_elem = browser.find_element(By.LINK_TEXT, 'This text is a link')
type(link_elem)
link_elem.click()



#fillig out and submitting forms
browser = webdriver.Firefox()
browser.get('https://autbor.com/example3.html')
user_elem = browser.find_element(By.ID, 'login_user')
user_elem.send_keys('your_real_username_here')
password_elem = browser.find_element(By.ID, 'login_pass')
password_elem.send_keys('your_real_password_here')
password_elem.submit()



#sending special keys
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()


'''Keys.ENTER  Keys.PAGE_UP       Keys.DOWN
Keys.RETURN  Keys.ESCAPE        Keys.LEFT
Keys.HOME    Keys.BACK_SPACE    Keys.RIGHT
Keys.END     Keys.DELETE        Keys.TAB
Keys.PAGE_DOWN   Keys.UP        Keys.F1 to Keys.F12'''


browser = webdriver.Firefox()
browser.get('https://nostarch.com')
html_elem = browser.find_element(By.TAG_NAME, 'html')
html_elem.send_keys(Keys.END)  # Scrolls to bottom
html_elem.send_keys(Keys.HOME)  # Scrolls to top


#controlling a browser with playwright
from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:
    browser = playwright.firefox.launch()
    page = browser.new_page()
    page.goto('https://autbor.com/example3.html')
    print(page.title())
    browser.close()
    
    
    #You may have noticed that no browser window appeared at all, because, by default, Playwright runs in headless mode.
    
playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=50)
page = browser.new_page()
page.goto('https://autbor.com/example3.html')
browser.close()
playwright.stop()

#clicking browser buttons
#page.go_back() Clicks the Back button

#page.go_forward() Clicks the Forward button

#page.reload() Clicks the Refresh/Reload button

#page.close() Clicks the Close Window button


#finding elements on the page

'''page.get_by_role(role, name=label)

Elements by their role and optionally their label

page.get_by_text(text)

Elements that contain text as part of their inner text

page.get_by_label(label)

Elements with matching <label> text as label

page.get_by_placeholder(text)

<input> and <textarea> elements with matching placeholder attribute values as the text provided

page.get_by_alt_text(text)

<img> elements with matching alt attribute values as the text provided

page.locator(selector)

Elements with a matching CSS or XPath selector'''



#methods
'''get_attribute(name)

Returns the value for the element’s name attribute, such as 'https://nostarch.com' for the href attribute in an <a href="https://nostarch.com"> element.

count()

Returns an integer of the number of matching elements in this Locator object.

nth(index)

Returns a Locator object of the matching element given by the index. For example, nth(3) returns the fourth matching element since index 0 is the first matching element.

first

The Locator object of the first matching element. This is the same as nth(0).

last

The Locator object of the last matching element. If there are, say, five match elements, this is the same as nth(4).

all()

Returns a list of Locator objects for each individual matching element.

inner_text()

Returns the text within the element, such as 'hello' in <b>hello</b>.

inner_html()

Returns the HTML source within the element, such as '<b>hello</b>' in <b>hello</b>.

click()

Simulates a click on the element, which is useful for link, checkbox, and button elements.

is_visible()

Returns True if the element is visible; otherwise, returns False.

is_enabled()

For input elements, returns True if the element is enabled; otherwise, returns False.

is_checked()

For checkbox or radio button elements, returns True if the element is selected; otherwise, returns False.

bounding_box()

Returns a dictionary with keys 'x' and 'y' for the position of the element’s top-left corner in the page, along with keys 'width' and 'height' for the element’s size.'''

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://autbor.com/example3.html')
    elems = page.locator('p')
    print(elems.nth(0).inner_text())
    print(elems.nth(0).inner_html())
    
    
playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=50)
page = browser.new_page()
page.goto('https://autbor.com/example3.html')
 
page.click('input[type=checkbox]')  # Checks the checkbox
page.click('input[type=checkbox]')  # Unchecks the checkbox
page.click('a')  # Clicks the link
page.go_back()
checkbox_elem = page.get_by_role('checkbox')  # Calls a Locator method
checkbox_elem.check()  # Checks the checkbox
checkbox_elem.uncheck()  # Unchecks the checkbox
checkbox_elem.set_checked(True)  # Checks the checkbox
checkbox_elem.set_checked(False)  # Unchecks the checkbox
page.get_by_text('is a link').click()  # Uses a Locator method
browser.close()
playwright.stop()



#filling out and submitting forms
playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=50)
page = browser.new_page()
page.goto('https://autbor.com/example3.html')
page.locator('#login_user').fill('your_real_username_here')
page.locator('#login_pass').fill('your_real_password_here')
page.locator('input[type="submit"]').click()
browser.close()
playwright.stop()

#sending special keys
playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=50)
page = browser.new_page()
page.goto('https://autbor.com/example3.html')
page.locator('html').press('End')  # Scrolls to bottom
page.locator('html').press('Home')  # Scrolls to top
browser.close()
playwright.stop()


#main special characters
''''Backquote'    'Escape'    'ArrowDown'
'Minus'     'End'       'ArrowRight'
'Equal'     'Enter'     'ArrowUp'
'Backslash' 'Home'      'F1' to 'F12'
'Backspace' 'Insert'    'Digit0' to 'Digit9'
'Tab'       'PageUp'    'KeyA' to 'KeyZ'
'Delete'    'PageDown'  
'Space'    '''



#practice questions:

#  1.  Briefly describe the differences between the webbrowser, requests, and bs4 modules.

# 2.  What type of object is returned by requests.get()? How can you access the downloaded content as a string value?

# 3.  What requests method checks that the download worked?

# 4.  How can you get the HTTP status code of a requests response?

# 5.  How do you save a requests response to a file?

#  6.  What two formats do most online APIs return their responses in?

#  7.  What is the keyboard shortcut for opening a browser’s Developer Tools?

#  8.  How can you view (in the Developer Tools) the HTML of a specific element on a web page?

#  9.  What CSS selector string would find the element with an id attribute of main?

#10.  What CSS selector string would find the elements with an id attribute of highlight?

#11.  Say you have a Beautiful Soup Tag object stored in the variable spam for the element <div>Hello, world!</div>. How could you get a string 'Hello, world!' from the Tag object?

#12.  How would you store all the attributes of a Beautiful Soup Tag object in a variable named link_elem?

#13.  Running import selenium doesn’t work. How do you properly import Selenium?

#14.  What’s the difference between the find_element() and find_elements() methods in Selenium?

#15.  What methods do Selenium’s WebElement objects have for simulating mouse clicks and keyboard keys?

#16.  In Playwright, what locator method call simulates pressing CTRL-A to select all the text on the page?

#17.  How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with Selenium?

#18.  How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with Playwright?

#answers:
#1. webbrowser opens a web browser to a specific page, requests downloads files and web pages from the internet, and bs4 parses HTML to extract information.
#2. requests.get() returns a Response object. You can access the downloaded content as a string value using the .text attribute of the Response object.
#3. The raise_for_status() method checks that the download worked.
#4. You can get the HTTP status code of a requests response using the .status_code
#5. You can save a requests response to a file by opening a file in write-binary mode and writing the content using the iter_content() method of the Response object.
#6. Most online APIs return their responses in JSON and XML formats.
#7. The keyboard shortcut for opening a browser’s Developer Tools is F12 or Ctrl+
#8. You can view the HTML of a specific element on a web page by right-clicking the element and selecting "Inspect" in the Developer Tools.
#9. The CSS selector string to find the element with an id attribute of main is '#
#10. The CSS selector string to find the elements with an id attribute of highlight is '#highlight'.
#11. You can get the string 'Hello, world!' from the Tag object using the .getText() method.
#12. You can store all the attributes of a Beautiful Soup Tag object in a variable named link_elem using the .attrs attribute.
#13. You properly import Selenium using 'from selenium import webdriver'.
#14. The find_element() method returns a single WebElement object, while find_elements() returns a list of WebElement objects.
#15. Selenium’s WebElement objects have the click() method for simulating mouse clicks and the send_keys() method for simulating keyboard keys.
#16. In Playwright, you can simulate pressing CTRL-A to select all the text on the page using 'page.locator("html").press("Control+A")'.
#17. You can simulate clicking a browser’s Forward, Back, and Refresh buttons with Selenium using the browser.forward(), browser.back(), and browser.refresh() methods.
#18. You can simulate clicking a browser’s Forward, Back, and Refresh buttons with Playwright using the page.go_forward(), page.go