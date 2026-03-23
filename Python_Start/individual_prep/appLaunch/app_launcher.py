import webbrowser

# Test if we can launch your school portal directly in Brave
# Replace 'brave' with the path to your brave.exe if it's not the default
brave_path = "C:/Users/Richter Richard NAHO/AppData/Local/BraveSoftware/Brave-Browser/Application/brave.exe %s"
webbrowser.get(brave_path).open("https://alueducation.instructure.com")