package algorithms;

public class QuickSort {
	public static void main(String ar[]){
		int a[]=new int[]{2,5,3,28,17,13,1,21,19,26,16,30,0};
		quickSort(a,0,12);
		for(int q=0;q<a.length;q++)
			System.out.print(a[q]+" ");
		
	}
	
	public static void quickSort(int a[],int p,int r){
		if(p<r){
			int q=partition(a,p,r);
			quickSort(a,p,q-1);
			quickSort(a,q+1,r);
		}
	}
	public static int partition(int a[],int p,int r){ 
		int pivot=a[r];
		int i=p-1,j=p;
		while(j<=r-1){ 
			if(a[j]<=pivot){
				i=i+1;
				int temp=a[i];		//Swapping 
				a[i]=a[j];	
				a[j]=temp;
			}
			
			j++;
		}
		int temp=a[i+1];			//putting the pivot in right position
		a[i+1]=pivot;
		a[r]=temp;
		
		return i+1;
	}
}
