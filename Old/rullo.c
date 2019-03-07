#include <stdio.h>
typedef struct Puzzle 
{
	int size;
	int * row_targets;
	int * col_targets;
	int * nums;
} Puzzle;

int * get_array(char * str)
{
	printf("%s", str);
	return NULL;
}

#define MAXCHAR 1000
int main() 
{	
	/*
    FILE *fp;
    char str[MAXCHAR];
    char* filename = "./test-cases/1-sanity-check.txt";
 
    fp = fopen(filename, "r");
    if (fp == NULL){
        printf("Could not open file %s",filename);
        return 1;
    }
    
    //get size
    fgets(str, MAXCHAR, fp);
    int size; 
    sscanf(str, "%d", &size);

    while (fgets(str, MAXCHAR, fp) != NULL)
        printf("%s", str);
    fclose(fp);

    int mark[5] = {19, 10, 8, 17, 9};
    Puzzle puzzle = {size, mark, mark, mark};
    printf("\n%d",puzzle.size);
    return 0;
    */
    get_array("hello");
    return 0;
}