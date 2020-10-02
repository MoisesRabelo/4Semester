import static java.lang.Integer.max;
import java.util.Scanner;

class No{
    public int dado;
    public No esquerdo; 
    public No direito;
    
    No(int dado){
        this.dado = dado;
    }
    
    public String toString(){
        return "{"+dado+"}";
    }
}

public class ArvoreBinaria {
    No raiz;
    
    public No criaNo(int dado){
        return new No(dado);
    }
    
    public No insere (No raiz, int dado){
        if(raiz == null) return criaNo(dado);
        else{
            if(dado <= raiz.dado){
                raiz.esquerdo = insere(raiz.esquerdo, dado);
            }
            else{
                raiz.direito = insere(raiz.direito, dado);
            }
        }
        return raiz;
    }
    
    public boolean pesquisa(No raiz, int valor){
        if(raiz == null) return false;
        else{
            if(valor == raiz.dado){
                return true;
            }
            else{
                if(valor < raiz.dado){
                    return pesquisa(raiz.esquerdo, valor);
                }
                else{
                    return pesquisa(raiz.direito, valor);
                }
            }
        }
    }
    
    public int menorValor(No raiz){
        while(raiz.esquerdo != null){
            raiz = raiz.esquerdo;
        }
        return raiz.dado;
    }
    
    public int profundMax(No raiz){
        int profEsq, profDir;
        if(raiz == null) return 0;
        
        else{
            profEsq = profundMax(raiz.esquerdo);
            profDir = profundMax(raiz.direito);
        }
        return max(profEsq, profDir) + 1;
    }
    
    public int tamanho(No raiz){
        if(raiz == null) return 0;
        
        else return tamanho(raiz.esquerdo) + 1 + tamanho(raiz.direito);
        
    }
    
    public void printArvore(No raiz){
        if(raiz != null){
            printArvore(raiz.esquerdo);
            System.out.println("{"+raiz.dado+"}");
            printArvore(raiz.direito);
        }
    }
    
    public void printArvoreInvertida(No raiz){
        if(raiz != null){
            printArvoreInvertida(raiz.direito);
            System.out.println("{"+raiz.dado+"}");
            printArvoreInvertida(raiz.esquerdo);
        }
    }
    
    public void printNos(No raiz){
        int d, esq = 0, dir = 0;
        if(raiz == null){
            return;
        }
        d = raiz.dado;
        if(raiz.esquerdo != null){
            esq = raiz.esquerdo.dado;
        }
        if(raiz.direito != null){
            dir = raiz.direito.dado;
        }
        System.out.println("{"+d+"["+esq+","+dir+"]"+"}");
        printNos(raiz.esquerdo);
        printNos(raiz.direito);
    }
    
    public static void main(String[] args) {
        Scanner ent = new Scanner(System.in);
        ArvoreBinaria ArvBin = new ArvoreBinaria();
        No raiz = ArvBin.criaNo(0);
        
        System.out.println("Quantos nós a inserir? ");
        int num = ent.nextInt();
        for(int i=0; i<num; i++){
            System.out.printf("Digite o valor do nó %d: ", i);
            int a = ent.nextInt();
            ArvBin.insere(raiz, a);
        }
        System.out.println("Impressão na forma de lista: ");
        ArvBin.printArvore(raiz);
        
        System.out.println("Impressão como lista invertida: ");
        ArvBin.printArvoreInvertida(raiz);
        
        System.out.println("Impressão por nós: ");
        ArvBin.printNos(raiz);
        
        System.out.println("Digite um valor para encontrar: ");
        int b = ent.nextInt();
        if(ArvBin.pesquisa(raiz, b)){
            System.out.println("Encontrado!");
        }
        else{
            System.out.println("Não encontrado");
        }
        
        System.out.println("Menor valor da árvore: "+ArvBin.menorValor(raiz));
        System.out.println("Profundidade máxima: "+ArvBin.profundMax(raiz));
        System.out.println("Tamanho da árvore: "+ArvBin.tamanho(raiz));
    } 
}
