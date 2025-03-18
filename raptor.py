import random
import time

# RAPTOR Attack: Passive Traffic Analysis
class RAPTOR_Attack:
    def __init__(self, tor_network):
        self.network = tor_network
        self.observed_traffic = {}  # Store observed traffic (packet size, timing)

    def monitor_traffic(self, path):
        """Simulates an AS monitoring both entry and exit traffic"""
        user, entry, middle, exit_node, destination = path

        # Simulated packet size & timing pattern (real attack uses more sophisticated methods)
        packet_size = random.randint(800, 1200)  # Simulated packet size in bytes
        timestamp = round(time.time(), 2)  # Current time

        # Adversary observes entry and exit traffic
        if entry == self.network.adversary_as or exit_node == self.network.adversary_as:
            print(f"Adversary AS Monitoring: {entry if entry == self.network.adversary_as else exit_node}")
            self.observed_traffic[user] = (packet_size, timestamp, destination)

    def correlate_traffic(self):
        """Check if any two monitored users have similar traffic patterns"""
        for user1 in list(self.observed_traffic.keys()):
            size1, time1, dest1 = self.observed_traffic[user1]

            for user2 in list(self.observed_traffic.keys())[1:]:
                size2, time2, dest2 = self.observed_traffic[user2]

                if user1 != user2 and abs(time1 - time2) <= 0.3 and size1 == size2:
                    print(f"Deanonymized: {user1} and {user2} visited {dest1}")
