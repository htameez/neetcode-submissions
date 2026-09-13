class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force solution:

        # for each temperature, check if next temp is greater than current temp
        # if yes, push 1
        # if no, continue searching and use counter
            # push number
        # if len(temperatures) == 1:
        #     return [0]

        # result = []
        # for i in range(len(temperatures) - 1):
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             result.append(j - i)
        #             break
        #         if j == len(temperatures) - 1:
        #             result.append(0)
        # result.append(0)
        # return result

        # efficient solution: monotonically decreasing stack

        # push indices if temp at that index is less than top element
        # if current temp is greater than top element, push index of that element - top element's index to result array
        if len(temperatures) == 1:
            return [0]

        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                popped_index = stack.pop()
                result[popped_index] = i - popped_index
            
            stack.append(i)

        return result
