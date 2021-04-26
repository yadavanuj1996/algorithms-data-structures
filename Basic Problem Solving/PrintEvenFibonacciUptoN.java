// Print even fibonacci numbers upto n 

import java.util.*;
import java.lang.*;
import java.io.*;

class PrintEvenFibonacciUptoN
{
	public static void main (String[] args) throws IOException
	{
		// your code goes here
	    StringBuilder sb = new StringBuilder();
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int a = 0;
		int b = 2;
		sb.append(a+" "+b+" ");
	    while(true){
	            int c=4*b+a;
	            if(c<=n){
	                sb.append(c+" ");    
	                a=b;
	                b=c;
	            }
	            else{
	                break;
	            }
	      
	        
	    }
	    System.out.println(sb);
	}
}
