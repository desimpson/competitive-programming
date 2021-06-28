#include <stdio.h>

#include <stdlib.h>

int main(void) {
    int nums[] = {
        2,
        7,
        11,
        15
    };
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    printf("numsSize = %d\n", numsSize);
    int target = 9;
    int * returnSize;

    return 0;
}

int * twoSum(int * nums, int numsSize, int target, int * returnSize) {
    int i, j;
    int * rtn;

    * returnSize = 2;
    rtn = (int * ) malloc(sizeof(int) * ( * returnSize));
    for (i = 0; i < numsSize - 1; ++i) {
        for (j = i + 1; j < numsSize; ++j) {
            if (nums[i] + nums[j] == target) {
                rtn[0] = i;
                rtn[1] = j;
                return rtn;
            }
        }
    }
    return rtn;
}
