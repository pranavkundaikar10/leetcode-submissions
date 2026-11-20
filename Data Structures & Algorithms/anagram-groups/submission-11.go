func groupAnagrams(strs []string) [][]string {

	var res = make(map[[26]int][]string, len(strs))

	for _, s := range strs {
		var counts [26]int
		for _, c := range s {
			counts[c-'a']++
		}
		res[counts] = append(res[counts], s)
	}

	var result = make([][]string, 0, len(res))

	for _, group := range res {
		result = append(result, group)
	}

	return result
}