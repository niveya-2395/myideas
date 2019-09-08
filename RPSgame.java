package testing;
import java.util.*;


public class RPSgame {
	
	public static void game(String ch1,String ch2)
	{
		ArrayList <String> list = new ArrayList<>();
		list.add("paper");
		list.add("rock");
		
		ArrayList <String> list1 = new ArrayList<>();
		list1.add("scissor");
		list1.add("paper");
		
		ArrayList <String> list2 = new ArrayList<>();
		list2.add("rock");
		list2.add("scissor");

		ArrayList <String> choice = new ArrayList<>();
		choice.add(ch1);
		choice.add(ch2);
		
		int value = ch1.compareTo(ch2);
		
		if(choice.equals(list) || choice.equals(list1) || choice.equals(list2))
		{
			System.out.println("Player 1 wins");
		}
			
		else if(value==0)
		{
			System.out.println("Tie");
		}
		
		else
		{
			Collections.reverse(list);
			Collections.reverse(list1);
			Collections.reverse(list2);
			if(choice.equals(list) || choice.equals(list1) || choice.equals(list2))
			{
				System.out.println("Player 2 wins");
			}
			
		}
		
		System.out.println("Game ends");
					
	}
	

	public static void main(String[] args) {
		
		String input1 = null;
		String input2 = null;
		
		
	    Scanner n = new Scanner(System.in);
		System.out.println("Player1");
		System.out.print("Enter rock, paper or scissor: ");
		input1 = n.next();
		System.out.print("Enter rock, paper or scissor: ");
		input2 = n.next();
		
		game(input1,input2);  
		
		System.out.print("Do you want to continue? Enter yes or no: ");
		String result = n.next();
		int value = result.compareTo("yes");
		if(value ==0)
		{
		  main(new String[] {"a", "b","c"});
		}
		
	}

}
