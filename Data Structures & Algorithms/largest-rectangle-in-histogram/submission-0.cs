public class Solution {
    public int LargestRectangleArea(int[] heights) {
        var stack = new Stack<int>();
        var maxArea = 0;
        for (var i = 0; i <= heights.Length; i++) {
            while (stack.Count != 0 && (i == heights.Length || heights[stack.Peek()] >= heights[i])) {
                var h = heights[stack.Pop()];  // popped bar = rectangle height
                var leftBound =
                    stack.Count == 0 ? -1 : stack.Peek();  // nearest smaller on the left
                var width = i - leftBound - 1;             // i is the right boundary
                maxArea = Math.Max(maxArea, h * width);
            }
            stack.Push(i);
        }


        return maxArea;
    }
}
