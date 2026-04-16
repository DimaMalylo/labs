import asyncio

class WebSocketClient:
    def __init__(self):
        self.connected = False
        self.queue = asyncio.Queue()

    async def connect(self, url):
        # Симуляція підключення
        await asyncio.sleep(0.5)
        self.connected = True
        print(f"Підключено до {url}")

    async def send_message(self, message):
        if not self.connected:
            print("Не підключено")
            return
        await asyncio.sleep(0.2)  # симуляція мережі
        print(f"Надіслано: {message}")
        await self.queue.put(message)  # "сервер" повертає повідомлення назад

    async def receive_message(self):
        if not self.connected:
            print("Не підключено")
            return
        message = await self.queue.get()
        await asyncio.sleep(0.2)  # симуляція затримки
        print(f"Отримано: {message}")
        return message

    async def close_connection(self):
        if self.connected:
            await asyncio.sleep(0.2)
            self.connected = False
            print("З'єднання закрито")
        else:
            print("З'єднання не було встановлено")


# --- Приклад використання ---
async def main():
    ws = WebSocketClient()
    await ws.connect("ws://fake-websocket.local")

    await ws.send_message("Привіт, WebSocket!")
    await ws.receive_message()

    await ws.send_message("Ще одне тестове повідомлення")
    await ws.receive_message()

    await ws.close_connection()

if __name__ == "__main__":
    asyncio.run(main())