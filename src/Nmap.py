import subprocess

class Nmap(object):
    def __init__(self, IP):
        self.IP = IP
        self.result = "" 

    @staticmethod
    def default_scan(IP):
        _scan_result_str = subprocess.run(["sudo", "bash", "-c", f"nmap -sn {IP}"], capture_output=True, text=True)
        _filtered_result = _scan_result_str.stdout.split("\n")
        return _filtered_result

    def _scan_structure(self, command):
        _scan_result_str = subprocess.run(["sudo", "bash", "-c", f"{command} {self.IP}"], capture_output=True, text=True)
        _filtered_result = _scan_result_str.stdout.split("\n")
        return _filtered_result
    
    def port_scan(self, port_range):
        return self._scan_structure(f"nmap -T5 --top-ports {port_range} -sS")

