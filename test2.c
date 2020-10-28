#include <stdio.h>
#include <string.h>
#define TYPE_LEN 4
int main()
{
  int i = 0;
  char type[TYPE_LEN+1];
  for (i=1; i<10099;)
  {
    snprintf(type,TYPE_LEN+1, "%4.4d", i);
    printf("%s\n", type);
    i = i + 50;
  }
  return 0;
}

