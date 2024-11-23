from flask import render_template
from . import device_bp

@device_bp.route('/')
def list_devices():
    devices = [
        {'id': 1, 'name': 'Device A', 'type': 'Sensor'},
        {'id': 2, 'name': 'Device B', 'type': 'Camera'}
    ]
    return render_template('device/list.html', devices=devices)


@device_bp.route('/<int:device_id>')
def device_detail(device_id):
    device = {'id': device_id, 'name': f'Device {device_id}', 'type': 'Unknown'}
    return render_template('device/detail.html', device=device)