# nvidia-dev-server


## dev:


Создание контейнера (на удаленной машине):
```
python3 run_dev.py --username krang --password pass --project_name project --project_root home/krang --project_data_root data --visible_devices 0 --ssh_port 8022 --ports "8000 8001 8002"
```

Запуск сервера
```bash
python3 run_server.py
```
Или
```bash
./run_server.sh
```

