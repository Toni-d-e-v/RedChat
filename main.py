import sys
import time
import socket   
hostname = socket.gethostname()   
IPAddr = socket.gethostbyname(hostname)   
from node import server

args = sys.argv
port_arg = args[1]
seed_arg = args[2]
# P2P storage
# P2P network

# send data over p2p network




def start_node(port):
    IP = socket.gethostbyname(hostname) # get ip address of hostname
    node = server("127.0.0.1", port)
    print("Our IP:",IPAddr)
    node_list = []
    time.sleep(1)
    # Do not forget to start your node!
    node.start()
    # Connect with another node, otherwise you do not create any network!
    # Example of sending a message to the nodes (dict).
    # awaited while loop
    if seed_arg != "True":
        node.connect_with_node("127.0.0.1", 12345) # connect to seed node
        node.send_to_nodes({"message": "init1","register": "True", "port": port, "host": "127.0.0.1"})
        node.send_to_nodes({"message": "init"})

        while True:
            our_list = server.node_list
            print(our_list)
            # chat room
            # send message to all nodes
            input_msg = input("Enter message: ")
            if input_msg == "exit":
                break
            send_msg_chat(input_msg,node)

def send_msg(msg,node):
    print(f"Sending: {msg}")
    # send message to all nodes
    # for loop to connect to all nodes in server.node_list
    for i in range(len(server.node_list)):
        node.connect_with_node(server.node_list[i]["host"], server.node_list[i]["port"])
        node.send_to_nodes(msg)
        time.sleep(1)


def send_msg_chat(msg,node):
    print(f"Sending: {msg}")
    # send message to all nodes
    # for loop to connect to all nodes in server.node_list
    # out list = server/
    our_list = server.node_list
    print(our_list)

    print(server.node_list)
    for i in range(len(server.node_list)):
        #print(server.node_list[i])
        if port_arg != server.node_list[i]["port"]:
            node.connect_with_node(server.node_list[i]["host"], int(server.node_list[i]["port"]))
            node.send_to_nodes({"message": "msg", "msg": msg})
            break


start_node(int(port_arg))

