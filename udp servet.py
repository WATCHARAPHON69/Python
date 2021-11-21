import socket 
def mainRun () : 
	host="127.0.0.1" 
	port=5000 
	server=socket.socket (socket.AF_INET,socket.SOCK_DGRAM) 
	server.bind ( (host, port)) 
	print ("Start Server") 
	while True: 
		data, addr=server.recv (1024) 
		data=data. decode ('utf-8') 
		print ("Message From Client :"+data)
		data=data.upper () 
		print ("Convert string :"+data) 
		server.sendto (data.encode ('utf-8'), addr) 
	server.close () 
if __name__=="__main__":
	mainRun()