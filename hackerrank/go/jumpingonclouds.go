func jumpingOnClouds(c []int32) int {
	temp := make([]int32, 0)
	steps := 0
	for _, value := range c {
		if value == 0 {
			temp = append(temp, value)
		} else {
			div := len(temp) / 2
			steps += div + 1
			temp = nil
		}
	}

	if len(temp) > 1 {
		div := len(temp) / 2
		steps += +div
	}

	return steps
}   