#include <stdio.h>
#include <time.h>
#include <math.h> 


long timediff(clock_t t1, clock_t t2) {
    long elapsed;
    elapsed = ((double)t2 - t1) / CLOCKS_PER_SEC * 1000;
    return elapsed;
}

int main()
{
    int c, d, pos, t;
    
    clock_t t1, t2;
    int a;
    long elapsed;
    t1 = clock();

    int x = 10;
    int array[x];
    for (int i=0; i<x;i++){
        array[i] = (rand() % 100);
    }
    
    for (c = 0; c < (x - 1); c++){
        pos = c;
        for (d = c + 1; d < x; d++){
            if (array[pos] > array[d]){
                pos = d;  
            } 
    }
    if (pos != c){
      t = array[c];
      array[c] = array[pos];
      array[pos] = t;
    }
  }
  
    t2 = clock();
    elapsed = timediff(t1, t2);
    printf("elapsed: %ld ms\n", elapsed);
  
  return 0;
}