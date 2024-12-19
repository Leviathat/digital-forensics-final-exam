def analyze_traffic(packets):
    """
    Analyze captured packets to extract useful information.
    Returns a dictionary with analysis results.
    """
    print("Analyzing traffic...")

    analysis_results = {
        'total_packets': len(packets),
        'protocol_counts': {},
        'src_ip_counts': {},
        'dst_ip_counts': {},
    }

    for packet in packets:
        try:
            # Protocol
            protocol = packet.highest_layer
            analysis_results['protocol_counts'][protocol] = analysis_results['protocol_counts'].get(protocol, 0) + 1

            # Source IP
            src_ip = packet.ip.src
            analysis_results['src_ip_counts'][src_ip] = analysis_results['src_ip_counts'].get(src_ip, 0) + 1

            # Destination IP
            dst_ip = packet.ip.dst
            analysis_results['dst_ip_counts'][dst_ip] = analysis_results['dst_ip_counts'].get(dst_ip, 0) + 1
        except AttributeError:
            # Skip packets that don't have IP layers
            continue

    print("Analysis complete.")
    return analysis_results
