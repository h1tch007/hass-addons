import socket
import yaml
import json
from time import sleep
import paho.mqtt.client as mqtt
import logging

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    mqtt_config = config.get("mqtt")
    log_config = config.get("logging")
    doors = config.get("doors")

def publish_discovery(client, door_id):
    discovery_topic = f"homeassistant/lock/{door_id}/config"
    discovery_payload = {
        "device": {
            "name": f"ЭНТ Эра-500",
            "manufacturer": "Эра Новых Технологий",
            "model": "ЭНТ",
            "model_id": "Эра-500",
            "sw_version": "0.24",
            "connections": [["ip", "10.113.0.100"]]
        },
        "name": f"Lock {door_id}",
        "unique_id": f"era_{door_id}",
        "command_topic": f"homeassistant/lock/{door_id}/set",
        "command_template": '{ "action": "{{ value }}", "code": "{{ code }}" }',
        "state_topic": f"homeassistant/lock/{door_id}/state",
        "state_locked": "LOCK",
        "state_unlocked": "UNLOCK",
        "payload_open": "OPEN",
        "code_format": "^\\d{4}$",
    }

    client.publish(discovery_topic, json.dumps(discovery_payload), retain=True)
    logger.debug(f"MQTT auto discovery payload sent for door {door_id}")

def on_connect(client, userdata, flags, rc, properties):
    logger.debug("Connected to MQTT Broker with result code "+str(rc))
    client.subscribe(mqtt_config['MQTT_TOPIC'])
    
    # Publish MQTT auto-discovery messages for each lock
    for door_id in doors:
        publish_discovery(client, door_id)

def on_message(client, userdata, msg):
    message = json.loads(msg.payload.decode())
    room = int(msg.topic.split("/")[2])
    action = message.get("action")
    code = message.get("code")
    delay = int(message.get("delay", 3))

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    if room not in doors:
        logger.error(f"Room '{room}' is not present in config.yaml")
        return

    if action == 'UNLOCK' and code == mqtt_config['LOCK_CODE']:
        sock.sendto(bytes.fromhex(doors[room]['disable_packet']), (doors[room]['host'], 7715))
        client.publish(f"homeassistant/lock/{room}/state", "UNLOCK")
        logger.info(f"Lock {room} unlocked.")
    elif action == 'LOCK' and code == mqtt_config['LOCK_CODE']:
        sock.sendto(bytes.fromhex(doors[room]['enable_packet']), (doors[room]['host'], 7715))
        client.publish(f"homeassistant/lock/{room}/state", "LOCK")
        logger.info(f"Lock {room} locked")
    elif action == 'OPEN' and code == mqtt_config['LOCK_CODE']:
        sock.sendto(bytes.fromhex(doors[room]['disable_packet']), (doors[room]['host'], 7715))
        client.publish(f"homeassistant/lock/{room}/state", "UNLOCK") # Понять почему не работает задержка
        logger.info(f"Lock {room} unlocking...")
        sleep(delay) 
        sock.sendto(bytes.fromhex(doors[room]['enable_packet']), (doors[room]['host'], 7715))
        client.publish(f"homeassistant/lock/{room}/state", "LOCK")
        logger.info(f"Lock {room} locked")
    else: 
        logger.error("Password is incorrrect.")

logger = logging.getLogger(__name__)
logging.basicConfig(encoding='utf-8', level=getattr(logging, log_config.get("level")))

# MQTT client setup
MQTT_BROKER="$(bashio::services mqtt 'host')"
MQTT_PORT="$(bashio::services mqtt 'port')"
MQTT_USERNAME="$(bashio::services mqtt 'username')"
MQTT_PASSWORD="$(bashio::services mqtt 'password')"
#client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, password=MQTT_PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
logger.debug("Connecting to MQTT Broker...")
client.loop_forever()