impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        
        return nums.iter().map(|x|*x).collect::<std::collections::HashSet<i32>>().len() != nums.len()

    }
}
