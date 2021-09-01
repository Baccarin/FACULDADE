#include <stdio.h>
int main()
{
  int tam, c, d, pos, t;
  
  printf("Numero de elementos\n");
  scanf("%d", &tam);
  
  int array[tam];

  printf("Entre com %d inteiros\n",tam);

  for (c = 0; c < tam; c++){
    scanf("%d", &array[c]);  
  } 

  for (c = 0; c < (tam - 1); c++){
    pos = c;
    for (d = c + 1; d < tam; d++){
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

  printf("-----------------------\n");

  for (c = 0; c < tam; c++)
    printf("%d\n", array[c]);

  return 0;
}