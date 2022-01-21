#include <stdio.h>
#include <stdlib.h>
// ROWS and COLS are global variables for rows and columns
#define ROWS 10
#define COLS 10

// all my functions are declared here
int randomize(int max, int min);
void printGrid();
void placeMines();
int check(int x, int y);
int flag(int x, int y);
int checkWin();

//here are some more variables and arrays defined that are used in some of my functions
char grid[10][10];
char tempGrid[10][10];
int coolArray[10][10];
int totalMines = 10;
int mines = 0;

int main(){
    // cycle through tempGrid and assign '*' for all indexes
    int i, j;
    for (i = 0; i < ROWS; ++i) {
        for (j = 0; j < COLS; ++j) {
            tempGrid[i][j] = '*';
        }
    }
    // print out the array tempGrid with '*'
    for(i = 0; i < ROWS; i++){
        printf("%d\t", i);
        for(j =0; j < COLS; j++){
            if (tempGrid[i][j] == '*'){
                printf("%c\t", tempGrid[i][j]);
            }
            else {
                printf("%c\t", tempGrid[i][j]);
            }
        }
        printf("\n");
    }
// drop the mines into array grid
    placeMines();
//while loop runs through the game until you win or lose
    while (1) {
        int x, y, q=1;
        char z;
        //prompt user to input coordinates to either check or flag and what coordinate they want the move to be
        int i = 0, j = 0;
    printf("\nEnter 'c' for check cell, 'f' for flag cell.\n");
    printf("Enter command & cell row col:\t");
    scanf(" %c %d %d", &z, &x, &y);
    if (x >= ROWS || x < 0 || y >= COLS || y < 0) {
        printf("Enter value within the scope of the grid\n");
    }
    //if its a c then run check function
    if (z == 'c'){
        q = check(x, y);
    }
    //if its a f then run flag function
    else if (z == 'f'){
        flag(x, y);
    }
    //if user didn't input something a valid number or character
    else {
        printf("Enter either flag or check\n");
    }
    //loop the printGrid function and keep checking for win
        printGrid();
        checkWin();
    //some quick code to check if you won or lost and how to respond
        if(q==0) {
            printf("You hit a mine, game over.\n");
            break;
        }else if (checkWin()==1){
            printf("Congratulations! You win!");
            break;
        }
    }
}

int randomize (int max, int min){
    //randomize function
     return rand() % max + min;
}

void printGrid(){
    int i = 0, j = 0;
    i = 0;
    j = 0;
    //this double for loop is used to print out the tempGrid that the user sees
    for(i = 0; i < ROWS; i++){
        printf("%d\t", i);
        for(j =0; j < COLS; j++){
            if (tempGrid[i][j] == '*'){
                printf("%c\t", tempGrid[i][j]);
            }
            else {
                printf("%c\t", tempGrid[i][j]);
            }
        }
        printf("\n");
    }
}
void placeMines() {
    srand(2);
    int i, j;
    int x, y;
    //start out by assigning all indexes in grid to '0'
    for (i = 0; i < ROWS; i++) {
        for (j = 0; j < COLS; j++) {
            grid[i][j] = '0';
        }
    }
    //randomize the mines locations within the grid function
    for (mines = 0; mines < totalMines; mines++) {
        x = randomize(10, 0);
        y = randomize(10, 0);
        if (grid[x][y] != 'M') {
            grid[x][y]='M';
        }
        //if it wants to place a mine in a place where a mine already exist, don't
        else if (grid[x][y] == 'M'){
            mines--;
        }
    }
    //this mess is a bunch of if statements to add the number of mines within a numbers perimeters (8 spots around it)
    for (i = 0; i < ROWS; i++) {
        for (j = 0; j < COLS; j++) {
            if (grid[i][j] != 'M') {
                //ill walk you through one if statement. they all do the same thing for different neighbour
                //if the slot (in this case) in the bottom left corner is a mine and is within the scope of the game
                //make the number '1' instead of '0'
                if ((grid[i - 1][j - 1] == 'M') && ((i - 1) >= 0) && ((j - 1) >= 0)) {
                    grid[i][j]++;
                }if ((grid[i - 1][j] == 'M') && ((i - 1) >= 0)) {
                    grid[i][j]++;
                }if ((grid[i][j - 1] == 'M') && ((j - 1) >= 0)) {
                    grid[i][j]++;
                }if ((grid[i - 1][j + 1] == 'M') && ((i - 1) >= 0) && ((j + 1) <= 9)) {
                    grid[i][j]++;
                }if ((grid[i + 1][j - 1] == 'M') && ((i + 1) <= 9) && ((j - 1) >= 0)) {
                    grid[i][j]++;
                }if ((grid[i + 1][j] == 'M') && ((i + 1) <= 9)) {
                    grid[i][j]++;
                }if ((grid[i][j + 1] == 'M') && ((j + 1) <= 9)) {
                    grid[i][j]++;
                }if ((grid[i + 1][j + 1] == 'M') && ((i + 1) <= 9) && ((j + 1) <= 9)) {
                    grid[i][j]++;
                }
            }
        }
    }
}

