// Sum of product of numbers

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class SumOfProductOfNumbers
{
	public static void main (String[] args) throws IOException
	{
		// your code goes here
	    StringBuilder sb = new StringBuilder();
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		String x[] = br.readLine().split(" ");
		int a[] = Arrays.stream(x).mapToInt(Integer::parseInt).toArray(); 
	    int sumOfNo=0, sumOfSquaresOfNo=0;
	    for(int i=0;i<a.length;i++){
	        sumOfNo+=a[i];
	        sumOfSquaresOfNo+=(int)Math.pow(a[i],2);
	    }
	
	    System.out.println(((int)Math.pow(sumOfNo,2)-sumOfSquaresOfNo)/2);
	}
}
