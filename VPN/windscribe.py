import os
import subprocess
import random
import VPN.servers as servers


class Windscribe:
    def __init__(self, user, password):
        """loads server list and logs into Windscribe"""
        self.login(user,password)

    def login(self, user, password):
        """logs into Windscribe using provided credentials"""
        commands = ["windscribe", "login"]
        proc = subprocess.Popen(commands, universal_newlines=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.stdin.write(user)
        proc.stdin.write(password)

    def locations(self):
        """prints the locations available to connect to in the shell"""
        # os.system("windscribe locations")
        print("\n".join(servers.server_free))
        

    def connect(self, server=None, rand=False):
        """connects to given server, best available server if no server given, or random server"""
        
        if rand:
            choice = random.choice(servers.server_free)
            os.system(f'windscribe connect "{choice}"')
        elif server != None:
            os.system(f'windscribe connect "{server}"')
        else:
            os.system("windscribe connect")
        
    
    def disconnect(self):
        """disconnect from the current server"""
        os.system("windscribe disconnect")

    def logout(self):
        """logout of windscribe"""
        os.system("windscribe logout")
