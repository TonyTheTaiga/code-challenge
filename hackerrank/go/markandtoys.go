func maximumToys(prices []int32, k int32) int32 {

    sort.Slice(prices, func(i, j int) bool { return prices[i] < prices[j]})
    fmt.Println(prices)
    var ret int32 = 0
    for _, price := range prices {
        k -= price
        if k > 0 {
            ret += 1
        } else { break }       
    } 
    return ret
}
