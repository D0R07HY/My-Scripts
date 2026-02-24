import java.util.*;

class exception2
{
	int numIndex()
	{
		int num;
		
		for (; ; )
		{
			try
			{
				Scanner scan=new Scanner(System.in);
				System.out.print("Number of index"+" : ");
				num=scan.nextInt();
				break;
			}
			catch (InputMismatchException err)
			{
				System.out.println("Input Integer Only!!");
			}	
		
		}
		
		return num;
	}
	
	
	int read(int i)
	{
		int num;
		
		for (; ; )
		{
			try
			{
				Scanner scan=new Scanner(System.in);
				System.out.print("Num"+i+" : ");
				num=scan.nextInt();
				break;
			}
			catch (InputMismatchException err)
			{
				System.out.println("Input Integer Only!!");
			}	
		
		}
		
		
		
		return num;
	}
	
	int sum(int i)
	{
		
		int sum=0+i;
		
		
		return sum;
	}
	
	
	void print(int sum)
	{
		System.out.println(sum);
	}
	
	public static void main(String[] args) 
	{
		exception2 obj=new exception2();
		int index=obj.numIndex();
		int num[]=new int[index];
		int num1,num2,sum,result=0;
		for (int i=0;i<num.length ;i++ )
		{
			num[i]=obj.read(i+1);
			result+=obj.sum(num[i]);
			
		}
		
		obj.print(result);
		
		
		
		
		
		
		
		
		
		
	}
}
