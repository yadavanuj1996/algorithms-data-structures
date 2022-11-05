package algorithms;

public class MergeSort {
	public static void main(String ar[]){
		int a[]=new int[]{2,5,3,28,17,13,1,21,19,26,16,30,0};
		mergeSort(a,0,12);
		for(int qa=0;qa<a.length;qa++)
			System.out.print(a[qa]+" ");
		
		System.out.println();
	}
	// p is for starting index q is for middle element and r is for last index
	public static void mergeSort(int a[],int p,int r){
		
		if(p<r){
			int q=(p+r)/2;
			mergeSort(a,p,q);
			mergeSort(a,q+1,r);
			merge(a,p,q,r);
			
			
		}	
		
		 
	}
	public static void merge(int a[],int p,int q,int r){	
		
		int leftArray[]=new int[q-p+2];
		int rightArray[]=new int[r-q+1];
		
		for(int i=0;i<q-p+1;i++){
			leftArray[i]=a[i+p];
		}
		leftArray[q-p+1]=2147483647;		// this is the largest value that int can support in java as in a[length+1]->infinite in pseudocode
		for(int j=0;j<r-q;j++){ 
			rightArray[j]=a[q+1+j];
			
		}
		rightArray[r-q]=2147483647;		// this is the largest value that int can support in java as in a[length+1]->infinite in pseudocode
		
		int i=0,j=0;
		for(int k=p;k<=r;k++){ 
			if(leftArray[i]<rightArray[j]){ 
				a[k]=leftArray[i];
				i++;
			}
			else if(leftArray[i]>rightArray[j]){
				a[k]=rightArray[j];
				j++;
			}
			
				
			
		}
		
	}
}
