func hasDuplicate(nums []int) bool {

	var seen = make(map[int]struct{})

	for _, val := range nums {
		
		if _, ok := seen[val]; ok {
			return true
		}
		seen[val] = struct{}{}
	}

    return false
}
