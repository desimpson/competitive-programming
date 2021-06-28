#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "../doctest.h"
#include <iostream>
#include <vector>

using namespace std;

vector<int> twoSum(vector<int> &, int);

vector<int> twoSum(vector<int> &nums, int target) {
    int n = nums.size();
    for (int i = 0; i < n - 1; ++i) {
        int num1 = nums[i];
        for (int j = i + 1; j < n; ++j) {
            int num2 = nums[j];
            if (num1 + num2 == target)
                return vector<int>{i, j};
        }
    }
    return vector<int>();
}

TEST_CASE("testing twoSum examples") {
    vector<int> nums;
    int target;
    vector<int> expected;

    // Example 1
    nums = {2, 7, 11, 15};
    target = 9;
    expected = {0, 1};
    CHECK(twoSum(nums, target) == expected);

    // Example 2
    nums = {3, 2, 4};
    target = 6;
    expected = {1, 2};
    CHECK(twoSum(nums, target) == expected);

    // Example 3
    nums = {3, 3};
    target = 6;
    expected = {0, 1};
    CHECK(twoSum(nums, target) == expected);
}
