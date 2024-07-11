from pypresence import Presence
import time
import psutil

client_id = "00000000000"
RPC = Presence(client_id)
RPC.connect()

start_time = time.time()

while True:
    elapsed_time = int(time.time() - start_time)
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    time_str = f"{hours:02}:{minutes:02}:{seconds:02}"

    (RPC.update(
        state="Status", 
        large_image="1", 
        large_text="Large Text", 
        start=start_time,
        buttons=[{"label": "Button1", "url": "https://example.com/"}] 
    ))

    if not 'csgo.exe' in (p.name() for p in psutil.process_iter()):
        RPC.close()
        break

    time.sleep(15)