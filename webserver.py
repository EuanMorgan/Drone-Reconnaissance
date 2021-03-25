from http.server import HTTPServer, BaseHTTPRequestHandler
from sys import argv
import winwifi, time
BIND_HOST = 'localhost'
PORT = 8008

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    
    def do_GET(self):
        self.write_response(b'')

    def do_POST(self):
        content_length = int(self.headers.get('content-length', 0))
    
    def beep(self):
        print("\a\a\a")

    def connect_to_drone(self):
        print("[2] Trying to connect to drone...")
        winwifi.WinWiFi.connect('4DRC_4K_GPS-2ccb0fc8')
        print("[2] Connected!")
  

    def reconnect_wifi(self):
        print("[4] Reconnecting to WiFi")
        winwifi.WinWiFi.connect('TALKTALK9C1F11')
        print("[4] Done!")
        self.beep()
    
    def activate(self):
        self.beep()
        print("[!] Receieved, beginning reconnaissance...")
        
        self.beep()
        self.connect_to_drone()
        self.beep()
        print("[3] Drone scouting...")
        for i in range(1,31):
            if i % 5 == 0:
                self.beep()
            time.sleep(1)
        self.reconnect_wifi()


    def write_response(self,content):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(content)

        # print(self.headers)
        # print(content.decode('utf-8'))
        self.activate()
        

if len(argv) > 1:
    arg = argv[1].split(":")
    BIND_HOST = arg[0]
    PORT = int(arg[1])

print(f'Listening on http://{BIND_HOST}:{PORT}\n')
httpd = HTTPServer((BIND_HOST,PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()



