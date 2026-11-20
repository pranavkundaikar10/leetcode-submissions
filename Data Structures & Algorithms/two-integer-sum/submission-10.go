func twoSum(nums []int, target int) []int {

	var seenMap = make(map[int]int, len(nums))

	for i, val := range nums {
		if idx, ok := seenMap[target - val]; ok {
			return []int{idx, i}
		}
		seenMap[val] = i
	}

	return nil
}
