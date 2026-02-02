import subprocess
import sys
from watchfiles import run_process

def start():
    run_process(
        ".",
        target=subprocess.run,
        args=([sys.executable, "main.py"],),
    )

if __name__ == "__main__":
    start()