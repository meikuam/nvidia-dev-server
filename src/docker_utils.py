import os
import time
import subprocess
import logging
import json
import pandas as pd
from io import StringIO


def check_password(password: str) -> bool:
    if len(password) > 0:
        SpecialSym = ['$', '@', '#', '%', '\r', '\n', '\'', '"']
        if any(char in SpecialSym for char in password):
            return False
        return True
    else:
        return False


def get_absolute_path(path):
    """get absolute path and create it if not exists"""
    if not os.path.isabs(path):
        path = os.path.normpath(os.path.join(os.getcwd(), path))
    check_path = path
    dir_names = []
    while not os.path.exists(check_path):
        dir_names.append(os.path.basename(check_path))
        check_path = os.path.dirname(check_path)
    dir_names.reverse()
    for dir_name in dir_names:
        check_path = os.path.join(check_path, dir_name)
        os.mkdir(check_path)
    return path


def get_container_info(
        container_name: str,
        info=[
            'status',
            'name',
            'runtime',
            'visible_devices',
            'ports',
            'mounts',
            'binds'
        ]
):
    container_info = {}

    query = 'docker inspect ' + container_name
    container_str = os.popen(query).read().strip()
    container_dict = json.loads(container_str)[0]

    state = container_dict.get('State', {})
    host_config = container_dict.get('HostConfig', {})
    config = container_dict.get('Config', {})

    if 'status' in info:
        status = state.get('Status', 'N/A')
        container_info['status'] = status

    if 'name' in info:
        container_info['name'] = container_dict.get('Name', 'N/A')

    if 'runtime' in info:
        container_info['runtime'] = host_config.get('Runtime', 'N/A')

    if 'visible_devices' in info:
        try:
            visible_devices = [x for x in config.get("Env", []) if "NVIDIA_VISIBLE_DEVICES" in x]
            if len(visible_devices) > 0:
                visible_devices = visible_devices[0].split('=')[-1]
            else:
                visible_devices = 'N/A'
            container_info['visible_devices'] = visible_devices
        except Exception as e:
            logging.info('get_container_info container: ' + container_name + ' e: ' + str(e))

    if 'ports' in info:
        try:
            query = 'docker port ' + container_name
            status = os.popen(query).read().strip()
            ports = []
            for line in status.splitlines():
                container_port, host_port = line.split('->')
                host_port = host_port.split('/')[0]
                container_port = container_port.split(":")[-1]
                ports.append([host_port, container_port])
            container_info['ports'] = ports
            # ports_dict = config.get('ExposedPorts', {})
            # ports = []
            # for key, value in ports_dict.items():
            #     container_port = key.split('/')[0]
            #     host_ip = value.get('HostIp', 'N/A')
            #     host_port = value.get('HostPort', container_port)
            #     ports.append([host_port, container_port])
            # container_info['ports'] = ports
        except Exception as e:
            logging.info('get_container_info container: ' + container_name + ' e: ' + str(e))
    if 'mounts' in info:
        try:
            mounts_dict = container_dict.get('Mounts', [])
            mounts = []
            for mount_data in mounts_dict:
                source_path = mount_data.get('Source', 'N/A')
                dist_path = mount_data.get('Destination', 'N/A')
                mounts.append([source_path, dist_path])
            container_info['mounts'] = mounts
        except Exception as e:
            logging.info('get_container_info container: ' + container_name + ' e: ' + str(e))
    if 'binds' in info:
        try:
            binds_dict = host_config.get('Binds', [])
            if binds_dict is not None:
                binds = [x.split(':') for x in binds_dict]
            else:
                binds = []
            container_info['binds'] = binds

        except Exception as e:
            logging.info('get_container_info container: ' + container_name + ' e: ' + str(e))


    return container_info


def get_info(status=None):
    query = 'docker ps -a --format "{{.Names}}"'
    names = os.popen(query).read().strip().splitlines()
    containers_info = []
    for name in names:
        container_info = get_container_info(
            container_name=name,
            info=[
                'name',
                'status',
                'runtime',
                'visible_devices',
                'ports',
                'mounts',
                'binds'
            ]
        )
        if status is None or status == container_info['status']:
            containers_info.append(container_info)
    return containers_info


def show_ports(container_name: str):
    query = 'docker port ' + container_name
    status = os.popen(query).read().strip()
    ports = []
    for line in status.splitlines():
        container_port, host_port  = line.split('->')
        host_port = host_port.split('/')[0]
        container_port = container_port.split(":")[-1]
        ports.append([host_port, container_port])
    ports_df = pd.DataFrame(ports, columns=['host', 'container'])
    print(ports_df)
    logging.info('show_ports query: ' + query + ' status: ' + str(ports_df))
    return ports


