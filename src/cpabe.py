import subprocess
import shlex

def init_module(_w3, _contract):
    global w3, contract_instance
    w3 = _w3
    contract_instance = _contract

'''
functionality required : 
1. Encrypt and Upload document to ethereum blockchain
2. Download the encrypted document
3. Download any requested attribute key
4. Take a requester public key and attributes,
     and upload their attribute key to blockchain after encrypting it with their public key
'''
#initial cpabe_setup:: pub_key and master_key is generated
subprocess.call("./cpabe-setup")

#cpabe-keygen:: sara_priv_key will be generated
command_line = input()
args = shlex.split(command_line)
print(args)
#tmp=subprocess.call(['./cpabe-keygen', '-o', 'sara_priv_key', 'pub_key', 'master_key', 1, 1, 1])
subprocess.Popen(args)

#cpabe-enc :: encrypted security_report.pdf.cpabe is generated
command_line1 = input()
args1 = shlex.split(command_line1)
print(args1)
#tmp=subprocess.call(['cpabe-enc' 'pub_key' 'security_report.pdf' 1 1 1])
subprocess.Popen(args1)

#cpabe-dec:: security_report.pdf will be generated on successful decryption 
command_line2 = input()
args2 = shlex.split(command_line2)
print(args2)
#tmp=subprocess.call(['cpabe-dec'  'pub_key' 'sara_priv_key' 'master_key' 'security_report.pdf.cpabe'])
subprocess.Popen(args2)

