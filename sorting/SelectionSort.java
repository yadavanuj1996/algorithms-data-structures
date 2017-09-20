package algorithms;

public class SelectionSort {

	public static void main(String ar[]){
		int a[]=new int[]{2,5,3,28,17,13,1,21,19,26,16,30};
		selectionSort(a);
		for(int i=0;i<a.length;i++)
			System.out.print(a[i]+" ");
	}
	
	public static int[] selectionSort(int a[]){
		
		for(int i=0;i<a.length-1;i++){
			int smallIndex=i;
			for(int j=i+1;j<a.length;j++){
				if(a[j]<a[smallIndex])
					smallIndex=j;
			}
			int temp=a[i];
			a[i]=a[smallIndex];
			a[smallIndex]=temp;
		}
		
		return a;
	}
}
