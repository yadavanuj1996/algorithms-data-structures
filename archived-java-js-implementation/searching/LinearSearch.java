package algorithms;

public class LinearSearch {
	public static void main(String ar[]){
		int a[]=new int[]{2,6,7,66,678,99,200};
		System.out.println(LinearSearch(a,200)); 
	}
	public static int LinearSearch(int a[],int x){
		int index=-1;
		for(int i=0;i<a.length;i++){
			if(a[i]==x){
				index=i;
				break;
			}
		}
		
		return index;
	}
}
