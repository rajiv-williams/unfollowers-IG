import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class WhoUnfollowedMe{

    private static ArrayList<String> getUnfollowers(ArrayList<String> followers, ArrayList<String> following){
        ArrayList<String> unfollowers = new ArrayList<String>();

        for(int i = 0; i < following.size(); i++){
            boolean userFound = false;
            String currUser = following.get(i);

            for(int j = 0; j < followers.size(); j++){
                if(followers.get(j).equals(currUser)){
                    userFound = true;
                    break;
                }
            }
            if(!userFound){
                unfollowers.add(currUser);
            }
        }
        return unfollowers;
    } 

    public static String arrayToString(ArrayList<String> a){
        String result = "";

        for(int i = 0; i < a.size(); i++){
            result+= a.get(i) + "\n";
        }
        return result;
    }
    public static void main(String[] args) {

     ArrayList<String> followers = new ArrayList<String>();
     ArrayList<String> following = new ArrayList<String>();
     String followerFile = "./followers.txt";
     String followingFile = "./following.txt";

     try {
        Scanner scFollowers = new Scanner(new File(followerFile));
        Scanner scFollowing = new Scanner(new File(followingFile));
        while(scFollowers.hasNextLine()){
            followers.add(scFollowers.nextLine());
        }
        while(scFollowing.hasNextLine()){
            following.add(scFollowing.nextLine());
        }
     } catch (FileNotFoundException e) {
        e.printStackTrace();
     }
     ArrayList<String> unfollowers = getUnfollowers(followers, following);
     String result = arrayToString(unfollowers);

     if(result != ""){
        System.out.println("\n" + String.valueOf(unfollowers.size()) + " accounts do not follow you:\n\n");
        System.out.println(result);
     }
     else{
        System.out.println("\n \\_(ツ)_/¯ \n\n");
     }
        
    }
}   