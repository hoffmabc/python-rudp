from packet import Packet


class PacketSender:

    def __init__(self, socket, address, port):
        print 'Init PacketSender'

        assert socket, 'No socket'
        assert address, 'No address'
        assert port, 'No port'

        self._socket = socket
        self._address = address
        self._port = port


    def send(self, packet):

        #buffer = packet.toBuffer()
        buffer = packet

        self._socket.sendto(buffer._payload, (self._address, self._port))
        # self._socket.send(buffer, 0, buffer.length, self._port, self._address)
