import random
import networkx as nx

# Simulated Tor network with relays and users
class TorNetwork:
    def __init__(self, num_users=5, num_relays=10):
        self.graph = nx.Graph()
        self.num_users = num_users
        self.num_relays = num_relays
        self.users = [f"User_{i}" for i in range(num_users)]
        self.relays = [f"Relay_{i}" for i in range(num_relays)]
        self.destinations = [f"Website_{i}" for i in range(3)]  # Possible destinations
        self.adversary_as = random.choice(self.relays)  # Adversary-controlled relay

        # Add nodes to the network
        self.graph.add_nodes_from(self.users + self.relays + self.destinations)

        # Randomly connect users to relays
        for user in self.users:
            entry = random.choice(self.relays)
            self.graph.add_edge(user, entry)

        # Randomly connect relays to each other (simulating Tor nodes)
        for _ in range(num_relays * 2):
            a, b = random.sample(self.relays, 2)
            self.graph.add_edge(a, b)

        # Connect exit relays to destinations
        for relay in self.relays:
            destination = random.choice(self.destinations)
            self.graph.add_edge(relay, destination)

    def get_random_path(self, user):
        """Selects a Tor circuit: Entry → Middle → Exit → Destination"""
        entry = random.choice(self.relays)
        middle = random.choice([r for r in self.relays if r != entry])
        exit_node = random.choice([r for r in self.relays if r not in {entry, middle}])
        destination = random.choice(self.destinations)
        return [user, entry, middle, exit_node, destination]