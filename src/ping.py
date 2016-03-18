#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
# Stdlib imports

# Core Django imports

# Third-party app imports

# Imports from your apps
ip_list = ["10.74.82.1",
           "10.74.82.2",
           "10.74.82.3",
           "10.74.82.4",
           "10.74.82.5",
           "10.74.82.6",
           "10.74.82.7",
           "192.168.1.1",
           "10.74.82.8",
           "10.74.82.9",
           "10.74.82.10",
           "10.74.82.11",
           "10.74.82.12",
           "10.74.82.13",
           "10.74.82.14",
           "10.74.82.15",
           "10.74.82.16",
           "10.74.82.17",
           "192.168.1.134",
           "10.74.82.18",
           "10.74.82.19",
           "10.74.82.20",
           "10.74.82.21",
           "10.74.82.22",
           "10.74.82.23",
           "10.74.82.24",
           "10.74.82.25",
           "10.74.82.26",
           "10.74.82.27",
           "10.74.82.28",
           "10.74.82.29",
           "10.74.82.30",
           "10.74.82.31",
           "10.74.82.32",
           "10.74.82.33",
           "10.74.82.34",
           "10.74.82.35",
           "10.74.82.36",
           "10.74.82.37",
           "10.74.82.38",
           "10.74.82.39",
           "10.74.82.40",
           "10.74.82.41",
           "10.74.82.42",
           "10.74.82.43",
           "10.74.82.44",
           "10.74.82.45",
           "10.74.82.46",
           "10.74.82.47",
           "10.74.82.48",
           "10.74.82.49",
           "10.74.82.50",
           "10.74.82.51",
           "192.168.1.235",
           "10.74.82.52",
           "10.74.82.53",
           "10.74.82.54",
           "10.74.82.55",
           "10.74.82.56",
           "10.74.82.57",
           "10.74.82.58",
           "10.74.82.59",
           "10.74.82.60",
           "10.74.82.61",
           "10.74.82.62",
           "10.74.82.63",
           "10.74.82.64",
           "10.74.82.65",
           "10.74.82.66",
           "10.74.82.67",
           "10.74.82.68",
           "10.74.82.69",
           "10.74.82.70",
           "10.74.82.71",
           "10.74.82.72",
           "10.74.82.73",
           "10.74.82.74",
           "10.74.82.75",
           "10.74.82.76",
           "10.74.82.77",
           "10.74.82.78",
           "10.74.82.79",
           "10.74.82.80",
           "10.74.82.81",
           "10.74.82.82",
           "10.74.82.83",
           "10.74.82.84",
           "10.74.82.85",
           "10.74.82.86",
           "10.74.82.87",
           "10.74.82.88",
           "10.74.82.89",
           "10.74.82.90",
           "10.74.82.91",
           "10.74.82.92",
           "10.74.82.93",
           "10.74.82.94",
           "10.74.82.95",
           "10.74.82.96",
           "10.74.82.97",
           "10.74.82.98",
           "10.74.82.99",
           "10.74.82.100",
           "10.74.82.101",
           "10.74.82.102",
           "10.74.82.119",
           "10.74.82.120",
           "10.74.82.147",
           "10.74.82.148",
           "10.74.82.238",
           "10.74.82.239",
           "10.74.82.240",
           "10.74.82.241",
           "10.74.82.242",
           "10.74.82.243",
           "10.74.82.244",
           "10.74.82.245",
           "10.74.82.246",
           "10.74.82.247",
           "10.74.82.248",
           "10.74.82.249",
           "10.74.82.250",
           "10.74.82.251",
           "10.74.82.252",
           "10.74.82.253",
           "10.74.82.254",
           ]

import os
import struct
import array
import time
import socket
import threading
import argparse
import concurrent.futures
import os, sys, socket, struct, select, time, signal

if sys.platform == "win32":
    default_timer = time.clock
else:
    default_timer = time.time

NUM_PACKETS = 3
PACKET_SIZE = 64
WAIT_TIMEOUT = 3.0

ICMP_ECHOREPLY = 0  # Echo reply (per RFC792)
ICMP_ECHO = 8  # Echo request (per RFC792)
ICMP_MAX_RECV = 2048  # Max size of incoming buffer

MAX_SLEEP = 1000

try:
    from thread import get_ident
except ImportError:
    try:
        from _thread import get_ident
    except ImportError:
        def get_ident():
            return 0


