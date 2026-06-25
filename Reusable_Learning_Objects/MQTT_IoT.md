Unit Context
Networking and Cyber Program — Murdoch University
Repository: SCH-IT-MurdochUni/NetworkingLabs
Lab stream: IoT / Reusable Learning Objects

1. Aim
In this lab, you will integrate MQTT into a smart-lighting IoT workflow.
You will subscribe to sensor/environment data from a public MQTT broker hosted in Australia, apply decision logic, and control a lab light (or simulated LED) automatically.

2. Learning Outcomes
By the end of this lab, you should be able to:

Describe MQTT publish/subscribe messaging and broker role.
Connect an IoT client to a public MQTT broker.
Subscribe to and parse JSON payloads.
Implement threshold-based automation logic.
Control a physical/simulated actuator from MQTT data.
Publish system state back to MQTT topics.
Implement basic reliability controls (reconnect, Last Will, hysteresis).
3. Prerequisites
Basic Python programming.
Introductory understanding of IP networking and ports.
Prior lab experience toggling a lab light/LED from code.
4. Equipment / Software
Raspberry Pi / lab PC / VM (Linux preferred; Windows/macOS acceptable).
Python 3.10+.
MQTT library: paho-mqtt.
Optional MQTT client tool:
MQTT Explorer or
Mosquitto CLI (mosquitto_sub, mosquitto_pub)
Hardware output:
Preferred: LED + resistor (simulation mode), or
Approved GPIO relay module for controlled lab light circuit.
5. Safety Notice
Do not connect mains voltage directly to GPIO.

If using real lighting circuits, only use approved relay modules and instructor-approved wiring.
For first run and assessment demos, LED simulation is recommended.

6. Lab Topology and Topic Plan
6.1 Logical flow
A publisher sends sensor data (lux) to a topic on an AU public broker.
Your controller subscribes to the topic.
Your code decides whether the light should be ON/OFF.
Your controller actuates output and publishes state telemetry.
6.2 Topic namespace (example)
Sensor input: mu/networking/iotlab1/environment/lightlevel
Light command (optional extension): mu/networking/iotlab1/lab01/light/cmd
Light state output: mu/networking/iotlab1/lab01/light/state
Instructor may provide a cohort-specific prefix, e.g. mu/2026/s1/<group-id>/...

6.3 Payload format (sensor feed)
{
  "timestamp": "2026-06-25T10:15:00+08:00",
  "source": "au-public-feed",
  "lux": 245
}
7. Pre-Lab Tasks
Install dependencies:
pip install paho-mqtt
Confirm you can reach broker host and port (1883 or instructor-specified TLS port).
Use MQTT Explorer or mosquitto_sub to verify you can see test messages.
Record in notebook:
Broker hostname
Port
Topic(s)
Whether authentication is required
8. Procedure
Task 1 — Verify subscription to broker
Use one of the following:

Option A: Mosquitto CLI

mosquitto_sub -h <BROKER_HOST> -p 1883 -t mu/networking/iotlab1/environment/lightlevel -v
Option B: MQTT Explorer

Add broker connection.
Subscribe to sensor topic.
Observe payload updates.
✅ Checkpoint 1: Show live payloads to demonstrator.

Task 2 — Build MQTT subscriber controller in Python
Create smart_light_mqtt.py and start from the scaffold below.

import json
import time
import paho.mqtt.client as mqtt

BROKER = "REPLACE_WITH_AU_BROKER"
PORT = 1883
TOPIC_SUB = "mu/networking/iotlab1/environment/lightlevel"
TOPIC_STATE = "mu/networking/iotlab1/lab01/light/state"

THRESHOLD_LUX = 300
HYSTERESIS = 20  # to avoid flicker
light_on = False

def set_light(state: bool):
    global light_on
    # TODO: replace with GPIO control if using hardware
    light_on = state
    print(f"[ACTUATOR] LIGHT {'ON' if state else 'OFF'}")

def evaluate_light_state(lux: float, current_state: bool) -> bool:
    # Hysteresis band:
    # turn ON below (THRESHOLD_LUX - HYSTERESIS)
    # turn OFF above (THRESHOLD_LUX + HYSTERESIS)
    on_point = THRESHOLD_LUX - HYSTERESIS
    off_point = THRESHOLD_LUX + HYSTERESIS

    if current_state:
        # currently ON; only turn off if clearly bright
        return False if lux > off_point else True
    else:
        # currently OFF; only turn on if clearly dark
        return True if lux < on_point else False

def publish_state(client, lux):
    payload = json.dumps({
        "ts": time.time(),
        "light": "ON" if light_on else "OFF",
        "lux": lux
    })
    client.publish(TOPIC_STATE, payload, qos=1, retain=False)

