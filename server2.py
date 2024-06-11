import socket

count = 0
fileno = 0

while(count <=1):

    if __name__ == '__main__':
        host = '0.0..0.0'
        port = 8082
        totalclient = 1
        counter = 0

    #netstat -ano|findstr 8082
    #taskkill /F /PID 19088


        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen(totalclient)

        connections = []
        print("Initializing clients")
        for i in range(totalclient):
            conn = sock.accept()
            connections.append(conn)
            print("connected with client", i + 1)

        
        idx = 0
   
        for conn in connections: 
            #receiving File Data 
            idx += 1 #1024\
            print()
            data = conn[0].recv(1024).decode()
            filename, data = data.split("::", 1)
           # data, file_type = data.split(";;", 1)
          #  print(filename, "\n", data, "\n", file_type)
            if not data: 
                continue

        #creating a new file at server end and writing the data 
            filename = filename+ ".py" #file_type
            fileno = fileno+1
            fo = open(filename, "w") 
            while data: 
                if not data: 
                    break
                else: 
                    fo.write(data) 
                    #fo.read()
                    data = conn[0].recv(1024).decode()
                    #break
            #break
       
            print() 
            print('Receiving file from client', idx) 
            print() 
            print('Received successfully! New filename is:', filename) 
            fo.close() 

    #closing all Connections 
 #   for conn in connections: 
    #    conn[0].close()
