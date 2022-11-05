package datastructure;

public class Stack {
	private char stackArray[];
	private int maxSize;
	private int top;
	
	public Stack(int size){
		this.top=-1;
		this.maxSize=size;
		this.stackArray=new char[maxSize];
	}
	public void push(char item){
		if(isFull()){
			System.out.println("Stack overflow");
		}
		else{
			top++;
			stackArray[top]=item;
		}
		
	}
	public char pop(){
		
		if(isEmpty()){
			System.out.println("Stack Underflow");
			return 'E';
		}
		else{
			int oldTop=top;
			top--;
			return stackArray[oldTop];
		}
		
	}
	public boolean isEmpty(){
		return (top==-1);
	}
	public boolean isFull(){
		return (top==maxSize-1);
	}
}
