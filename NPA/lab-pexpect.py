import pexpect

ip_pool = {
    "R01" : "172.16.112.3",
    "R02" : "172.16.112.4",
}

def test(IP_POOL):
    for key in IP_POOL.keys():
        print(key)
        print(IP_POOL["R01"])

'''TELNET OPEN CONNECTIONS'''
def telnet_openConnections(USERNAME, PASSWORD, PROMPT, CHILD) :
    #username
    CHILD.expect("Username")
    CHILD.sendline(USERNAME)
    #password
    CHILD.expect("Password")
    CHILD.sendline(PASSWORD)
    print('Connections_Opened')

''' TELNET CLOSE CONNECTIONS'''
def telnet_closeConnections(CHILD) :
    CHILD.sendline("exit")
    CHILD.close()
    print("Connections_closed")

'''GET IP INT BR CAMMAND'''
def get_ip_info(PROMPT, CHILD) :
    #sending command
    CHILD.expect(PROMPT)
    CHILD.sendline('sh ip int bri')
    
    #write result
    CHILD.expect(PROMPT)
    result = CHILD.before
    print(result)
    print(type(result))
    print()
    print(result.decode("UTF-8"))
    
'''SET-UP IP ADDRESS'''
def setup_ip(PROMPT, IP_POOL, CHILD):
    #open config plain
    CHILD.expect(PROMPT)
    CHILD.sendline('config t')
    
    #open interfaces plain
    CHILD.expect(PROMPT)
    CHILD.sendline('int g0/2')
    
    #setting ip address int g0/1
    CHILD.expect(PROMPT)
    CHILD.sendline('ip address 192.168.2.1 255.255.255.0')
    CHILD.expect(PROMPT)
    CHILD.sendline('no shut')
    CHILD.expect(PROMPT)
    CHILD.sendline('end')

def loopback_create(PROMPT, IP_POOL, CHILD):
    #open config plain
    CHILD.expect(PROMPT)
    CHILD.sendline('config t')
    
    #open interfaces plain
    CHILD.expect(PROMPT)
    CHILD.sendline('int loopback 0')
    
    #setting ip address int g0/1
    CHILD.expect(PROMPT)
    CHILD.sendline('ip address 172.16.2.2 255.255.255.255')
    CHILD.expect(PROMPT)
    CHILD.sendline('no shut')
    CHILD.expect(PROMPT)
    CHILD.sendline('end')
    
def main() :
    PROMPT = "#"
    PROMPT_CONF = "(config)#"
    PROMPT_INT = "(config-if)#"
    IP = "172.31.112.4"
    USERNAME = "admin"
    PASSWORD = "cisco"
    CHILD = pexpect.spawn("telnet " + IP, timeout=100)
    
    telnet_openConnections(USERNAME, PASSWORD, PROMPT, CHILD)
    loopback_create(PROMPT, 0, CHILD)
    get_ip_info(PROMPT, CHILD)
    telnet_closeConnections(CHILD)
    
test(ip_pool)