def on_connect(client, userdata, flags, rc, properties=None):
    print("[MQTT] Connected with rc =", rc)
    client.subscribe(TOPIC_SUB, qos=0)

def on_message(client, userdata, msg):
    global light_on
    try:
        data = json.loads(msg.payload.decode("utf-8"))
        lux = data.get("lux", None)
        if lux is None:
            print("[WARN] No 'lux' field in payload")
            return

        desired_state = evaluate_light_state(float(lux), light_on)
        if desired_state != light_on:
            set_light(desired_state)

        publish_state(client, lux)
        print(f"[DATA] lux={lux}, light={'ON' if light_on else 'OFF'}")

    except json.JSONDecodeError:
        print("[ERROR] Invalid JSON payload")
    except Exception as e:
        print("[ERROR]", e)

def main():
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.on_message = on_message

    # Last Will (published if client disconnects ungracefully)
    client.will_set(
        TOPIC_STATE,
        payload='{"status":"offline","light":"UNKNOWN"}',
        qos=1,
        retain=False
    )

    client.connect(BROKER, PORT, keepalive=60)
    client.loop_forever()

if __name__ == "__main__":
    main()
Run:

python smart_light_mqtt.py
✅ Checkpoint 2: Demonstrate automatic ON/OFF changes based on incoming lux values.

Task 3 — Publish test data (if no live feed is available)
Create mqtt_lux_publisher.py:

import json
import random
import time
import paho.mqtt.client as mqtt

BROKER = "REPLACE_WITH_AU_BROKER"
PORT = 1883
TOPIC = "mu/networking/iotlab1/environment/lightlevel"

client = mqtt.Client(protocol=mqtt.MQTTv311)
client.connect(BROKER, PORT, keepalive=60)
client.loop_start()

try:
    while True:
        lux = random.randint(100, 600)
        payload = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "source": "lab-simulator",
            "lux": lux
        }
        client.publish(TOPIC, json.dumps(payload), qos=0, retain=False)
        print("Published:", payload)
        time.sleep(2)
except KeyboardInterrupt:
    pass
finally:
    client.loop_stop()
    client.disconnect()
✅ Checkpoint 3: Show your subscriber reacts correctly to your own test publisher.

Task 4 — Observe and validate state topic
Subscribe to your state topic:

mosquitto_sub -h <BROKER_HOST> -p 1883 -t mu/networking/iotlab1/lab01/light/state -v
Verify:

State message appears after each sensor message.
light field matches actual LED/light behavior.
Offline will message appears if subscriber is killed ungracefully.
✅ Checkpoint 4: Demonstrate state telemetry and will behavior.

9. Deliverables
Submit:

smart_light_mqtt.py
(Optional) mqtt_lux_publisher.py
Short report (1–2 pages) containing:
Broker/topic details used
Decision rule and threshold values
Evidence (screenshots/logs) of ON/OFF behavior
Reliability features implemented
Reflection: challenges and improvements
10. Assessment Rubric (20 marks)
Criterion	Marks	Description
MQTT connectivity & subscription	4	Correct broker connection and topic subscription
Payload parsing & validation	4	Correct JSON handling, robust error handling
Automation logic	4	Correct threshold/hysteresis behavior
Actuation + state publish	4	Output control works and state topic is accurate
Reliability + reflection	4	Reconnect/will/hardening + clear technical reflection
11. Extension Challenges (Optional)
Add manual override via command topic (.../light/cmd with ON, OFF, AUTO).
Add time-window policy (e.g., automation only after 5:00 PM local time).
Compare QoS 0 vs QoS 1 delivery behavior under packet loss.
Add Node-RED dashboard for live visualization.
Add TLS broker connection and authenticated client configuration.
12. Troubleshooting Guide
No messages received
Check topic spelling exactly.
Confirm publisher and subscriber use same broker and port.
Check firewall/network egress rules.
JSON parse errors
Print raw payload before parsing.
Validate payload in MQTT Explorer.
Light flickers near threshold
Increase hysteresis band.
Frequent disconnects
Increase keepalive.
Implement reconnect loop / backoff.
Hardware not switching
Validate GPIO pin mapping and relay power requirements.
Test with LED simulation first.
13. Academic Integrity & Good Practice
You may discuss concepts with peers, but submitted code must be your own work unless group submission is specified.
Cite any external libraries, snippets, or AI assistance per unit policy.
Use meaningful commit messages if working in Git.
Instructor Notes (not for student submission)
Validate current AU public broker availability before class (public brokers may change/limit access).
Keep backup options:
Instructor-hosted broker in AU region.
Local broker fallback for continuity.
For large classes, allocate unique topic prefixes per group to prevent collisions.
