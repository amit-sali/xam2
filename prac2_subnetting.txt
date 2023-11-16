class temp:
    def __init__(self, ip_address):
        self.ipaddress = ip_address
        self.octet1=0
        self.octet2=0

    def ip_decimal_to_binary(self):
        binary_parts = []
        int_parts=[]
        for part in self.ipaddress.split('.'):
            int_parts.append(int(part))
        for part in self.ipaddress.split('.'):
            binary_parts.append(format(int(part), '08b'))
        self.octet1=int_parts[0]
        self.ip1=int_parts[0]
        self.ip2=int_parts[1]
        self.ip3=int_parts[2]
        self.octet4=binary_parts[3]
        return '.'.join(binary_parts)

    def subnetgen(self,reserved_bits):
        octet_new=""
        for i in range(8) :
            if(i<(8 - int(reserved_bits))) :
                octet_new+="1"
            else :
                octet_new+="0"
        print("Subnet generator : ",2**(int(reserved_bits)))
        return(2**(int(reserved_bits)))

    def netrange(self,lim,ip1,ip2,ip3) :
        print("the range of subnets are : ")
        for i in range(lim,256,lim) :
            print(ip1,".",ip2,".",ip3,".",i-lim," to ",ip1,".",ip2,".",ip3,".",i-1)
        print(ip1,".",ip2,".",ip3,".",i," to ",ip1,".",ip2,".",ip3,".",255)
            
def classfinder(octet1):
    if octet1 >= 0 and octet1 <= 127:
        print("IP belong to class A")
        return '255.0.0.0'
    elif octet1 >= 128 and octet1 <= 191:
        print("IP belong to class B")
        return '255.255.0.0'
    elif octet1 >= 192 and octet1 <= 223:
        print("IP belong to class C")
        return '255.255.255.0'
    elif octet1 >= 224 and octet1 <= 239:
        print("IP belong to class D")
        return '255.255.255.255'
    elif octet1 >= 240 and octet1 <= 255:
        print("IP belong to class E")
        return '255.255.255.255'
    else:
        return 'Invalid IP address'

def main():
    ip_address = input("Enter IP address (format: xxx.xxx.xxx.xxx): ")
    a = temp(ip_address)
    no_host = int(input("Enter number of hosts: "))
    no_host_len = len(bin(no_host)) - 2
    binary_no_host = format(no_host, 'b')  
    binary_ip = a.ip_decimal_to_binary()
    print("IP in binary:", binary_ip)
    print("Number of hosts in binary:", binary_no_host)  
    default_subnet = classfinder(int(a.octet1))
    print("Default subnet  : ", default_subnet)
    print("Length of hosts in binary : ", no_host_len)
    octet_4 = no_host_len
    l = a.subnetgen(octet_4)
    ip1 = a.ip1
    ip2 = a.ip2
    ip3 = a.ip3
    a.netrange(l, ip1, ip2, ip3)

if __name__ == "__main__":
    main()