def check_running(container_name: str) -> bool:
    query = 'docker ps -f name=' + container_name + ' | tail -1 | grep ' + container_name
    logging.info('check_running query: ' + query)
    status = os.popen(query).read().strip()
    logging.info('check_running container: ' + container_name + ' status: ' + str(status))
    return status


def check_exsists(container_name: str) -> bool:
    query = 'docker ps -f name=' + container_name + ' -a | tail -1 | grep ' + container_name
    logging.info('check_exsists query: ' + query)
    status = os.popen(query).read().strip()
    logging.info('check_exsists container: ' + container_name + ' status: ' + str(status))
    return status

def check_image_exsists(image_name: str, image_version: str) -> bool:
    query = 'docker images -f "reference=' + image_name + ':' + image_version + '"'
    query += '| tail -1 | grep ' + image_name
    logging.info('check_image_exsists query: ' + query)
    status = os.popen(query).read().strip()
    logging.info(
        'check_image_exsists image_name: ' +
        image_name + 'image_version: ' +
        image_version + ' status: ' + str(status)
    )
    return status


def start_container(container_name: str) -> bool:
    logging.info('start_container container: ' + container_name)
    subprocess.call('docker start ' + container_name, shell=True)
    return True


def build_container(image_name: str, image_version: str, username: str, password: str, ports: str) -> bool:
    query = 'docker build -t ' + image_name + ':' + image_version + \
            ' docker/dev --build-arg UID=$(id -u $(whoami))' + \
            ' --build-arg USER=' + username + \
            ' --build-arg PASSWORD=' + password
    if ports is not None:
        query += ' --build-arg PORTS="' + ports + '"'

    logging.info('build_container query: ' + query)
    subprocess.call(query, shell=True)
    logging.info('build_container statue: ' + str(True))
    return True


def run_container(
        container_name: str,
        image_name: str,
        image_version: str,
        project_root: str,
        project_root_internal: str,
        project_data_root: str,
        ssh_port, host_ports, ports,
        visible_devices: str
) -> bool:
    query = 'docker run --restart=always -it -d ' + \
            ' -P --name=' + container_name + \
            ' -v ' + project_root + ':' + project_root_internal + \
            ' -v ' + project_data_root + ':' + os.path.join(project_root_internal, 'data')
            # ' --mount type=bind,source=' + project_root + ',target=' + project_root_internal + ',bind-propagation=shared' + \
            # ' --mount type=bind,source=' + project_data_root + ',target=' + os.path.join(project_root_internal, 'data') + ',bind-propagation=shared'
    if visible_devices is not None:
        query += ' --runtime=nvidia  -e NVIDIA_VISIBLE_DEVICES=' + visible_devices
    if ssh_port is not None:
        query += ' -p ' + ssh_port + ':22'
    if ports is not None:
        for host_port, port in zip(host_ports.split(' '), ports.split(' ')):
            query += ' -p ' + host_port + ':' + port

    query += ' ' + image_name + ':' + image_version + ' bash'

    logging.info('run_container query: ' + query)
    subprocess.call(query, shell=True)
    return True


def start_ssh(container_name: str, username: str, host='0.0.0.0'):
    subprocess.call('docker exec --user root ' + container_name + ' service ssh start', shell=True)
    # subprocess.call('scp ~/.ssh/id_rsa.pub -p ' + ssh_port + ' ' + username + '@' + host + ':/home/', shell=True)
    # subprocess.call('ssh -p ' + ssh_port + ' ' + username + '@' + host +
    #                 'cat id_rsa.pub >> .ssh/authorized_keys && rm id_rsa.pub', shell=True)

    ssh_port_host = os.popen("docker port " + container_name + " 22").read().split(':')[-1].strip()
    query = 'ssh ' + username + '@' + host + ' -p ' + ssh_port_host
    logging.info('start_ssh query: ' + query)
    print('start_ssh: ', query)
    os.system(query)


def start_jupyter(container_name: str):
    print('start jupyter')
    # subprocess.call('docker exec --user ' + username + ' ' + container_name +
    #                 ' jupyter notebook --ip=0.0.0.0 --port ' + jupyter_port +
    #                 ' --no-browser > /dev/null 2>&1 &',
    #                 shell=True)
    #
    # time.sleep(5)
    # jupyter_token = os.popen("docker exec " + container_name + " jupyter notebook list").read()
    # print(jupyter_token)
    # jupyter_token = jupyter_token.split('::')[0].strip().split('?token=')[-1]
    #
    # jupyter_link = 'http://' + host + ':' + container_name + '/tree?token=' + jupyter_token
    # print('jupyter link: ', jupyter_link)
    # os.system('xdg-open ' + jupyter_link)

