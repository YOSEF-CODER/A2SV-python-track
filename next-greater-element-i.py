class Solution:
	def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
		ans = [-1]*len(nums1)
		mono = []
		ind = defaultdict(int)
		for i, v in enumerate(nums1):
			ind[v] = i

		for i, v in enumerate(nums2):
			while mono and nums2[mono[-1]] < v:
				val = nums2[mono.pop()]
				if val in ind: ans[ind[val]] = v
			mono.append(i)
		return ans