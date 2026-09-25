import asyncio
import json
from aiohttp import web

# --- 1. ASYNC RECEIVER (Background Server) ---
async def receive_json(request):
    try:
        data = await request.json()
    except json.JSONDecodeError:
        return web.json_response({"status": "error", "message": "Invalid JSON"}, status=400)
    
    # Save the incoming file locally
    filename = f"incoming_{data.get('sender_id', 'unknown')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
        
    print(f"\n[Received] New data saved to {filename}!")
    return web.json_response({"status": "success"})

async def start_server():
    # Set up the server application and routes
    app = web.Application()
    app.router.add_post('/receive-json', receive_json)
    
    # Run the server on port 5000
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 5000)
    await site.start()
    print("Local async server running on port 5000.")

# --- 2. ASYNC SENDER ---
async def send_json(target_ngrok_url, local_filename, my_id):
    try:
        with open(local_filename, "r") as f:
            payload = json.load(f)
    except FileNotFoundError:
        payload = {"message": "Test payload data"}
        
    payload["sender_id"] = my_id
    url = f"{target_ngrok_url.rstrip('/')}/receive-json"
    
    # Use aiohttp to send the file asynchronously
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                print(f"[Sent] Status Code: {response.status}")
    except Exception as e:
        print(f"[Error] Could not send data: {e}")

# --- 3. MAIN ASYNC LOOP ---
async def main():
    # Start the background server task
    await start_server()
    print("1. Run 'ngrok http 5000' in your terminal.")
    print("2. Share your Ngrok URL with your partner.")
    
    my_name = input("\nEnter your name identifier: ")
    partner_url = input("Enter your partner's Ngrok URL: ")
    
    print("\nReady! Type 'send' to transmit data, or 'exit' to quit.")
    
    # Read user input without blocking the entire async event loop
    loop = asyncio.get_event_loop()
    while True:
        # Fast non-blocking wrapper for standard input
        cmd = await loop.run_in_executor(None, input, "\n> ")
        cmd = cmd.strip().lower()
        
        if cmd == 'send':
            # Schedule the send task to run concurrently
            asyncio.create_task(send_json(partner_url, "my_data.json", my_name))
        elif cmd == 'exit':
            print("Exiting...")
            break

if __name__ == '__main__':
    # Start the asyncio event loop
    asyncio.run(main())
