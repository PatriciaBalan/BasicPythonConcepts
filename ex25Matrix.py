class Solution:
   def endPoints(self, matrix, m, n):
       direction={
           "up":"right",
           "right":"down",
           "down":"left",
           "left":"up",
       }
       i,j=0,0
       curr="right"
       while True:
           if matrix[i][j]==0:
               if curr=="left":
                   j-=1
                   if j<0:
                       return [i,j+1]
               elif curr=="right":
                   j+=1
                   if j>n-1:
                       return [i,j-1]
               elif curr=="down":
                   i+=1
                   if i>m-1:
                       return [i-1,j]
               elif curr=="up":
                   i-=1
                   if i<0:
                       return [i+1,j]
           else:
               matrix[i][j]=0
               curr=direction[curr]

s = Solution()
print(s.endPoints(0,0,0))
