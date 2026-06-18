#include <string.h>
#include <stdio.h>

void secret_function() {
    char buffer[10];
    // ثغرة برمجية واضحة
    strcpy(buffer, "This string is definitely longer than ten characters!");
}

int main() {
    secret_function();
    return 0;
}
