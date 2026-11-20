func hasDuplicate(nums []int) bool {

	var seen = make(map[int]struct{})

	for i, num := range nums {
		fmt.Println(i, num)
		_, ok := seen[num]
		if ok {
			return true
		}
		seen[num] = struct{}{}
	}
    return false
}
