import subprocess
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
import getpass
import json


#Tables: 
table_name = ('TBPA_VALID_PARTNER_GROUPINGS', 'TBGG_SEG_VALUE_TRANSLATIONS')


# Function to run Hadoop command

def run_unix_cmd(args_list):
    print('Running system command:{0}'.format('     '.join(args_list)))
    proc = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess .PIPE, universal_newlines=True)
    s_output, s_err = proc.communicate()
    s_return = proc.returncode
    return s_return, s_output, s_err

# Create Sqoop Job
def sqoop_job(table_name):
    cmd = ['sqoop', 'import', '--connect', 'jdbc:oracle:thin:@sl09.atradiusnet.com:1519/SYMF.atradiusnet.com', '--username', 'NLSMAY1','--password', 'Winter18','--table', 'ORABUP0.'+table_name, '-m', '1', '--hive-import', '--hive-table', 'D_NATIVE_ZONE.'+table_name]
    print(cmd)
    (ret, out, err) = run_unix_cmd(cmd)
    print(ret, out, err)
    if ret == 0:
        logging.info('Success.')
    else:
        logging.info('Error.')

##if __name__ == '__main__':
  ##  for k, values in table_name.items:
    ##    sqoop_job(table_name)

for i in table_name:
    sqoop_job(i)