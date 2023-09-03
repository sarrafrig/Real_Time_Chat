import network
import usocket as socket

Host = "localhost"  # Server IP address
Port = 8765

def main():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect("your_wifi_ssid", "your_wifi_password")

    while not wifi.isconnected():
        pass

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((Host, Port))

    username = input("Enter your username: ")
    soc.send(username.encode())

    while True:
        message = input("Enter a message: ")
        soc.send(message.encode())

        server_message = soc.recv(1024)
        print("Received from server:", server_message.decode("utf-8"))


    soc.close()

if __name__ == "__main__":
    main()