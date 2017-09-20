package datastructure;

public class StackImplementation {
	public static void main(String ar[]){
	
		
		StackImplementation s=new StackImplementation();
		s.reverseString("Hello");
	}
	public void numberStack(){
		/*Stack newStack=new Stack(10);
		newStack.push(20);
		newStack.push(40);
		newStack.push(60);
		newStack.push(80);
		while(!newStack.isEmpty())
			System.out.println(newStack.pop());
		
		*/
	}
	public void reverseString(String str){
		int sizeString=str.length();
		Stack newStack=new Stack(sizeString);
		for(int i=0;i<sizeString;i++)
			newStack.push(str.charAt(i));
		
		while(!newStack.isEmpty())
			System.out.print(newStack.pop());
	}
	
}
