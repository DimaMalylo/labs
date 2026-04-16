import asyncio
import json
import random

# --- 1. REST Client (імітація) ---
class RestClient:
    def __init__(self):
        pass

    def get(self, endpoint):
        # Імітуємо REST API відповіді
        data = [
            {"id": 1, "title": "Тестове повідомлення 1", "body": "Дані для інтеграції"},
            {"id": 2, "title": "Тестове повідомлення 2", "body": "Дані для інтеграції"},
            {"id": 3, "title": "Тестове повідомлення 3", "body": "Дані для інтеграції"},
        ]
        print(f"REST GET {endpoint} -> {len(data)} записів")
        return data

# --- 2. WebSocket Client (імітація) ---
class WebSocketClient:
    def __init__(self):
        self.queue = asyncio.Queue()
        self.connected = False

    async def connect(self, url):
        await asyncio.sleep(0.1)
        self.connected = True
        print(f"WebSocket підключено до {url}")

    async def send_message(self, message):
        if self.connected:
            print(f"WebSocket надіслано: {message}")
            await self.queue.put(message)

    async def receive_message(self):
        if self.connected:
            msg = await self.queue.get()
            print(f"WebSocket отримано: {msg}")
            return msg

    async def close_connection(self):
        self.connected = False
        print("WebSocket з'єднання закрито")

# --- 3. MQTT Client (імітація) ---
class MQTTClient:
    def __init__(self):
        self.queue = asyncio.Queue()
        self.connected = False

    async def connect(self, broker="fake-mqtt-broker"):
        await asyncio.sleep(0.1)
        self.connected = True
        print(f"MQTT підключено до {broker}")

    async def publish(self, topic, message):
        if self.connected:
            await asyncio.sleep(0.1)
            print(f"MQTT надіслано на {topic}: {message}")
            await self.queue.put((topic, message))

    async def disconnect(self):
        self.connected = False
        print("MQTT з'єднання закрито")

# --- 4. Інтеграція ---
async def main():
    # REST
    rest = RestClient()
    data = rest.get("/posts")

    # WebSocket
    ws = WebSocketClient()
    await ws.connect("ws://fake-websocket.local")

    # MQTT
    mqtt_client = MQTTClient()
    await mqtt_client.connect()

    topic = "home/test"

    # Відправка даних через WebSocket та MQTT
    for item in data:
        message = json.dumps(item)

        # WebSocket
        await ws.send_message(message)
        await ws.receive_message()

        # MQTT
        await mqtt_client.publish(topic, message)

    # Закриття з'єднань
    await ws.close_connection()
    await mqtt_client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
    