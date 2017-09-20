package algorithms;

public class BinarySearch {
								
	public static void main(String ar[]){
		int a[]=new int[]{2,4,6,7,16,28,93,107,118,928,1000};
		int x=107;
		
		System.out.println(binarySearch(a,x));
	}
	
	
	
	//Note : For BS we need to have an sorted array
	
	public static int binarySearch(int a[],int x){
		int index=-1;			//If the element is not found method will return -1			
		int firstIndex=0;
		int lastIndex=a.length-1;
		
		while(firstIndex<=lastIndex){		
			//As we are changing the value of firstindex and lastindex on basis of that the required 
			//search number x is smaller or larger so if the element will not occur than after several
			//iterations the firstindex will become greater than lastindex
											
			int middleIndex=(firstIndex+lastIndex)/2;			//The middleIndex is the integer value of the sum of index of first and last element
			
			if(a[middleIndex]== x){
				index=middleIndex;
				break;
			}
			else if(a[middleIndex]< x){
				firstIndex=middleIndex+1;
			}
			else if(a[middleIndex]> x){
				lastIndex=middleIndex-1;
			}
			
		}
		return index;
	}
}
