#include <gtest/gtest.h>
#include "uselessCmp.h"
#include "uselessCmp_private.h"


int main(int argc, char **argv)
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

// Demonstrate some basic assertions.
TEST(HelloTest, BasicAssertions) {
  // Expect two strings not to be equal.
  EXPECT_STRNE("hello", "world");
  // Expect equality.
  EXPECT_EQ(7 * 6, 42);
}


// @ UselessCmp HelloTest TC, TC_123, test, , , draft, FeatureY, IMPL_UselessCmp

// Demonstrate the testing of a module api function
TEST(HelloTest, CmpFunctionA) {
  
  //Define Test Expectation(s)
  int a = 3;
  int b = 4;
  int expected_result = a + b;

  //Execute the Test (Call the function)
  int result = uselessCmp_Add(a, b);
  
  //Check test result against defined expectation.
  EXPECT_EQ(expected_result, result);
}

// Demonstrate the testing of a module internal function
TEST(HelloTest, PrivateCmpFunctionA) {
  
  //Define Test Expectation(s)
  int a = 3;
  int b = 4;
  int expected_result = a + b;

  //Execute the Test (Call the function)
  int result = uselessCmp_internal_Add(a, b);
  
  //Check test result against defined expectation.
  EXPECT_EQ(expected_result, result);
}