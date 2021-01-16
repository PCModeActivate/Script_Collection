#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;

int x1 = 1, x2 = 0, y1 = 0, y2 = 1;
///This is a program used to find the linear diophantine equation solution for any given question.
void GCDWR(int a, int b){
    string t = "";
    int q = a/b;
    int r = a - q*b;
    int tempx = x1, tempy = y1;
    x1 = x2;
    x2 = tempx-q*(x2);
    y1 = y2;
    y2 = tempy-q*(y2);
    ///printf("x = %d, y = %d, r = %d, q =  %d\n", x2, y2, r, q);
    if (b%r == 0){
        printf("GCD = %d, certificate is x = %d, y = %d\n\n", r, x2, y2);
    }
    else
        GCDWR(b,r);
}

int main(){
    int a,b;
    for (;;){
        printf("Enter your a and b for GCD(a,b) where a>=b in order, separated by a comma:\n");
        scanf("%d,%d", &a,&b);
        x1 = 1; x2 = 0; y1 = 0; y2 = 1;
        GCDWR(a,b);
    }
}
