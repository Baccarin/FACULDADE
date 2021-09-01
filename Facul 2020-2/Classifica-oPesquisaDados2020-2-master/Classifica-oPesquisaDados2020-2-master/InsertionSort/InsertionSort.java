package InsertionSort;

import java.util.Random;

public class InsertionSort {

    Random gerador = new Random();

    public int[] preencheVetor(int tamanho) {
        int vetor[] = new int[tamanho];
        for (int i = 0; i < tamanho; i++) {
            vetor[i] = (gerador.nextInt(100));
        }
        return vetor;
    }

    public int [] Insertion(int vetor[], int tamanho) {
        int chave, j;
        for (int i = 1; i < tamanho; i++) {
            chave = vetor[i];
            j = i - 1;
            while (j >= 0 && vetor[j] > chave) {
                vetor[j + 1] = vetor[j];
                j--;
            }
            vetor[j + 1] = chave;
        }
        return vetor;
    }

    public void printVetor(int vetor[]) {
        for (int i = 0; i < vetor.length; i++) {
            System.out.printf(" %d -", vetor[i]);
        }
        System.out.println("\n-------");
    }

    public static void main(String[] args) {
        InsertionSort insert = new InsertionSort();
        int vetor[] = insert.preencheVetor(50);
        insert.printVetor(vetor);
        vetor = insert.Insertion(vetor, vetor.length);
        insert.printVetor(vetor);
    }
}