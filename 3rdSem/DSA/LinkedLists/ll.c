#include <stdio.h>
#include <stdio.h>

typedef struct Human {
    char* NickName;
    int age;
    struct Human* wants_to_kill;
} Human;

void SetNewTarget(struct Human* Random_Person, struct Human* Target)
{
  while (Random_Person->wants_to_kill != NULL)
  {
    *Random_Person = *(Random_Person->wants_to_kill);
  }
  Random_Person->wants_to_kill = Target;
}

int main(void)
{
  Human pranav = {"Pranav", 20, NULL};
  Human shreyash = {"Yash", 35, NULL};
  Human Lohit = {"Lohit", 12, NULL};
  SetNewTarget(&pranav  ,&shreyash);
  SetNewTarget(&shreyash,&Lohit);

  Human Current_Human = pranav;
  
  while (Current_Human.wants_to_kill != NULL) {
    printf("%s wants to kill %s\n", Current_Human.NickName, Current_Human.wants_to_kill->NickName);
    Current_Human = *(Current_Human.wants_to_kill);
  }
  printf("%s wants to kill no one \n",Current_Human.NickName);
  
  return 0;
}
