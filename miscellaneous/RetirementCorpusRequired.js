# Future value of money and money required for retirment problem


import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class RetirementCorpusRequired
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		int initialAmt = 600000;
		float inflation=(float)0.05;
		int currentYear=2021;
		double totalCorpusRequiredForRetirement = 0;
		for(int i=25;i<=45;i++){
		    float opportunityCost=inflation;
		    float futureValueOfMoney = initialAmt*  (float) Math.pow((1+opportunityCost),i);
		    System.out.println("Future Value of 6 laks in year "+currentYear+" is "+futureValueOfMoney);
		    totalCorpusRequiredForRetirement+=futureValueOfMoney;
		    currentYear++;
		}
		System.out.println(totalCorpusRequiredForRetirement);
	}
}
