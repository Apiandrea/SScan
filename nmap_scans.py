import subprocess

def default_scan(IP):
    _scan_result_str = subprocess.run(["sudo", "bash", "-c", f"nmap -sn {IP}"], capture_output=True, text=True)
    _filtered_result = _scan_result_str.stdout.split("\n")
    return _filtered_result

def port_scan(IP):
    _scan_result_str = subprocess.run(["sudo", "bash", "-c", f"nmap -T5 --top-ports 50 -sS {IP}"], capture_output=True, text=True)
    _filtered_result = _scan_result_str.stdout.split("\n")
    return _filtered_result

