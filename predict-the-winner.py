class Solution:

    def PredictTheWinner(self, nums: List[int]) -> bool:
        def playerWinner(left,right,player1):
            if left==right:
                if player1:
                    return [nums[left],0]
                else:
                    return [0,nums[right]]
            else:
                if player1:
                    resL=playerWinner(left+1,right,False)
                    resR=playerWinner(left,right-1,False)
                    resL[0]+=nums[left]
                    resR[0]+=nums[right]

                    if resL[0]>resR[0]:
                        return resL
                    else:
                        return resR
                else:
                    resL=playerWinner(left+1,right,True)
                    resR=playerWinner(left,right-1,True)
                    resL[1]+=nums[left]
                    resR[1]+=nums[right]

                    if resL[1]>resR[1]:
                        return resL
                    else:
                        return resR
       

        score = playerWinner(0, len(nums)-1, True)
        return score[0] >= score[1]