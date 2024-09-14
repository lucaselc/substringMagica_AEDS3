#define MAX_SIZE 255

typedef unsigned int uint;

typedef struct {
    uint a;
    uint b;
} query_t;

typedef struct {
    char* haystack;
    char* needle;
    query_t* queries;
    uint queries_len;
} problem_input_t;

problem_input_t* read_file(const char* name, int* size);
void input_free(problem_input_t* input);
