//java program to find largest of 4 numbers-tutorialsinhand.com
package tihInterviewPreparation;

public class TutorialsInHand {

	public static void main(String[] args) {		
		int n1 = 6661, n2 = 666, n3 = 188, n4 = 66;
		
		if(n1>n2 && n1>n3 && n1>n4) {
			System.out.println(n1+ " is greatest");
		} else if(n2>n1 && n2>n3 && n2>n4) {
			System.out.println(n2+ " is greatest");
		} else if(n3>n1 && n3>n2 && n3>n4) {
			System.out.println(n3+ " is greatest");
		} else {
			System.out.println(n4+ " is greatest");
		}
		
	}
}