int check(int x, int y) {
    if(grid[x][y]=='M'){
        tempGrid[x][y] = grid[x][y];
        return 0;
    //check to make sure same value isn't printed twice
    }else if (tempGrid[x][y] != '*') {
        printf("Please enter values that hasn't been used yet\n");
    //if the guess is valid reveal it
    }else if (tempGrid[x][y] == '*') {
        tempGrid[x][y] = grid[x][y];
        //this mess of if statements reveals all '0' on the map that are connected to the guessed '0' value
        //if you are wondering why it's called cool array it's because I almost broke my laptop making it :)
        if (grid[x][y] == '0') {
            coolArray[x][y]++;
            if ((grid[x - 1][y - 1] == '0') && ((x - 1) >= 0) && ((y - 1) >= 0) && coolArray[x-1][y-1]==0) {
                check(x-1, y-1);
            }else if(((x - 1) >= 0) && ((y - 1) >= 0)){
                tempGrid[x-1][y-1]=grid[x - 1][y - 1];
            }
            //ill walk you through one if statement and what it does
            //so if a neighbouring value is also '0' then reveal it
            if ((grid[x - 1][y] == '0') && ((x - 1) >= 0) && coolArray[x-1][y]==0) {
                check(x-1, y);
            // but make sure to only reveal it if it's in the scope of the map
            }else if(((x - 1) >= 0)){
                tempGrid[x - 1][y]=grid[x - 1][y];
            }
            if ((grid[x][y - 1] == '0') && ((y - 1) >= 0) && coolArray[x][y-1]==0) {
                check(x, y-1);
            }else if(((y - 1) >= 0)){
                tempGrid[x][y - 1]=grid[x][y - 1];
            }
            if ((grid[x + 1][y] == '0') && ((x + 1) <= 9) && coolArray[x+1][y]==0) {
                check(x+1, y);
            }else if(((x + 1) <= 9)){
                tempGrid[x + 1][y]=grid[x + 1][y];
            }
            if ((grid[x][y + 1] == '0') && ((y + 1) <= 9) && coolArray[x][y+1]==0) {
                check(x, y+1);
            }else if(((y + 1) <= 9)){
                tempGrid[x][y + 1]=grid[x][y + 1];
            }
            if ((grid[x + 1][y + 1] == '0') && ((y + 1) <= 9) && ((x + 1) <= 9) && coolArray[x+1][y+1]==0) {
                check(x+1, y+1);
            }else if(((y + 1) <= 9) && ((x + 1) <= 9)){
                tempGrid[x + 1][y + 1]=grid[x + 1][y + 1];
            }
            if ((grid[x - 1][y + 1] == '0') && ((y + 1) <= 9) && ((x - 1) >= 0)&& coolArray[x-1][y+1]==0) {
                check(x-1, y+1);
            }else if(((y + 1) <= 9) && ((x - 1) >= 0)){
                tempGrid[x - 1][y + 1]=grid[x - 1][y + 1];
            }
            if ((grid[x + 1][y - 1] == '0') && ((x + 1) <= 9) && ((y - 1) >= 0)&& coolArray[x+1][y-1]==0) {
                check(x+1, y-1);
            }else if(((x + 1) <= 9) && ((y - 1) >= 0)){
                tempGrid[x + 1][y - 1]=grid[x + 1][y - 1];
            }
        }
    }
    return 1;
}

int flag(int x, int y){
    //simple code that allows players to flag potential mines
    tempGrid[x][y] = 'F';
}

int checkWin(){
    int i, j, haveWon;
    //a loop that says if there is only 10 not guessed slots you win
    //this is done by adding 1 to a temp variable everytime a 'F' is used and based on how many '*" still remain
    for(i = 0; i < ROWS; i++){
        for(j = 0; j < COLS; j++){
            if(tempGrid[i][j]=='F'||tempGrid[i][j]=='*'){
                haveWon++;
            }
        }
    }
    //when temp variable hits 10 you win
    if(haveWon==10){
        return(1);
    }
    return 0;
}



