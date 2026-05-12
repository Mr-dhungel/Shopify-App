import subprocess
import time

BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
USER_DATA_DIR = r"C:\Users\Mukunda\AppData\Local\BraveSoftware\Brave-Browser\User Data"

subprocess.Popen([
    BRAVE_PATH,
    f'--user-data-dir={USER_DATA_DIR}',
    '--profile-directory=Default',
    '--remote-debugging-port=9222'
])

time.sleep(5)

print("Browser launched with CDP")