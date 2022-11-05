package algorithms;

public class RecursiveLinearSearch {
	
	public static void main(String ar[]){
		int a[]=new int[]{2,4,6,7,16,28,93,107,118,928,1200};
		int x=1200;
		
		System.out.println(recursiveLinearSearch(a,x,0));
	}
	
	public static int recursiveLinearSearch(int a[],int x,int i){
		
		
		if(a[i]==x)
			return i;
		else if((a.length-1)==i)
			return -1;
		else 
			return recursiveLinearSearch(a,x,i+1);
	}
}
