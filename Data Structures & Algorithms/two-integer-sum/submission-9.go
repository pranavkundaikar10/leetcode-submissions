func twoSum(nums []int, target int) []int {

	var seenMap = make(map[int]int)

	for i, val := range nums {
		if idx, ok := seenMap[target - val]; ok {
			return []int{idx, i}
		}
		seenMap[val] = i
	}

	return []int{0, 0}
    
}
