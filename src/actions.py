#!/usr/bin/env python3
import socket
import threading
import queue
import serial
import parse
from time import sleep


class PortException(BaseException):
    pass


class Actions(threading.Thread):
    def __init__(self, input_queue: queue.Queue, port, baudrate):
        self.queue = input_queue
        self.interrupt = False
        try:
            self.serial = serial.Serial(
                port=port,
                baudrate=baudrate,
                bytesize=serial.SEVENBITS,
                parity=serial.PARITY_EVEN,
                stopbits=serial.STOPBITS_TWO,
                timeout=None,
                xonxoff=False,
                dsrdtr=False,
                rtscts=False
            )
            if self.serial.isOpen():
                while self.serial.in_waiting == 0:
                    print('Waiting')
                    sleep(0.5)
                print('Connected')
                self.serial.write('%\n'.encode('UTF-8'))
                self.serial.write('G17G40G49G91G53\n'.encode('UTF-8'))
                threading.Thread.__init__(self, name="XHC_Action")
        except serial.SerialException as ex:
            print(ex)
            exit(-1)

    def start(self) -> None:
        threading.Thread.start(self)

    def run(self):
        while not self.interrupt:
            try:
                action = str(self.queue.get(block=True, timeout=1))
                buf = self.serial.in_waiting
                self.serial.flushInput()
                if buf == 0:
                    print('Buffer full, command discarded')
                else:
                    if action.startswith('mpg'):
                        filename = 'mpg'
                    else:
                        filename = action
                    with open('nc_commands/' + filename + '.nc', 'r') as command:
                        content = command.read()
                        if filename == 'mpg':
                            t = parse.parse('mpg({},{})', action)
                            content = content.format(t[0], t[1])
                        print('Sending command \'{}\''.format(content))
                        content_bytes = content.encode("UTF-8")
                        self.serial.write(content_bytes)
                        print('Done')
            except queue.Empty:
                pass

    def quit(self):
        self.serial.write('%'.encode('UTF-8'))
        self.interrupt = True


if __name__ == "__main__":
    srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        srv.bind(('localhost', 61111))  # Allocate random port
    except socket.error as e:
        print("Socket bind failed with error code {0}: {0}".format(e.errno, e.getMessage()))
    print(srv.getsockname())
    try:
        while True:
            data, addr = srv.recvfrom(1024)
            if not data:
                continue
            print("From {0}: {1}".format(addr, data))

    except KeyboardInterrupt:
        pass
    srv.close()
    print('')
    exit(0)
