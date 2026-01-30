#ifndef USELESSCMP_H
#define USELESSCMP_H

#ifdef __cplusplus
extern "C" {
#endif

// Add your declarations here

// variant specific function
void uselessCmp_PrintVariant();

// common function
void uselessCmp_PrintHello();

// addition function
int uselessCmp_Add(int a, int b);

// Logger interface for demonstration of GMock
typedef struct {
    void (*log)(const char* message);
    void (*logWithLevel)(int level, const char* message);
} uselessCmp_Logger_t;

// Function that uses the logger (for GMock demonstration)
void uselessCmp_SetLogger(uselessCmp_Logger_t* logger);
int uselessCmp_AddWithLogging(int a, int b);

int uselessCmp_AddWithFactor(int a, int b);

#ifdef __cplusplus
}
#endif

#endif // USELESSCMP_H