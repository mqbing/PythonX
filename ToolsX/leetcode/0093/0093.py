from typing import List

from twisted.trial import unittest


class Solution:
    """20190921"""

    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        思路，因为是 4 部分，取出一个数字做为第一部分，然后再判断后面的
        要注意范围是 0-255
        要注意不能以 0 开头
        """
        ans = []
        self.restore_ip_addresses(ans, [], s, 4)
        return ans

    def restore_ip_addresses(self, ans: List[str], pre: List[str], s: str, n: int):
        if s == '' and n == 0:
            ans.append('.'.join(pre))
        elif s == '' or n == 0:
            return
        else:
            length = len(s)  # 这里可以再优化
            for count in range(1, 4):
                if length >= count:
                    # 取一位
                    t = s[:count]
                    if self.is_valid_part(t):
                        self.restore_ip_addresses(ans, pre + [t], s[count:], n - 1)

    def is_valid_part(self, s: str):
        return s != '' and 0 <= int(s) <= 255 and (s[0] != '0' or s == '0')  # 第一位不是 0 或者本身就是 0:


class _Test(unittest.TestCase):
    def test(self):
        _input = '25525511135'
        _output = Solution().restoreIpAddresses(_input)
        _expect = ["255.255.11.135", "255.255.111.35"]
        self.assertListEqual(_expect, _output)
