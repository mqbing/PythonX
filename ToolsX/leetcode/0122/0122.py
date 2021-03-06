from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

        在 0121_3 中记录最低、最高，虽然更快，但就无法解决本问题，可以卖出多次
        所以本问题需要用最大子数列解决
        子数列的结束时，累计子数列的值


        12345
        如果是连续增长的，只需要连续子数列就行
        1437
        只要价格降低，就可以卖出，不用担心后面会有更高价，因为卖出后就可以买入当天的低价

        >>> Solution().maxProfit([7,1,5,3,6,4])
        7
        >>> Solution().maxProfit([1,2,3,4,5])
        4
        >>> Solution().maxProfit([7,6,4,3,1])
        0
        """
        max_cur = max_so_far = 0
        for i in range(len(prices) - 1):
            dif = prices[i + 1] - prices[i]
            if dif < 0:
                # 卖出
                max_so_far += max_cur
                max_cur = 0
            else:
                # 延续子数列
                max_cur += dif
        # 退出循环时，如果有最大值，则加上
        max_so_far += max_cur
        return max_so_far


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
