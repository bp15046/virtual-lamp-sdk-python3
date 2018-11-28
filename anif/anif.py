from abc import ABCMeta, abstractmethod


class AccessNetworkInterface(metaclass=ABCMeta):
    def __init__(self, addr, port):
        self._addr = addr
        self._port = port
        self._file = None
        self._data = None
        
    def open(self, file):
        self._file = file
        self._connect()
    
    def close(self):
        self._file = None
        self._disconnect()
    
    def write(self, data):
        self._data = data
        self._send()

    def read(self):
        return self._recv()

    @abstractmethod
    def _connect(self):
        pass

    @abstractmethod
    def _disconnect(self):
        pass
    
    @abstractmethod
    def _send(self):
        pass

    @abstractmethod
    def _recv(self):
        pass