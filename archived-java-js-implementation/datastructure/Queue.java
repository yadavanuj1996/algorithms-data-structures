package datastructure;

public class Queue {

	private int rear,front,maxSize,noOfItems;		// rear,front are index depending on the items in queue
	private long queueArray[];						//Queue 
	
	public Queue(int size){
		this.maxSize=size;							// Maximum items a queue can have
		this.rear=-1;								//The rear shows the latest index where element is added
		this.front=0;								// index position of the first elemetn
		this.noOfItems=0;							// Total no of itmes in queue is 0 in starting
		this.queueArray=new long[maxSize];
	}
	public void insert(long item){
		if(!isFull()){
			rear++;
			noOfItems++;
				
			queueArray[rear]=item;
		}
		else{
			System.out.println("Queue Full");
		}
		
	}
	public long remove(){				
		if(!isEmpty()){
			int oldFront=front;
			front++;
			noOfItems--;
		
			if(front==maxSize){
				front=0;
				rear=-1;
			}
				
			return queueArray[oldFront];
		
		}
		else{
			System.out.println("Queue is empty");
			return -1;
		}
			
	}
	public void view(){						//To display the contents of the queue 
		System.out.print("[ ");
		for(int i=front;i<=rear;i++){
			System.out.print(queueArray[i]+" ");
		}
		System.out.print("]");
	}
	public long peekFront(){
		return queueArray[rear];
	}
	
	public boolean isFull(){
		return (noOfItems==maxSize);
	}
	public boolean isEmpty(){
		return (noOfItems==0);
	}
}
