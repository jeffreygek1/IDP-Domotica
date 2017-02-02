package rpiclient;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class Client {
	
	public static void socket_Test() throws UnknownHostException, IOException, ClassNotFoundException, InterruptedException{
		Socket socket = null;
		OutputStream output_stream = null;
		PrintWriter out = null;
		final String hostName = "127.0.0.1";
		final int port = 4444;
		ObjectOutputStream oos = null;
		ObjectInputStream ois = null;
		int i =0;
		
	
		while (true){
			if(i>4)break;		
			socket = new Socket(hostName, port);
			oos = new ObjectOutputStream(socket.getOutputStream());	
			if(i==4)oos.writeObject("exit");
			
			else oos.writeObject(""+i);
			i++;
				
			ois = new ObjectInputStream(socket.getInputStream());
			String message = (String) ois.readObject();
			
			System.out.println("Message: " + message);
			  ois.close();
	          oos.close();
	          Thread.sleep(100);
		}
			
		} 
	
		
	
	
	public static void main(String[] args) throws UnknownHostException, IOException, ClassNotFoundException, InterruptedException{
		socket_Test();
		
	}

}
