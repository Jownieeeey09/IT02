import java.util.Scanner;

public class StringLengthComparator {
    public static void main(String[] args) {
        Scanner stringScanner = new Scanner(System.in);

        System.out.print("String1: ");
        String firstString = stringScanner.nextLine();

        System.out.print("String2: ");
        String secondString = stringScanner.nextLine();

        int length1 = firstString.length();
        int length2 = secondString.length();

        if (length1 > length2) {
            System.out.println(firstString + " is longer than " + secondString);
        } else if (length1 < length2) {
            System.out.println(firstString + " is shorter than " + secondString);
        } else {
            System.out.println(secondString + "has equal length as" + firstString);
        }

    }

}
