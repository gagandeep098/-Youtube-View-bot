import webbrowser, time
url = input("ENTER URL: ")
t = input("ENTER DURATION: ")
for i in range(5):
  webbrowser.open_new(url)
  time.sleep(int(t))
