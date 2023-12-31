data = "2512393914141839183912122d2d1913121913121f1f1f1f39393215321539391f171f1731312e122e12131213121f121f12141439392222131e131e1417141714161416131312120e0e0e0e202012123939211821181313393915151816181613133939161631312f1e2f1e0e0e0e110e1e111e2f122f121317131731223122"

# Define scan code to key mapping for the Norwegian keyboard layout
key_mapping = {
    0x10: "q",
    0x11: "w",
    0x12: "e",
    0x13: "r",
    0x14: "t",
    0x15: "y",
    0x16: "u",
    0x17: "i",
    0x18: "o",
    0x19: "p",
    0x1A: "å",
    0x1B: "¨",
    0x1C: "Enter",
    0x1E: "a",
    0x1F: "s",
    0x20: "d",
    0x21: "f",
    0x22: "g",
    0x23: "h",
    0x24: "j",
    0x25: "k",
    0x26: "l",
    0x27: "ø",
    0x28: "æ",
    0x29: "'",
    0x2B: "`",
    0x2C: "z",
    0x2D: "x",
    0x2E: "c",
    0x2F: "v",
    0x30: "b",
    0x31: "n",
    0x32: "m",
    0x33: ",",
    0x34: ".",
    0x35: "-",
    0x39: " ",
    0x08: "BACKSPACE",
    0x09: "TAB",
    0x0D: "ENTER",
    0x1B: "ESC",
    0x20: "MELLOMROM",
    0x21: "SIDE OPP",
    0x22: "SIDE NED",
    0x23: "SLUTT",
    0x24: "HJEM",
    0x25: "VENSTRE PIL",
    0x26: "OPP PIL",
    0x27: "HØYRE PIL",
    0x28: "NED PIL",
    0x2D: "SETT INN",
    0x2E: "SLETT",
    0x30: "0",
    0x31: "1",
    0x32: "2",
    0x33: "3",
    0x34: "4",
    0x35: "5",
    0x36: "6",
    0x37: "7",
    0x38: "8",
    0x39: "9",
    0x41: "A",
    0x42: "B",
    0x43: "C",
    0x44: "D",
    0x45: "E",
    0x46: "F",
    0x47: "G",
    0x48: "H",
    0x49: "I",
    0x4A: "J",
    0x4B: "K",
    0x4C: "L",
    0x4D: "M",
    0x4E: "N",
    0x4F: "O",
    0x50: "P",
    0x51: "Q",
    0x52: "R",
    0x53: "S",
    0x54: "T",
    0x55: "U",
    0x56: "V",
    0x57: "W",
    0x58: "X",
    0x59: "Y",
    0x5A: "Z",
    0xBA: "Æ",
    0xBB: "+",
    0xBC: ",",
    0xBD: "-",
    0xBE: ".",
    0xBF: "/",
    0xC0: "Ø",
    0xDB: "Å",
    0xDC: "'",
    0xDD: "¨",
    0xDE: "*"
}


# Decode hexadecimal data to bytes
bytes_data = bytes.fromhex(data)

# Decode bytes to a string using ASCII encoding
keystrokes = bytes_data.decode("ascii")

# Map scan codes to keys and print the resulting keystrokes
result = ""
for scan_code in bytes_data:
    if scan_code in key_mapping:
        result += key_mapping[scan_code]

print(result)
