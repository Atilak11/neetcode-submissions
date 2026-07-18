class Solution {
    public int[] twoSum(int[] nums, int target) {
        int num1 = 0;
        int num2 = 0;
        int[] arr = new int[2];

        HashMap<Integer, Integer> find = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            num1 = i;

            if (find.containsKey(target - nums[i]))
            {
                num2 = find.get((target-nums[i]));
                arr[0] = num2;
                arr[1] = num1;
                return arr;
            }
            find.put(nums[i], i);
            
        }
        return arr;
    }
}
