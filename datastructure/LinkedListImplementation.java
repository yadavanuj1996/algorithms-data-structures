package datastructure;

public class LinkedListImplementation {
	public static void main(String ar[]){
		
		Node nodeA=new Node();
		nodeA.data=4;
		Node nodeB=new Node();
		nodeB.data=3;
		Node nodeC=new Node();
		nodeC.data=7;
		Node nodeD=new Node();
		nodeD.data=1;
		
		nodeA.next=nodeB;
		nodeB.next=nodeC;
		nodeC.next=nodeD;
		
		LinkedListImplementation l=new LinkedListImplementation();
		System.out.println(l.linkListLength(nodeA));
	}
	public int linkListLength(Node aNode){
		int count=0;
		while(aNode!=null){
			
			aNode=aNode.next;
			count++;
		}

			return count;
	}
}
