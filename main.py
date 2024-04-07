import socket


server_addres = ("127.0.0.1", 2000)

def star_my_server():
    #start
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(server_addres)
        server.listen(4)
        print("Port: ", "http://1270.0.1:2000/")
        while True:
            print("Working...")
            #loading...
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode("utf-8")

            content = load_page_from_get_request(data)
            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print("Shoutdown this shit...")


def load_page_from_get_request(request_data):
    HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
    HDRS_404 = "HTTP/1.1 400 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
    path = request_data.split(" ")[1]
    response = ''
    try:
        with open('templates' + path, 'rb') as file:
            response = file.read()

        return HDRS.encode('utf-8') + response
    except Exception:
        return (HDRS_404 + "Sorry, bro! No page...").encode('utf-8')

if __name__=='__main__':
    star_my_server()