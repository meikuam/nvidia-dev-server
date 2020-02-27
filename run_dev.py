import os
import time
import argparse
import logging
from src.docker_utils import *


if __name__ == "__main__":
    logging.basicConfig(
        filename='errors.log',
        format="%(asctime)-15s %(message)s'",
        level=logging.INFO
    )
    # setup environment
    parser = argparse.ArgumentParser(description='Create container tool')
    parser.add_argument('--username', action='store', help='username', required=True)
    parser.add_argument('--password', action='store', default='password', help='password', required=True)
    parser.add_argument('--project_name', action='store', default='project', help='project_name', required=True)
    parser.add_argument('--project_root', action='store', default='home/krang', help='absolute path to home directory of project', required=False)
    parser.add_argument('--project_data_root', action='store', default='data', help='absoulte path to data directory of project', required=False)
    parser.add_argument('--ssh_port', action='store', default=None, help='ssh port', required=False)
    parser.add_argument('--ports', action='store', default=None, help='ports for container (same ports for host and container)', required=False)
    parser.add_argument('--visible_devices', action='store', default=None, help='visible nvidia devices', required=False)
    parser.add_argument('--instance', action='store', default=0, type=int, help='instance of project', required=False)

    args = parser.parse_args()


    host = '0.0.0.0'
    username = args.username
    password = args.password.strip()
    if not check_password(password):
        print('not valid password')

    project_name = args.project_name
    image_version = 'dev'

    project_root = get_absolute_path(args.project_root)
    project_data_root = get_absolute_path(args.project_data_root)
    ssh_port = args.ssh_port
    ports = args.ports
    visible_devices = args.visible_devices
    instance = str(args.instance)

    project_root_internal = os.path.join('/home/', username)
    # create image name
    image_name = project_name + '-' + username
    # create container name
    container_name = image_name
    if visible_devices is not None:
        container_name += '-devs-' + visible_devices
    container_name += '-instance-' + str(instance)

    # print arguments

    print('container_name: ', container_name)
    print('image_name: ', image_name)

    print('username: ', username)
    print('password: ', password)
    print('project_name: ', project_name)
    print('project_root: ', project_root)
    print('project_data_root: ', project_data_root)
    print('ssh_port: ', ssh_port)
    print('ports: ', ports)
    print('visible_devices: ', visible_devices)
    print('instance: ', instance)


    if check_running(container_name):
        print('docker container: already running')
    elif check_exsists(container_name):
        print('docker container: * exists *')
        start_container(container_name)
        print('docker container: now running')
    else:
        print('docker container: * not exists *')
        build_container(
            image_name=image_name,
            image_version=image_version,
            username=username,
            password=password,
            ports=ports
        )
        if check_image_exsists(image_name=image_name, image_version=image_version):
            print('docker container: built')
            run_container(
                container_name=container_name,
                image_name=image_name,
                image_version=image_version,
                project_root=project_root,
                project_root_internal=project_root_internal,
                project_data_root=project_data_root,
                ssh_port=ssh_port,
                host_ports=ports, ports=ports,
                visible_devices=visible_devices
            )
            if check_running(container_name):
                print('docker container: now running')
                print('docker container: show ports')
                show_ports(container_name)
            else:
                print('docker container: error while running, abort')
                exit(0)
        else:
            print('docker container: error while building, abort')
            exit(0)

    print('start ssh service')
    start_ssh(
        container_name=container_name,
        username=username,
        host=host
    )
