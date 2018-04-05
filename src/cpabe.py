import subprocess
import shlex
import os
'''
functionality required : 
1. generate a new key in "./key" directory and encrypt document using that key
2. generate a new key for the access control
3. decrypt using the given key
'''
#initial cpabe_setup:: pub_key and master_key is generated
def gen_pair():
    if not os.path.exists("./key"):
        subprocess.call(["mkdir", "./key"])
    subprocess.call(shlex.split("cpabe-setup --output-public-key ./key/pub_key --output-master-key ./key/master_key"))

#cpabe-keygen:: sara_priv_key will be generated
# command_line = input()
def gen_priv_key(name):
    command_line = "cpabe-keygen -o ./key/{}_priv_key ./key/pub_key ./key/master_key 1 1 1".format(name)
    args = shlex.split(command_line)
    print(args)
    #tmp=subprocess.call(['./cpabe-keygen', '-o', 'sara_priv_key', 'pub_key', 'master_key', 1, 1, 1])
    subprocess.Popen(args)

#cpabe-enc :: encrypted security_report.pdf.cpabe is generated
# command_line1 = input()
def encrypt_report(file_name):
    command_line = "cpabe-enc ./key/pub_key ./{} 1 1 1".format(file_name)
    args1 = shlex.split(command_line1)
    print(args1)
    #tmp=subprocess.call(['cpabe-enc' 'pub_key' 'security_report.pdf' 1 1 1])
    subprocess.Popen(args1)

#cpabe-dec:: security_report.pdf will be generated on successful decryption
def dec_file(filename, user):
    command_line2 = "cpabe-dec ./key/pub_key ./key/{}_priv_key  {}.cpabe".format(user, filename)
    args2 = shlex.split(command_line2)
    print(args2)
    #tmp=subprocess.call(['cpabe-dec'  'pub_key' 'sara_priv_key' 'security_report.pdf.cpabe'])
    subprocess.Popen(args2)