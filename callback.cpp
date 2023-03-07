#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "callback.h"

callback_t callback = NULL;

int setCallback(callback_t f){
    callback = f;
    return 0;
}

int doCallback(char* s) {
    return callback(s);
}

void c_free(void *ptr) {
         free(ptr);
}
