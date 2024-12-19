import time
import pyshark

def capture_traffic(input_file=None):
    """
    Capture network traffic.
    If input_file is provided, reads traffic from the file; otherwise captures live traffic for 10 seconds.
    """
    if input_file:
        print(f"Reading traffic from file: {input_file}")
        capture = pyshark.FileCapture(input_file)
    else:
        print("Capturing live traffic for 10 seconds...")
        capture = pyshark.LiveCapture(interface='any')
        capture.sniff(timeout=10)
    
    packets = [packet for packet in capture]
    print(f"Captured {len(packets)} packets.")
    return packets
