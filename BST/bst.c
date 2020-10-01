#include <stdio.h>
#include <stdbool.h>


struct nodo{
	int valor;
	struct nodo *esquerda;
	struct nodo *direita;

};typedef struct nodo No;



void printar(No *raiz);
No *criaNo(int valor);
No *busca(No *raiz, int *valor);
No *inserir(No *raiz, int valor);

int main(){

	int valor = 50;
	No *raiz = criaNo(valor);
	No *temp;
	char opc;

	while(1){
		getchar();
		printf("digite sua opcao\n");
		scanf("%c", &opc);
		getchar();
		if(opc == 'p'){
			printf("a arvore eh \n");
			printar(raiz);
		}else if(opc == 'b'){
			printf("digite o valor a ser buscado\n");
			scanf("%d", &valor);
			temp = busca(raiz, &valor);
			if(temp == NULL){
				printf("valor nao encontrado\n");
			}else{
				printf("valor encontrado : %d\n", temp->valor);
			}

		}else{
			printf("digite o valor a ser inserido\n");
			scanf("%d", &valor);
			inserir(raiz, valor);
			
		}
		
		
	}	

	return 0;
}

void printar(No *raiz){
	if(raiz != NULL){
		printar(raiz->esquerda);
		printf("%d\n",raiz->valor);
		printar(raiz->direita);
	}
}

No *criaNo(int valor){
	No *raiz = (No*)malloc(sizeof(No));
	raiz->esquerda = NULL;
	raiz->direita = NULL;
	raiz->valor = valor;
	return raiz;
}

No *busca(No *raiz, int *valor){
	
	if(raiz == NULL || raiz->valor == *valor){
		return raiz;
	}
	if(raiz->valor > *valor){
		return busca(raiz->esquerda, valor);
	}
	return busca(raiz->direita, valor);
}


No *inserir(No *raiz, int valor){
	if(raiz == NULL){
		return criaNo(valor);
	}
	if(raiz->valor > valor){
		raiz->esquerda = inserir(raiz->esquerda, valor);
	}else if(raiz->valor < valor){
		raiz->direita = inserir(raiz->direita, valor);
	}
	return raiz;
}

