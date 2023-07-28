# some test cases have failed 
# failed testcase: 1/333
# expected: "0.(003)", Actual: "0.(0)"

class Solution:
    def find_repeating_pattern(self, st):
        trailing_to_pattern = ""
        while len(st) >=1:
            for i in range(1, (len(st) // 2) + 1):
                if st[:i] == st[i:i + len(st[:i])]:
                    return f"{trailing_to_pattern}({(st[:i])})"
            trailing_to_pattern += st[0]
            st = st[1:]
        return trailing_to_pattern    
            

    def fractionToDecimal(self, numerator: int, denominator: int):
        res = numerator / denominator
        if numerator % denominator == 0:
            return str(int(res))
        res = str(res)
        decimal_right = res.split(".")[1]
        decimal_left = res.split(".")[0]
        if len(decimal_right)>=15:
            decimal_right = decimal_right[:len(decimal_right) - 1]
        print(f"{decimal_right=}{decimal_left=}")
        pattern = ""
        pattern = self.find_repeating_pattern(decimal_right)
        out=""
        print(f"{decimal_left=}{pattern=}")
        if pattern:
            out = decimal_left + "."+pattern
        return out


obj = Solution()
res = obj.fractionToDecimal(1, 7)
print(res)
# class Solution:
#     def find_repeating_pattern(st):
#         trailing_to_pattern=""
#         while len(st)>1:
#             for i in range(1, (len(st)//2)+1):
#                 # print(st[:i],st[i:i+len(st[:i])])
#                 if st[:i]==st[i:i+len(st[:i])]:
#                     print(st[:i])
#                     return f"{trailing_to_pattern}(st[:i])"
#             st=st[1:]
#             trailing_to_pattern+=st[0]

#     def fractionToDecimal(self, numerator: int, denominator: int) :
#         res=numerator/denominator 
#         if numerator%denominator ==0:
#             return(str(int(res)))
#         res=str(res)
#         decimal_right=res.split(".")[1]
#         decimal_left=res.split(".")[0]
#         decimal_right=decimal_right[:len(decimal_right)-1]
#         print(f"{decimal_right=}")
#         pattern=""
#         pattern=self.find_repeating_pattern(decimal_right)
#         if pattern:
#             out=decimal_left+pattern
#         print(out)  
#         return out  

#         '''formatedResult = ('{:<0'+str((len(str(float(result)).split('.')[0])+50))+'}').format(float(result))
#         print(formatedResult)
#         return str(formatedResult).rstrip("0")'''
#         '''res= float(numerator/denominator)
#         if numerator%denominator==0:
#             res=int(res)
#         res=str(res)    
#         decimal_right=
#         is_repeat=False
#         while not is_repeat:
#             pattern=self.find_repeating_pattern()'''

    
    
    
# obj=Solution()
# res=obj.fractionToDecimal(7,12)
# print(res)
# print(7/12)

# def find_repeating_pattern(st):
#     while len(st)>1:
#         for i in range(1, (len(st)//2)+1):
#             # print(st[:i],st[i:i+len(st[:i])])
#             if st[:i]==st[i:i+len(st[:i])]:
#                 print(st[:i])
#                 return
#         st=st[1:]        
#     '''for i in range(1, (len(st)//2)+1):
#         if st[:i]*(len(st)//i)==st:
#             print(st[:i], "ok")'''

# find_repeating_pattern("214285714285714")

# print("abcd"[2:4]) #cd






