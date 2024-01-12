import pexpect

PROMPT = "#"
IP = "172.31.112.3"
USERNAME = "admin"
PASSWORD = "cisco"
COMMAND = "sh ip int bri"


child = pexpect.spawn("telnet " + IP, timeout=100)
child.expect("Username")
child.sendline(USERNAME)
child.expect("Password")
child.sendline(PASSWORD)
child.expect(PROMPT)
child.sendline(COMMAND)
child.expect(PROMPT)
result = child.before
print(result)
print(type(result))
print()
print(result.decode("UTF-8"))
child.sendline("exit")
child.close()

# def connect(host_add, username, password) :
#     child = pexpect.spawn(f'telnet {host_add}')
#     print('telnet successful')
    
#     child.expect('Username: ')
#     child.sendline(username)
#     print('username filled')
    
#     child.expect('Password: ')
#     child.sendline(password)
#     print('password filled')
    
#     child.sendline('show ip int br')
#     print('show ip int br')

#     # Wait for the command to complete and print the output
#     child.expect('\r\n')
#     print(child.before.decode('utf-8'))
    
#     # Close the Telnet session
#     child.sendline('exit')
#     child.expect(pexpect.EOF)

# connect('172.31.112.1', 'admin', 'cisco')