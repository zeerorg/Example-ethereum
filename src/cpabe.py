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
    subprocess.call(shlex.split("./cpabe-setup --output-public-key ./key/pub_key --output-master-key ./key/master_key"))

#cpabe-keygen:: sara_priv_key will be generated
# command_line = input()
def gen_priv_key(name):
    command_line = "./cpabe-keygen -o ./key/{}_priv_key ./key/pub_key ./key/master_key".format(name)
    args = shlex.split(command_line)
    print(args)
    #tmp=subprocess.call(['./cpabe-keygen', '-o', 'sara_priv_key', 'pub_key', 'master_key', 1, 1, 1])
    subprocess.run(args, stdout=subprocess.PIPE, input=b"business_staff strategy_team 'executive_level = 7' 'office = 2362' 'hire_date = '`date +%s`")

#cpabe-enc :: encrypted security_report.pdf.cpabe is generated
# command_line1 = input()
def encrypt_report(file_name):
    command_line = "./cpabe-enc -k ./key/pub_key ./{}".format(file_name)
    args1 = shlex.split(command_line)
    print(args1)
    #tmp=subprocess.call(['cpabe-enc' 'pub_key' 'security_report.pdf' 1 1 1])
    
    subprocess.run(args1, stdout=subprocess.PIPE, input=b"(sysadmin and (hire_date < 946702800 or security_team)) or (business_staff and 2 of (executive_level >= 5, audit_group, strategy_team))")

#cpabe-dec:: security_report.pdf will be generated on successful decryption
def dec_file(filename, user):
    command_line2 = "./cpabe-dec -k -o {} ./key/pub_key ./key/{}_priv_key  {}.cpabe".format(filename, user, filename)
    args2 = shlex.split(command_line2)
    print(args2)
    #tmp=subprocess.call(['cpabe-dec'  'pub_key' 'sara_priv_key' 'security_report.pdf.cpabe'])
    subprocess.run(args2, stdout=subprocess.PIPE)
