import tor
import raptor
import matplotlib.pyplot as plt
import networkx as nx

def draw_tor_network(tor_network, adversary):
    plt.figure(figsize=(10, 7))

    pos = nx.spring_layout(tor_network.graph)  # Position nodes

    # Draw nodes with different colors
    nx.draw_networkx_nodes(tor_network.graph, pos, nodelist=tor_network.users, node_color="green", node_size=800, label="Users")
    nx.draw_networkx_nodes(tor_network.graph, pos, nodelist=tor_network.relays, node_color="gray", node_size=500, label="Relays")
    nx.draw_networkx_nodes(tor_network.graph, pos, nodelist=tor_network.destinations, node_color="red", node_size=800, label="Websites")
    nx.draw_networkx_nodes(tor_network.graph, pos, nodelist=[adversary], node_color="blue", node_size=900, label="Adversary AS")

    # Draw edges
    nx.draw_networkx_edges(tor_network.graph, pos, alpha=0.5)
    nx.draw_networkx_labels(tor_network.graph, pos, font_size=8)

    plt.title("Tor Network Visualization with Adversary AS")
    plt.legend()
    plt.show()

def main():
    # Run Simulation
    t = tor.TorNetwork(num_users=5, num_relays=10)
    r = raptor.RAPTOR_Attack(t)

    # Simulating user traffic through Tor
    #for _ in range(1000):
    for user in t.users:
        path = t.get_random_path(user)
        print(f"{user} path: {path}")
        r.monitor_traffic(path)

    # Correlate traffic to perform the attack
    r.correlate_traffic()

    # Show the traffic the adversary observed
    print(r.observed_traffic)

    # Draw the network
    draw_tor_network(t, t.adversary_as)

if __name__ == "__main__":
    main()