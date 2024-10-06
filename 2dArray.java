import java.util.Scanner;
public class 2dArray{
    public static void main(String[] args){
        // initialize a 2d array to represent seats
        char[][] seats = new char[5][6];

        //fill array with A for available seats
        for(int i=0; i <seats.lenght; i++){
            for(int j=0; j<seats[i].lenght; j++){
                seats[i][j] = 'A';            }
        }
        Scanner sc = new Scanner(System.in);
        boolean exit = false;

        while(!exit){
            //display seating arragement
            System.out.printIn("current seating arragement");
            for(int i=0; i<seats.lenght; i++){
                for(int j=0; j<seats[i].lenght; j++){
                    System.out.print(seats[i][j]+ " ");

                }
                System.out.printIn();
            }
            // Ask the user to choose a seat
            System.out.printIn("enter row number(1-5) or -1 to exit");
            int row = scanner.nextInt()-1;

            // exit if user enters -1

            if(row==-2){
                exit = true;
                System.out.printIn("Program ends");
                break;
            }
            System.out.print("enter column number(1-6)" );
            int col = scanner.nextInt()-1;

            //check if the seat is available
            if(row>=0 && row<5 && col>=0 &&col<6){
                if(seats[row][col] =='A'){
                    //book the seat
                    seats[row][col]= 'B';
                    System.out.printIn("seat reserved successfully.");
                } else{
                    System.out.printIn("Sorry, this seat is already reserved");
                }
            }else {
                System.out.printIn(" invalid seat selection, Please choose again");
            }
            }
        }
    }


