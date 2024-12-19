from traffic import capture_traffic
from analyze import analyze_traffic
from visualize import visualize_traffic

def main():
    print("Starting network traffic analysis...")

    # Capture network traffic (from file or live)
    file = "ipv4frags.pcap"
    traffic_data = capture_traffic(file)

    # Analyze captured traffic
    analysis_results = analyze_traffic(traffic_data)

    # Visualize the analysis
    visualize_traffic(analysis_results)

if __name__ == "__main__":
    main()
