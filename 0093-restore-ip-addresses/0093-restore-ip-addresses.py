class Solution:
    def restoreIpAddresses(self, s: str):
        result = []

        def backtrack(index, parts, path):
            if parts == 4:
                
                if index == len(s):
                    result.append(path[:-1]) 
                return

           
            for i in range(index, min(index + 3, len(s))):
                part = s[index:i+1]

                if len(part) > 1 and part[0] == '0':
                    continue

                if int(part) > 255:
                    continue
                backtrack(i + 1, parts + 1, path + part + ".")

        backtrack(0, 0, "")
        return result