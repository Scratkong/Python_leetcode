# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#     左括号必须用相同类型的右括号闭合。
#     左括号必须以正确的顺序闭合。
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
#
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
#
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
# 在真实的面试中遇到过这道题？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        # "error "
        # for i in range(len(s)/2):
        #     if s[i] = '(' and s[len-i] !=')':
        #         return False
        #     elif s[i] = '[' and s[len(s)-i] !=']':
        #         return False
        #     elif s[i] = '{' and s[len(s)-i] != '}':
        #     .......

        # solution 1
        # while '{}' in s or '()' in s or '[]' in s:
        #     s = s.replace('{}','')
        #     s = s.replace('[]','')
        #     s = s.replace('()','')
        # return s == ''
        # BAD  waste to much time


        # solution 2
        ls = []
        for i in range(len(s)):
            # 左括号入栈
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                ls.append(s[i])
                continue
            if len(ls) == 0:
                return False
            # 出栈比较是否匹配
            p = ls.pop()
            if (p == '(' and s[i] == ')') or ( p == '[' and s[i] == ']') or (p == '{' and s[i] == '}'):
                continue
            else:
                return False
        if len(ls) > 0 :
            return False
        return True
