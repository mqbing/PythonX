class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """不包含重复字符的最长子字符串

        i∈[0,n)
            记录之前的最长串
            如果 s[i] 位于最长串中，最长串加 1
            否则最长串变为 s[i] 的首次出现位置到 i

        要注意
        选择在有重复字符的时候才赋值，那么退出循环时需要加上后面不重复的

        1
        如果不使用 find 函数，加一层遍历

        >>> Solution().lengthOfLongestSubstring('ohomm')
        3
        >>> Solution().lengthOfLongestSubstring('')
        0
        >>> Solution().lengthOfLongestSubstring('a')
        1
        >>> Solution().lengthOfLongestSubstring('au')
        2
        >>> Solution().lengthOfLongestSubstring('aab')
        2
        >>> Solution().lengthOfLongestSubstring('abcabcbb')
        3
        >>> Solution().lengthOfLongestSubstring('bbbbb')
        1
        >>> Solution().lengthOfLongestSubstring('pwwkew')
        3
        """
        length = len(s)
        max_start = max_length = 0
        for i in range(1, length):  # 从 1 开始，如果长度为 1 ，在返回时会处理
            cur_max_str = s[max_start:i]  # 当前最长子串
            position = -1
            for j in range(len(cur_max_str)):  # 比 find 函数慢
                if cur_max_str[j] == s[i]:
                    position = j
                    break
            if position != -1:  # 找到重复元素
                max_length = max(max_length, i - max_start)  # 记录最长，因为不包含当前元素，所以不用加 1
                max_start = max_start + position + 1  # 重置起点，注意从 s 中找到直接取 position，如果是截取字符串再查找，应该加上起始索引
        return max(max_length, length - max_start)  # 返回的时候还要再处理，如果没进入循不，返回 length ，如果进入了，则最后一部分不重复的，要计入总长度


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
