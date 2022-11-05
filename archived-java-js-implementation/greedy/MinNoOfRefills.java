import java.io.*;

class MinNoOfRefills
{
 public static void main(String ar[]) throws IOException{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb=new StringBuilder();
		int x[]=new int[]{0,1,3,5,9,14,17};
		System.out.println(noOfRefills(x,x.length,5));
		
		
		
	}
	
	public static int noOfRefills(int x[],int n,int l){
	        
	        int noOfRefill=0,currentRefill=0;
	        while(currentRefill<n-1){ 
	            int lastRefill=currentRefill;
	           
	            while(currentRefill<n-1 && x[currentRefill+1]-x[lastRefill]<=l){
	                currentRefill++;
	            } 
	            if(currentRefill==lastRefill)
	                return -1;
	            else 
	                noOfRefill++;
	        }
	        return noOfRefill;
	    
	}
}
