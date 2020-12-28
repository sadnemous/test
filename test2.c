#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef char FIDS[29];


int main()
{
   char fids[3][30]={"First", "Second", "Third" }; 
   FIDS *fdPtr;
   printf("%s\n", fids[0]);
   printf("%s\n", fids[1]);
   fdPtr = fids;
   printf("%s\n", fdPtr[2]); 

   return 0;
}


