#include <linux/limits.h>
#include <stdio.h>

char* sqrtop = " ------ ";
char* sqrgap = "      ";
char* payload= ">>--->";
int height = 4;

int main()
{
    printf("%s%s%s\n",sqrtop,sqrgap,sqrtop);
    for(int i = 0; i <= height; i++)
    {
        if(i != (height/2)){printf("|%s|%s|%s|\n",sqrgap,sqrgap,sqrgap);}
        else{printf("|%s|%s|%s|\n",sqrgap,payload,sqrgap);}
    }
    printf("%s%s%s\n",sqrtop,sqrgap,sqrtop);
    return 0;
}
