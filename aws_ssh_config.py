import boto.ec2
import time
from boto.exception import BotoServerError

###############################################################################
def generate_ssh_config():
    client = boto.ec2.connect_to_region(REGION)
    reservations = client.get_all_reservations()
    instances = []
    for reservation in reservations:
        instances.append(reservation.instances[0])
    get_instance_ip_dict(instances)

###############################################################################
def get_instance_ip_dict(instances):
    config_file = open('config_ssh', 'w')
    config_file.truncate()
    for i in instances:
        #pip =  i.private_ip_address
        #iid =  i.id
        tag = ""
        if 'Name' in i.tags:
            tag = i.tags['Name']

        config_file.write('Host '+str(tag))
        config_file.write("\n")
        config_file.write('\t HostName '+ str(i.private_ip_address))
        config_file.write("\n")
        config_file.write("\t port 22")
        config_file.write("\n\n")
    print "config_ssh file generated"
    config_file.close()

REGION = 'us-east-1'
generate_ssh_config()
###############################################################################
