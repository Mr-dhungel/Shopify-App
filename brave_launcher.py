import subprocess
import time
from config.settings import BRAVE_PATH, BRAVE_USER_DATA_DIR

subprocess.Popen([
    BRAVE_PATH,
    f'--user-data-dir={BRAVE_USER_DATA_DIR}',
    '--profile-directory=Default',
    '--remote-debugging-port=9222'
])

time.sleep(5)

print("Browser launched with CDP")