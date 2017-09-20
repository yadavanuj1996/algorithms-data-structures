package algorithms;

public class InsertionSort {
	public static void main(String ar[]){
	int a[]=new int[]{2,5,3,28,17,13,1,21,19,26,16,30};
		
	insertionSort(a);
	for(int i=0;i<a.length;i++)
		System.out.print(a[i]+" ");
	
	}
	public static int[] insertionSort(int a[]){
		
		for(int i=1;i<a.length;i++){
			int presentVal=a[i];
			int j=i-1;
			while(j>=0 && presentVal<a[j]){
				a[j+1]=a[j];
				j--;
			}
			a[j+1]=presentVal;
		}
		
		return a;
	}
}
