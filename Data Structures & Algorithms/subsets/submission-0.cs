public class Solution {
    public List<List<int>> Subsets(int[] nums) {
        var result = new List<List<int>>();
        var curPath = new Stack<int>();
        void bt(int start)
        {
            result.Add(curPath.ToList());

            for (int i = start; i < nums.Length; i++)
            {
                curPath.Push(nums[i]);
                bt(i+1);
                curPath.Pop();
            }
        }
        
        bt(0);
        return result;
    }
}
