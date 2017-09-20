package algorithms;

public class RecursiveBinarySearch {

	public static void main(String ar[]){
		int a[]=new int[]{23,45,67,87,91,97,98,102,113};
		System.out.println(recursiveBinarySearch(a,102,0,a.length-1));
	}
	
	public static int recursiveBinarySearch(int a[],int x,int firstIndex,int lastIndex){
		int middleIndex=(firstIndex+lastIndex)/2;
		
		if(a[middleIndex]==x)
			return middleIndex;
		else if(firstIndex>lastIndex)
			return -1;
		else if(a[middleIndex]>x)
			return recursiveBinarySearch(a,x,firstIndex,middleIndex-1);
		else 
			return recursiveBinarySearch(a,x,middleIndex+1,lastIndex);
	}
}
