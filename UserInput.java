import java.io.FileWriter;
import java.io.IOException;
import java.util.NoSuchElementException;
import java.util.Scanner;
import java.io.Console;

public class UserInput {
    public static void getUserDetails(){

        //Getting username
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your username: ");
        String username = sc.nextLine();
        
        //Getting password
        // Console console = System.console();
        // if(console == null){
        //     System.out.println("Couldn't get Console instance");
        //     System.exit(0);
        // }
        // char[] passwordArray = console.readPassword("Enter your password: ");
        // String password = new String(passwordArray);
        
        System.out.print("Enter your password: ");        
        String password = sc.nextLine();
        sc.close();

        try {
           FileWriter w = new FileWriter("userDetails.txt");
           w.write("username:" + username + "\n" +
                    "password:" + password);
           w.close();
        } catch (IOException e) {
           System.out.println("Failed to write file.");
           e.printStackTrace();
        }
    }

    public static void main(String[] args){

        try {
            getUserDetails();
        } catch (NoSuchElementException e) {
            System.out.println("ERROR");
            e.printStackTrace();
        }
        
    }
}
