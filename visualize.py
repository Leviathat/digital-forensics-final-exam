import matplotlib.pyplot as plt

def visualize_traffic(analysis_results):
    """
    Visualize the traffic analysis results using matplotlib.
    """
    print("Visualizing traffic analysis results...")

    # Protocol distribution
    protocols = list(analysis_results['protocol_counts'].keys())
    protocol_counts = list(analysis_results['protocol_counts'].values())

    plt.figure(figsize=(10, 6))
    plt.bar(protocols, protocol_counts, color='skyblue')
    plt.title('Protocol Distribution')
    plt.xlabel('Protocol')
    plt.ylabel('Count')
    plt.show()

    # Source IP distribution
    src_ips = list(analysis_results['src_ip_counts'].keys())
    src_ip_counts = list(analysis_results['src_ip_counts'].values())

    plt.figure(figsize=(10, 6))
    plt.bar(src_ips, src_ip_counts, color='lightgreen')
    plt.title('Source IP Distribution')
    plt.xlabel('Source IP')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Destination IP distribution
    dst_ips = list(analysis_results['dst_ip_counts'].keys())
    dst_ip_counts = list(analysis_results['dst_ip_counts'].values())

    plt.figure(figsize=(10, 6))
    plt.bar(dst_ips, dst_ip_counts, color='salmon')
    plt.title('Destination IP Distribution')
    plt.xlabel('Destination IP')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    print("Visualization complete.")
