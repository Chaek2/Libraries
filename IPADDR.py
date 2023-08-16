import os

"""
@ipconfig/all | find "Subnet Mask"
@ipconfig/all | find "IPv4" 
@ipconfig/all | find "Default Gateway"
@ipconfig/all | find "Host Name"
@ipconfig/all | find "DNS Suffix Search List"
@ipconfig/all | find "Physical Address"
@ipconfig/all | find "DHCP Enabled"
@ipconfig/all | find "DHCP Server"
"""

class IP(object):
    def __init__(self):
        self.ipv4=[]
        self.ipv6=[]
        self.IPv4()
        self.IPv6()
        
    def IPv4(self):
        for i in os.popen('@ipconfig/all | find "IPv4"').readlines():
            self.ipv4.append(i[39:].replace('(Ћб­®ў­®©)','').replace(' \n',''))
        return self.ipv4

    def IPv6(self):
        for i in os.popen('@ipconfig/all | find "IPv6"').readlines():
            self.ipv6.append(i[39:].replace('(Ћб­®ў­®©)','').replace(' \n',''))
        return self.ipv6
    