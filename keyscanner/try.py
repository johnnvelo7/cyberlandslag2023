import keyboard

filename = "scancodes.txt"
processed_codes = set()

def on_press(event):
    if event.scan_code not in processed_codes:
        with open(filename, "a") as f:
            f.write("0x{:02X}: \"{}\"\n".format(event.scan_code, event.name))
        processed_codes.add(event.scan_code)

keyboard.hook(on_press)

keyboard.wait()
