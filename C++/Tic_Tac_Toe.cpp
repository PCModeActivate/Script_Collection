#include<stdio.h>

using namespace std;

int game(int board[3][3]){
    /// return code: -1 = P2 win, 0 = game not finished, 1 = P1 win, 2 = draw

    ///check horizontal
    for (int i = 0; i < 3; i++){
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2]){
            if (board[i][0]) return board[i][0];
        }
    }

    ///check vertical
    for (int i = 0; i < 3; i++){
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i]){
            if (board[0][i]) return board[0][i];
        }
    }

    ///check diagonals
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2]){
        if (board[0][0]) return board[0][0];
    }
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0]){
        if (board[0][2]) return board[0][2];
    }

    ///check draw
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            if (!board[i][j]) return 0;
        }
    }

    ///draw game
    return 2;
}

void print_board (int board[3][3]){
    printf("\n    0   1   2\n   ------------\n");
    for (int i = 0; i < 3; i++){
        printf("%d |", i);
        for (int j = 0; j < 3; j++){
            if (board[i][j] == 0){
                printf("   |");
            } else if (board[i][j] == 1){
                printf(" X |");
            } else {
                printf(" O |");
            }
        }
        printf("\n   ------------\n");
    }
}
int main(){
    int board[3][3];

    ///init
    for (int i = 0; i < 3; i++){
        board [i][0] = 0;
        board [i][1] = 0;
        board [i][2] = 0;
    }

    bool player_turn = false; /// F = p1, T = p2

    print_board(board);

    int endgame_code = 0;

    while (!endgame_code){
        if (player_turn){
            printf("Player O's turn.\n");
        } else {
            printf("Player X's turn.\n");
        }

        int x = 0, y = 0;
        printf("Input coordinate of your move below in the form of x,y (with comma, no whitespace).\n");
        scanf("%d,%d", &x, &y);

        while (x < 0 || x > 2 || y < 0 || y > 2 || board[y][x]){
            printf("Invalid input! Input coordinate of your move below in the form of x,y (with comma, no whitespace).\n");
            scanf("%d,%d", &x, &y);
        }

        if (player_turn){
            board [y][x] = -1;
        } else {
            board [y][x] = 1;
        }

        print_board(board);

        player_turn = !player_turn;

        endgame_code = game(board);

        if (endgame_code == 1){
            printf("X won.\n");
        } else if (endgame_code == -1){
            printf("O won.\n");
        } else if (endgame_code == 2){
            printf("Draw.\n");
        }
    }
    printf("Press e to exit.\n");
    char buffer = 0;
    while (buffer != 'e')
        scanf("%c", &buffer);
}
