#include <stdio.h>

void quick(int *vetor, int inicio, int fim);
int particionar(int *vetor, int inicio, int fim);
void troca(int *vetor, int i, int j);

int main(){
	int vetor[11] = {10,9,8,7,6,5,4,3,2,1,0};
	int i;
	printf("vetor de teste\n");
	for(i = 0; i <= 10; i++){
		printf("%d, ", vetor[i]);
	}
	printf("\n");
	quick(vetor, 0, 10);
	printf("vetor ordenado\n");
	for(i = 0; i <= 10; i++){
		printf("%d, ", vetor[i]);
	}
	printf("\n");
	
	return 0;
}


void quick(int *vetor, int inicio, int fim){
	int pivo;
    if(inicio < fim){
    	pivo = 	particionar(vetor, inicio, fim);
    	
    	quick(vetor, inicio, pivo-1);
    	quick(vetor, pivo+1, fim);
	}
	
}

int particionar(int *vetor, int inicio, int fim){
	int pivo = vetor[fim];
	int i = (inicio-1);
	int j;
	for(j = inicio; j <= fim-1; j++){
		if(vetor[j] <= pivo){
			i++;
			troca(vetor, i, j);
		}
	}
	troca(vetor, i+1,j);
	return (i+1);
}

void troca(int *vetor, int i, int j){
	int aux = vetor[i];
	vetor[i] = vetor[j];
	vetor[j] = aux;
}
