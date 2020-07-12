import os
import socket

def ping_one(ip):
    """
    ping单个ip地址，打印出有效的ip地址
    """
    try:
        code =  os.popen('ping %s' % ip).read()

        if '100% 丢失' in code:
            return False
        else:
            return True

    except Exception as e:
       print(e)
  

def tcp_one(ip_port):
    """
    用socket连接ip地址及端口，参数ip_port_tuple 为一个元祖
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to remote host
    try:
        s.connect((ip_port,))
        success_ports.append(ip_port)  
            
    except Exception as e:
        print('Error:', e)
    finally:
        s.close()
