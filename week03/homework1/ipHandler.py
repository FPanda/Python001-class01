from IPy import IP

def convertIpRangeToIpList(ip_start, ip_end):
    start_ip = IP(ip_start)
    end_ip = IP(ip_end)

    ip_list = list()

    int_start_ip = start_ip.int()
    int_end_ip = end_ip.int()

    for i in range (int_start_ip, int_end_ip+1):
        ip_list.append(IP(i).strNormal(0))

    print(ip_list)
    return ip_list
