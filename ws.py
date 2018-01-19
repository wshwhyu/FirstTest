import dpkt
import sys

f=file(r"D:\WyPcap\pcap\Capture\2017-8-21_16-56-00\P2P_AudioVideo_Client\SinaVideo_Client_1\192.168.90.187_61397-180.149.139.168_80-TCP.pcap","rb")
pcap=dpkt.pcap.Reader(f)


for ts, buf in pcap:
  eth=dpkt.ethernet.Ethernet(buf)
  ip=eth.data
  tcp=ip.data

  if tcp.dport==80 and len(tcp.data)>0:
     try:
        http=dpkt.http.Request(tcp.data)
        print http
     except:
        print 'issue'
        continue


f.close()
