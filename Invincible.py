import keyboard
import webbrowser

typed_text = ""

def check_input(event):
    global typed_text
    typed_text += event.name if event.name.isalnum() else ""
    
    if "invincible" in typed_text:
        webbrowser.open("https://www.youtube.com/watch?v=7s0nIxBLZio")
        typed_text = ""  # Reset after triggering

keyboard.on_press(check_input)
keyboard.wait()
