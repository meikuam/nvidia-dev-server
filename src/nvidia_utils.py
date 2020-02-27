import os
import pandas as pd
import logging
from io import StringIO
from openssh_wrapper import SSHConnection


def get_current(conn=None):
    """gets current data from nvidia-smi tool"""
    get_current_data = 'nvidia-smi --query-gpu=gpu_name,temperature.gpu,utilization.gpu,memory.free,memory.used,memory.total --format=csv,nounits,noheader'
    try:
        if conn is None:
            ret = os.popen(get_current_data).read()
        else:
            ret = conn.run(get_current_data)
        ret = str(ret)
        return pd.read_csv(StringIO(ret), header=None, names=['name', 'temp', 'utilization', 'free', 'used', 'total'])
    except Exception as e:
        logging.info('get_current container: e: ' + str(e))
        return None
