#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_LINE_LENGTH 10000

char** readLinesFromFile(char *filename, int *lineCount);
unsigned concatenate(unsigned x, unsigned y);

int main() {

    int lineCount = 0;
    char **lineas = readLinesFromFile("../input.txt", &lineCount);
    int final_numbers[lineCount];

    for(int i = 0; i<lineCount; i++){
        int count_digits = 0;
        int *digits = NULL;

        for(int j = 0; j< strlen(lineas[i]); j++){

            if (isdigit(lineas[i][j])) {
                digits = realloc(digits, (count_digits + 1) * sizeof(int));
                digits[count_digits] = lineas[i][j] - '0';
                count_digits++;
            }

        }

        final_numbers[i] = concatenate(digits[0], digits[count_digits - 1]);

        count_digits = 0;
        free(digits);
    }

    int total = 0;
    for(int i = 0; i < lineCount; i++){
        total += final_numbers[i];
    }

    printf("Total: %d\n", total);
    return 0;
}


char** readLinesFromFile(char *filename, int *lineCount) {

    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error al abrir el archivo");
        exit(1);
    }

    char **lines = NULL;
    char buffer[MAX_LINE_LENGTH];
    int count = 0;

    while (fgets(buffer, MAX_LINE_LENGTH, file)) {
        lines = realloc(lines, (count + 1) * sizeof(char*));
        buffer[strcspn(buffer, "\n")] = 0;
        lines[count] = malloc(strlen(buffer) + 1);
        strcpy(lines[count], buffer);
        count++;
    }

    fclose(file);

    *lineCount = count;
    return lines;
}


unsigned concatenate(unsigned x, unsigned y) {
    unsigned pow = 10;
    while(y >= pow)
        pow *= 10;
    return x * pow + y;
}
