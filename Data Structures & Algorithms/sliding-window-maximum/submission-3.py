class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        st = deque()
        result = []

        for right, num in enumerate(nums):
            while st and nums[st[-1]] < num:
                st.pop()
            
            st.append(right)

            left = right - k

            while st and st[0] <= left:
                st.popleft()
            
            if right + 1 >= k:
                result.append(nums[st[0]])
        return result