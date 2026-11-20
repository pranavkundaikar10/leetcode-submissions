func isAnagram(s string, t string) bool {

	if len(s) != len(t) {
		return false
	}

	var counts [26]int

	for i, val := range s {
		counts[val - 'a']++
		counts[t[i] - 'a']--
	}

	for _, val:= range counts {
		if val != 0 {
			return false
		}
	}

	return true

}
