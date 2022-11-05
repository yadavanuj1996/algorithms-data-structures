package datastructure;

public class QueueImplementation {
	public static void main(String ar[]){
		Queue myQueue=new Queue(4);
		myQueue.insert(10);
		myQueue.insert(20);
		myQueue.insert(30);
		myQueue.insert(40);
		System.out.println(myQueue.remove());
		myQueue.insert(50);
		
		
		
		
		
		myQueue.view();
		
	}
}
