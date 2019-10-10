import "fmt"

// Complete the countSwaps function below.
func countSwaps(a []int32) {
	var count int32 = 0
	var first int32
	var last int32
	var n int = len(a)

	for i := 0; i < n; i++ {
		for j := 0; j < n-1; j++ {
			if a[j] > a[j+1] {
				count++
				temp := a[j]
				a[j] = a[j+1]
				a[j+1] = temp
			}
		}
	}

	first = a[0]
	last = a[n-1]

	fmt.Print(fmt.Sprintf("Array is sorted in %d swaps.\n"+
		"First Element: %d\n"+
		"Last Element: %d", count, first, last))
}
