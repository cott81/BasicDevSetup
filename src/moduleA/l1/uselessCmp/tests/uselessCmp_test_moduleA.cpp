#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include "uselessCmp.h"

using ::testing::_;
using ::testing::StrEq;
using ::testing::InSequence;

// Mock implementation of the logger interface
class MockLogger {
public:
    MOCK_METHOD(void, log, (const char* message), ());
    MOCK_METHOD(void, logWithLevel, (int level, const char* message), ());
};

// Global mock instance for C interface
static MockLogger* g_mockLogger = nullptr;

// C wrapper functions that call the mock
extern "C" {
    static void mockLog(const char* message) {
        if (g_mockLogger) {
            g_mockLogger->log(message);
        }
    }
    
    static void mockLogWithLevel(int level, const char* message) {
        if (g_mockLogger) {
            g_mockLogger->logWithLevel(level, message);
        }
    }
}

// Test fixture for GMock demonstration
class UselessCmpLoggerTest : public ::testing::Test {
protected:
    void SetUp() override {
        g_mockLogger = &mockLogger;
        logger.log = mockLog;
        logger.logWithLevel = mockLogWithLevel;
        uselessCmp_SetLogger(&logger);
    }
    
    void TearDown() override {
        uselessCmp_SetLogger(nullptr);
        g_mockLogger = nullptr;
    }
    
    MockLogger mockLogger;
    uselessCmp_Logger_t logger;
};

// Test that demonstrates GMock expectations
TEST_F(UselessCmpLoggerTest, AddWithLogging_CallsLoggerMethods) {
    // Arrange - Set up expectations
    EXPECT_CALL(mockLogger, log(StrEq("Starting addition operation")))
        .Times(1);
    EXPECT_CALL(mockLogger, logWithLevel(1, StrEq("Addition completed successfully")))
        .Times(1);
    
    // Act - Call the function under test
    int result = uselessCmp_AddWithLogging(5, 3);
    
    // Assert - Verify the result
    EXPECT_EQ(8, result);
    // Mock expectations are automatically verified in destructor
}

// Test with ordered expectations
TEST_F(UselessCmpLoggerTest, AddWithLogging_CallsLoggerInOrder) {
    // Arrange - Set up ordered expectations
    InSequence seq;
    EXPECT_CALL(mockLogger, log(_))
        .Times(1);
    EXPECT_CALL(mockLogger, logWithLevel(_, _))
        .Times(1);
    
    // Act
    uselessCmp_AddWithLogging(10, 20);
    
    // Expectations verified automatically
}

// Test without logger (null safety)
TEST(UselessCmpLoggerTest_NoFixture, AddWithLogging_NullLogger_DoesNotCrash) {
    // Arrange - No logger set (should be null)
    uselessCmp_SetLogger(nullptr);
    
    // Act & Assert - Should not crash
    int result = uselessCmp_AddWithLogging(1, 2);
    EXPECT_EQ(3, result);
}
