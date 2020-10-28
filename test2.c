#include <stdio.h>
#include <string.h>
int main()
{
  int i = 0;
  char type[4];
  for (i=1; i<10099;)
  {
    snprintf(type,4, "%4.4d", i);
    printf("%s\n", type);
    i = i + 50;
  }
  return 0;
}

