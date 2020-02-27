import logging
from flask import Flask, request, g, render_template
from flask_restplus import Api, Resource, fields
from src.nvidia_utils import get_current
from src.docker_utils import get_info

# import uwsgi

logging.basicConfig(
    filename='server_log.log',
    format="%(asctime)-15s %(message)s'",
    level=logging.INFO
)

flask_app = Flask(__name__)

app = Api(app=flask_app,
          version="1.0",
          title="nvidia-dev-docker",
          doc='/api/doc/',
          prefix='/api',
          description="API for nvidia dev docker")


device_params_model = app.model(
    'device_params',
    {
        'name': fields.String(),
        'temp': fields.Integer(),
        'utilization': fields.String(),
        'free': fields.Integer(),
        'used': fields.Integer(),
        'total': fields.Integer()
    }
)
device_list_model = app.model(
    'device list',
    {
        'devices': fields.List(fields.Nested(device_params_model))
    }
)

device_status_namespace = app.namespace('device_status', description='Get status of devices')


@device_status_namespace.route("/")
class DeviceClass(Resource):

    @device_status_namespace.doc(responses={200: 'Status OK', 503: 'Error'})
    @device_status_namespace.marshal_with(device_list_model)
    def get(self):
        current_data = get_current()
        if current_data is not None:
            return {'devices': current_data.to_dict(orient='records')}
        else:
            return {503}


container_model = app.model(
    'container_params',
    {
        'name': fields.String(),
        'status': fields.String(),
        'runtime': fields.String(),
        'visible_devices': fields.String(),
        'ports': fields.List(
            fields.List(
                fields.String()
            )
        ),
        'mounts': fields.List(
            fields.List(
                fields.String()
            )
        ),
        'binds': fields.List(
            fields.List(
                fields.String()
            )
        ),
    }
)
container_list_model = app.model(
    'container list',
    {
        'containers': fields.List(fields.Nested(container_model))
    }
)

container_namespace = app.namespace('containers', description='Containers')


@container_namespace.route("/")
class ContainerClass(Resource):

    @container_namespace.doc(responses={200: 'status of containers', 503: 'Error'})
    @container_namespace.marshal_with(container_list_model)
    def get(self):
        container_data = get_info(status='running')
        if container_data is not None:
            return {'containers': container_data}
        else:
            return {503}


@flask_app.route("/")
@flask_app.route("/index")
def index(name=None):
    return render_template('index.html', name=name)


if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port=5000, debug=True)
