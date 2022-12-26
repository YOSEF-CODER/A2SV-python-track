class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        li=[]
        li.append(celsius+273.15)
        li.append(celsius * 1.80 + 32.00)
        return li