import subprocess
import time
from config.settings import BRAVE_PATH, BRAVE_USER_DATA_DIR


class BrowserLauncher:
    """Brave Browser launcher for remote debugging"""

    def __init__(self, debugging_port: int = 9222):
        self.brave_path = BRAVE_PATH
        self.user_data_dir = BRAVE_USER_DATA_DIR
        self.debugging_port = debugging_port
        self.process = None

    def launch(self, wait_time: int = 5):
        """Launch Brave browser with remote debugging enabled"""
        self.process = subprocess.Popen(
            [
                self.brave_path,
                f"--user-data-dir={self.user_data_dir}",
                "--profile-directory=Default",
                f"--remote-debugging-port={self.debugging_port}",
            ]
        )

        time.sleep(wait_time)
        print(f"✅ Browser launched with CDP on port {self.debugging_port}")

    def close(self):
        """Close the browser process"""
        if self.process:
            self.process.terminate()
            self.process.wait()
            print("✅ Browser closed")


def launch_brave_browser(debugging_port: int = 9222):
    """Convenience function to launch Brave browser"""
    launcher = BrowserLauncher(debugging_port)
    launcher.launch()
    return launcher
