import speech_recognition as sr
import webbrowser
import tkinter as tk
from threading import Thread

# Function to open links based on recognized text
def open_link(text):
    links = {
        "invincible": "https://www.youtube.com/watch?v=7s0nIxBLZio",
        "invisible": "https://www.youtube.com/watch?v=7s0nIxBLZio",  # Common misinterpretation
        "are you sure": "https://www.youtube.com/watch?v=Mc2hzULTFEs",
        "balls": "https://www.youtube.com/watch?v=04dIAa4Rn4M",
        "ball": "https://www.youtube.com/watch?v=04dIAa4Rn4M",  # Common misinterpretation of "balls"
        "beam attack": "https://www.youtube.com/watch?v=DRfR6Q9iInw",
        "deez nuts": "https://www.youtube.com/watch?v=66I78hXXwvk",  # Added new phrase and link
        "these nuts": "https://www.youtube.com/watch?v=66I78hXXwvk",  # Failsafe for "deez nuts"
        "how was the fall": "https://www.youtube.com/watch?v=hNA-hRy6GeQ"  # Added new phrase and link
    }
    found = False
    for keyword, url in links.items():
        if keyword in text:
            webbrowser.open(url)
            log_message(f"Opening link for: {keyword}")
            found = True
    if not found:
        log_message("No matching keyword found in the sentence.")

# Function to log messages in the GUI
def log_message(message):
    output_text.insert(tk.END, message + "\n")
    output_text.see(tk.END)

# Function to start speech recognition
def start_recognition():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        log_message("Listening... Say something!")
        while running:  # Run continuously while the process is active
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio).lower()
                log_message(f"You said: {text}")
                open_link(text)
            except sr.UnknownValueError:
                log_message("Could not understand what you said.")
            except sr.RequestError as e:
                log_message(f"Request error from Google Speech Recognition service: {e}")
            except Exception as e:
                log_message(f"An error occurred: {e}")

# Function to start the recognition thread
def start_thread():
    global running
    running = True
    recognition_thread = Thread(target=start_recognition)
    recognition_thread.daemon = True
    recognition_thread.start()

# Function to stop the recognition process
def stop_recognition():
    global running
    running = False
    log_message("Stopped listening.")

# Create the GUI
root = tk.Tk()
root.title("Speech Recognition")

# Add buttons and text box to the GUI
start_button = tk.Button(root, text="Start Listening", command=start_thread, width=20)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Listening", command=stop_recognition, width=20)
stop_button.pack(pady=10)

output_text = tk.Text(root, height=15, width=50)
output_text.pack(pady=10)

# Run the GUI event loop
root.mainloop()