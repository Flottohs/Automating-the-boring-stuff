'''Let’s say that part of your job is to copy the URLs for links on a web page and paste them into a spreadsheet. (In Chapter 13, you’ll learn how to scrape all the links for the HTML source of the page. But let’s say you only need to copy some of them, and a human must decide which ones on a case-by-case basis.) You could follow these steps:

  1.  Right-click a link in a web browser.

  2.  Select the Copy Link or Copy Link Address item from the context menu.

  3.  Switch to the spreadsheet app.

  4.  Press CTRL-V to paste the link.

  5.  Switch back to the web browser.'''
  
'''This is a boring task, especially if the page has dozens or hundreds of links. Let’s create a small clipboard-recording program to make it faster. We’ll deploy this program on our computer so that we can conveniently run it when needed. Our program will monitor the clipboard to see if new text has been copied to it, and if so, it will print it to the terminal screen. This way, we can convert our five-step process into a two-step process:

  1.  Right-click a link in a web browser.

  2.  Select the Copy Link or Copy Link Address item from the context menu.

Then, the user can just copy all the text from the clipboard recorder’s terminal window and paste it into the spreadsheet at once. Enter the following into the file editor and save it as cliprec.py:'''



import pyperclip, time

print('Recording clipboard... (Ctrl-C to stop)')
previous_content = ''
try:
    while True:
        content = pyperclip.paste()  # Get clipboard contents.
       
        if content != previous_content:
            # If it's different from the previous, print it:
            print(content)
            previous_content = content

        time.sleep(0.01)  # Pause to avoid hogging the CPU.
except KeyboardInterrupt:
    pass
