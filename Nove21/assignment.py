import socket                                                                  
                                                                                 
                                                                                 
  def check_port(host, port):                                                    
      try:                                                                       
         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:           
              s.settimeout(1)                                                                      
            s.connect((host, port))                                            
         print(f"Port {port} is open")                                          
      except socket.error:                                                       
         print(f"Port {port} is closed")                                        
                                                                                 
                                                                                 
  target_host = "127.0.0.1"                                                      
  target_port = 65432                                                            
                                                                                 
  check_port(target_host, target_port)
