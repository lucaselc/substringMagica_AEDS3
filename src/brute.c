#include "brute.h"
#include <string.h>

bool brute_strstr(char* haystack, char* needle) {
    int i, j, k;
    int haystack_len = strlen(haystack);
    int needle_len = strlen(needle);

    // Percorre cada posição do texto onde o padrão pode caber
    for(i = 0; i <= (haystack_len - needle_len); i++) {
        k = i;
        j = 0;

        // Compara o padrão com a substring atual do texto
        while(haystack[k] == needle[j] && j < needle_len) {
            j++;
            k++;
        }

        // Se j alcançou o comprimento do padrão, uma correspondência foi encontrada
        if(j == needle_len) {
            return true;
        }
    }
    return false;
}
