#include <stdio.h>
#include "uselessCmp.h"
#include "uselessCmp_private.h"

// Static logger instance for demonstration
static uselessCmp_Logger_t* g_logger = NULL;

// Working example below:
// @ UselessCmp Implementation, IMPL_UselessCmp, impl, REQ_SW_L1ComponentA, SWC_UselessCmp, draft, FeatureY

void uselessCmp_PrintHello(void)
{
    printf("Hello from uselessCmp!\n");
}

int uselessCmp_Add(int a, int b)
{    
    int result = a + b;
    printf("uselessCmp_Add: %d + %d = %d\n", a, b, result);
    return result;
}

void uselessCmp_SetLogger(uselessCmp_Logger_t* logger)
{
    g_logger = logger;
}

int uselessCmp_AddWithLogging(int a, int b)
{
    if (g_logger && g_logger->log) {
        g_logger->log("Starting addition operation");
    }
    
    int result = a + b;
    
    if (g_logger && g_logger->logWithLevel) {
        g_logger->logWithLevel(1, "Addition completed successfully");
    }
    
    return result;
}

int uselessCmp_internal_Add(int a, int b)
{    
    int result = a + b;
    printf("internal uselessCmp_Add: %d + %d = %d\n", a, b, result);
    return result;
}