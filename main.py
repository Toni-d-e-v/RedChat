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


def start_node_seed(port):
    IP = socket.gethostbyname(hostname) # get ip address of hostname
    node = server("127.0.0.1", port)
    print("Our IP:",IPAddr)
    node_list = []
    time.sleep(1)
    # Do not forget to start your node!
    node.start()

# from messages list with dict get who and message

def get_strings_from_list_with_dict(list_with_dict):
    for i in range(len(list_with_dict)):
        msg = list_with_dict[i]["msg"]
        who = list_with_dict[i]["who"]

    return list_of_strings

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
        time.sleep(1)
        for i in range(len(server.node_list)):
            node.connect_with_node(server.node_list[i]["host"], server.node_list[i]["port"])
        import PySimpleGUI as sg

        sg.theme('DarkAmber')   # Add a touch of color
        # All the stuff inside your window.

        layout = [  
                    [sg.Text('RedChat P2P')],
                    # list all messages
                    [sg.Text('Send Message:'), sg.InputText()],
                    [sg.Button('Send'), sg.Button('Exit')] ]
        sg.Print('RedChat P2P - Messages:', do_not_reroute_stdout=False)
        # Create the Window
        window = sg.Window('RedChat P2P', layout)
        # Event Loop to process "events" and get the "values" of the inputs
        while True:


            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
                break
                sys.exit()
            message = {
                "who": "You",
                "msg": values[0]
            }
            server.messages.append(message)
            send_msg_chat(values[0],node)

        window.close()


def send_msg(msg,node):
    print(f"Sending: {msg}")
    # send message to all nodes
    # for loop to connect to all nodes in server.node_list
    for i in range(len(server.node_list)):
        node.connect_with_node(server.node_list[i]["host"], server.node_list[i]["port"])
        node.send_to_nodes(msg)
        time.sleep(1)


def send_msg_chat(msg,node):
    # send message to all nodes
    # for loop to connect to all nodes in server.node_list
    # out list = server/
    our_list = server.node_list
    print(f"You: {msg}")
    node.send_to_nodes({"message": "msg", "msg": msg})

if seed_arg == "False":
    start_node(int(port_arg))
else:
    start_node_seed(int(port_arg))


