from p2pnetwork.node import Node
from p2pnetwork.nodeconnection import NodeConnection

class server (Node):
    node_list = [ ]
    new_list = [ ]


    # Python class constructor
    def __init__(self, host, port, id=None, callback=None, max_connections=0):
        super(server, self).__init__(host, port, id, callback, max_connections)

    def outbound_node_connected(self, connected_node):
        print("outbound_node_connected: " + connected_node.id)

    def inbound_node_connected(self, connected_node):
        print("inbound_node_connected: " + connected_node.id)

        # send them node list

    def inbound_node_disconnected(self, connected_node):
        print("inbound_node_disconnected: " + connected_node.id)
        self.node_list.remove(connected_node)
    def outbound_node_disconnected(self, connected_node):
        print("outbound_node_disconnected: " + connected_node.id)
        self.node_list.remove(connected_node)
        print("node_list: " + str(self.node_list))
    def node_message(self, connected_node, data):
        if "register" in data:
            node = {
                "host": data["host"],
                "port": data["port"],
            }
            self.node_list.append(node)
            print("node_list: " + str(self.node_list))   
        if "init" in data['message']:
            for peer in self.node_list:
                self.send_to_nodes({"message": peer, "peers": 1})
        if "peers" in data:
            # add peer to
            self.node_list.append(data['message'])
            print("New node_list: " + str(self.node_list))
            #print(str(self.node_list))
        if "msg" in data:
            print("Node" + connected_node.id + "Said : " + str(data['msg']))



    def node_disconnect_with_outbound_node(self, connected_node):
        print("node wants to disconnect with oher outbound node: " + connected_node.id)
        
    def node_request_to_stop(self):
        print("node is requested to stop!")


    class MyOwnPeer2PeerNode (Node):
        # Python class constructor
        def __init__(self, host, port, id=None, callback=None, max_connections=0):
            super(MyOwnPeer2PeerNode, self).__init__(host, port, id, callback, max_connections)

        # Override event functions...

        # Override this method to initiate your own NodeConnection class.
        def create_new_connection(self, connection, id, host, port):
            return MyOwnNodeConnection(self, connection, id, host, port)






