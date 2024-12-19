import pyshark

def live_capture(interface="eth0", packet_count=5):
    try:
        cap = pyshark.LiveCapture(interface=interface)
        print(f"Live Capture starts {interface}...")

        for packet in cap.sniff_continuously(packet_count=packet_count):
            print(packet)
    except Exception as e:
        print(f"ERRRR: {e}")

def existing_capture(filename):
    try:
        cap = pyshark.FileCapture(filename)
        packet = cap[0]
        print("1 packet:")
        print(packet)
        return packet
    except Exception as e:
        print(f"ERRRR: {e}")
        return None

def fetch_protocol_info(packet):
    protonums = {1: "ICMP", 
                 6: "TCP",
                 17: "UDP",
                 58: "IPv6-ICMP"}
    try:
        ip_layer = packet.ip
        protocol = None

        src_addr = ip_layer.src
        dst_addr = ip_layer.dst

        if ip_layer.version == "4":
            protocol = ip_layer.proto
        elif ip_layer.version == "6" and hasattr(ip_layer, 'nxt'):
            protocol = ip_layer.nxt

        return {
            "src_addr": src_addr,
            "dst_addr": dst_addr,
            "protocol": protonums.get(int(protocol), protocol)
        }
    except AttributeError as e:
        print(f"ERRRR: {e}")
        return None

live_capture(interface="Wi-Fi", packet_count=10)

packet = existing_capture(filename="ipv4frags.pcap")

if packet:
    info = fetch_protocol_info(packet)
    print("Protocol and adresses info: ")
    print(info)