class Ping(object):
    def __init__(self, my_socket, destination_ip, timeout=500):
        self.my_socket = my_socket
        self.destination_ip = destination_ip
        self.my_id = (get_ident() ^ os.getpid()) & 0xFFFF
        # self.my_id = os.getpid() & 0xFFFF
        self.my_sequence_number = 0
        self.packet_size = 64
        self.timeout = timeout

    def ping_once(self):
        delay = None
        sentTime = self.send_one_ping()

        if sentTime == None:
            return delay

        recvTime, dataSize, iphSrcIP, icmpSeqNumber, iphTTL = self.receive_one_ping()

        if recvTime:
            delay = (recvTime - sentTime) * 1000
        else:
            delay = None
        print("IP: %s === ID: %s   ==  Delay:%s" % (self.destination_ip, str(self.my_id), str(delay)))
        return delay

    def send_one_ping(self):
        # Header is type (8), code (8), checksum (16), id (16), sequence (16)
        # (packet_size - 8) - Remove header size from packet size
        myChecksum = 0

        # Make a dummy heder with a 0 checksum.
        header = struct.pack(
            "!BBHHH", ICMP_ECHO, 0, myChecksum, self.my_id, self.my_sequence_number
        )

        padBytes = []
        startVal = 0x42
        # 'cose of the string/byte changes in python 2/3 we have
        # to build the data differnely for different version
        # or it will make packets with unexpected size.
        if sys.version[:1] == '2':
            bytes = struct.calcsize("d")
            data = ((self.packet_size - 8) - bytes) * "Q"
            data = struct.pack("d", default_timer()) + data
        else:
            for i in range(startVal, startVal + (self.packet_size - 8)):
                padBytes += [(i & 0xff)]  # Keep chars in the 0-255 range
            # data = bytes(padBytes)
            data = bytearray(padBytes)

        # Calculate the checksum on the data and the dummy header.
        myChecksum = self.checksum(header + data)  # Checksum is in network order

        # Now that we have the right checksum, we put that in. It's just easier
        # to make up a new header than to stuff it into the dummy.
        header = struct.pack(
            "!BBHHH", ICMP_ECHO, 0, myChecksum, self.my_id, self.my_sequence_number
        )

        packet = header + data

        sendTime = default_timer()

        try:
            self.my_socket.sendto(packet, (self.destination_ip, 1))  # Port number is irrelevant for ICMP
        except socket.error as e:
            print("General failure (%s)" % (e.args[1]))
            return
        return sendTime

    def receive_one_ping(self):
        """
        Receive the ping from the socket. Timeout = in ms
        """
        timeLeft = self.timeout / 1000

        while True:  # Loop while waiting for packet or timeout
            startedSelect = default_timer()
            whatReady = select.select([self.my_socket], [], [], timeLeft)
            howLongInSelect = (default_timer() - startedSelect)
            if whatReady[0] == []:  # Timeout
                return None, 0, 0, 0, 0

            timeReceived = default_timer()

            recPacket, addr = self.my_socket.recvfrom(ICMP_MAX_RECV)

            ipHeader = recPacket[:20]
            iphVersion, iphTypeOfSvc, iphLength, \
            iphID, iphFlags, iphTTL, iphProtocol, \
            iphChecksum, iphSrcIP, iphDestIP = struct.unpack(
                "!BBHHHBBHII", ipHeader
            )

            icmpHeader = recPacket[20:28]
            icmpType, icmpCode, icmpChecksum, \
            icmpPacketID, icmpSeqNumber = struct.unpack(
                "!BBHHH", icmpHeader
            )

            if icmpPacketID == self.my_id:  # Our packet
                dataSize = len(recPacket) - 28
                return timeReceived, (dataSize + 8), iphSrcIP, icmpSeqNumber, iphTTL

            timeLeft = timeLeft - howLongInSelect
            if timeLeft <= 0:
                return None, 0, 0, 0, 0

    @staticmethod
    def checksum(source_string):
        countTo = (int(len(source_string) / 2)) * 2
        sum = 0
        count = 0
        loByte = 0
        hiByte = 0
        while count < countTo:
            if (sys.byteorder == "little"):
                loByte = source_string[count]
                hiByte = source_string[count + 1]
            else:
                loByte = source_string[count + 1]
                hiByte = source_string[count]
            try:  # For Python3
                sum = sum + (hiByte * 256 + loByte)
            except:  # For Python2
                sum = sum + (ord(hiByte) * 256 + ord(loByte))
            count += 2

        # Handle last byte if applicable (odd-number of bytes)
        # Endianness should be irrelevant in this case
        if countTo < len(source_string):  # Check for odd length
            loByte = source_string[len(source_string) - 1]
            try:  # For Python3
                sum += loByte
            except:  # For Python2
                sum += ord(loByte)

        sum &= 0xffffffff  # Truncate sum to 32 bits (a variance from ping.c, which
        # uses signed ints, but overflow is unlikely in ping)

        sum = (sum >> 16) + (sum & 0xffff)  # Add high 16 bits to low 16 bits
        sum += (sum >> 16)  # Add carry from above (if any)
        answer = ~sum & 0xffff  # Invert and truncate to 16 bits
        answer = socket.htons(answer)

        return answer


def ping_once(aa, destination_ip):
    ping = Ping(my_socket=aa, destination_ip=destination_ip)
    ping.ping_once()


class SendPingThr(threading.Thread):
    '''
    发送ICMP请求报文的线程。

    参数：
        ipPool      -- 可迭代的IP地址池
        icmpPacket  -- 构造的icmp报文
        icmpSocket  -- icmp套字接
        timeout     -- 设置发送超时
    '''

    def __init__(self, ipPool, Socket):
        threading.Thread.__init__(self)
        self.Socket = Socket
        self.ipPool = ipPool

    def run(self):
        time.sleep(0.01)  # 等待接收线程启动
        for ip in self.ipPool:
            try:
                ping = Ping(my_socket=self.Socket, destination_ip=ip)
                ping.ping_once()
            except socket.timeout:
                break


if __name__ == '__main__':
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    scaned_host_list = []
    # sendThr = SendPingThr(ip_list, my_socket)
    # sendThr.start()

    # for ip in ip_list:
    #     ping_once(my_socket, ip)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
    # executor = concurrent.futures.ProcessPoolExecutor(max_workers=5)

    futures = [executor.submit(ping_once, my_socket, ip) for ip in ip_list]
    #
    for future in concurrent.futures.as_completed(futures, timeout=120):
        scaned_host_list.append(future.result())
    executor.shutdown()
    my_socket.close()
