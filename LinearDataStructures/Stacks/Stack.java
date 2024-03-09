

/**
 * Stack
 */
public class Stack {
    static int size=5;
     static int a[]=new int[size];
     static int top=-1;
     private static void push(int val){
      if(top==size-1){
          System.out.println("value can not be inserted stack will overflow");
      }
      else{
          top++;
          a[top]=val;
          System.out.println("element pushed is "+a[top]);
      }
  
     }
     private static void pop(){
      if(top==-1){
          System.out.println("value can not be poped out stack is underflowing");
      }
      else{
          System.out.println("value popped is:"+a[top]);
          top--;
          
      }
     }
     private static void peep(){
      if(top==-1){
          System.out.println("no elemnets are present");
      }
      else{
          System.out.println("top pointing element is "+a[top]);
      }
     }
  
      public static void main(String[] args) {
          push(10);
          push(20);
          peep();
          pop();
          peep();
          
          
      }
  }