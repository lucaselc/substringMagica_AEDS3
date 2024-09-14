#include "bmh.h"
#include <stdlib.h>
#include <string.h>

// Algoritmo de comparação utilizado no BMH.
// A principal diferença entre algoritmos convencionais é começar pelo final da string.
static bool streq(char* str1, char* str2, int len) {
    for (int i = len - 1; i >= 0 ; i--) {
        if (str1[i] != str2[i]) {
            return false;
        }
    }
    return true;
}

static char* preprocess(char* needle) {
    char* tbl = malloc(256);
    int size = strlen(needle);

    // Inicializa tabela
    for(int i = 0; i < 256; i++) {
        tbl[i] = size;
    }

    // Preenche tabela
    for(int i = 0; i < size-1; i++) {
        tbl[needle[i]] = size - 1 - i;
    }

    return tbl;
}

bool bmh_strstr(char* haystack, char* needle) {
    // Inicializa a tabela de preprocessamento
    char* table = preprocess(needle);
    int skip = 0;
    int haystack_len = strlen(haystack);
    int needle_len = strlen(needle);
    while (haystack_len - skip >= strlen(needle)) {
        // Testa se a substring é igual ao segmento atual de haystack
        if (streq(&haystack[skip], needle, needle_len)) {
            free(table);
            return true;
        }
        // Desloca a busca para frente
        skip += table[haystack[skip + needle_len - 1]];
    }
    free(table);
    return false;
}
