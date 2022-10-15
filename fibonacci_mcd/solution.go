package fibonacci_mcd

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
	arguments := make([]string, 0)
	scanner := bufio.NewScanner(os.Stdin)
	if err := scanner.Err(); err != nil {
		log.Println(err)
		return
	}
	for scanner.Scan() {
		arguments = append(arguments, scanner.Text())
	}
	solution(arguments)
}

//solution returns start and end of substring
func solution(arguments []string) map[int][2]int {
	mapResult := make(map[int][2]int, 0)
	if len(arguments) < 1 {
		log.Println("error args len < 1")
		return mapResult
	}

	size, err := strconv.Atoi(arguments[0])
	if err != nil {
		log.Println("error parsing pattern size")
		return mapResult
	}

	if len(arguments) < size+1 {
		log.Println("error args len < k")
		return mapResult
	}

	for i := 1; i < size+1; i++ {
		k, err := strconv.Atoi(arguments[i])
		if err != nil {
			log.Println("error parsing pattern k")
			return mapResult
		}
		if val, ok := mapResult[k]; ok {
			if len(val) > 1 {
				fmt.Printf("%d %d\n", val[0], val[1])
				continue
			}
		}
		fn, mcd := getFnMCD(k, 1, 1)
		fmt.Printf("%d %d\n", fn, mcd)
		row := [2]int{fn, mcd}
		mapResult[k] = row
	}
	return mapResult
}

//O(2^n)
func getFnMCD(k int, prevFn int, fn int) (int, int) {
	thisFn := prevFn + fn
	divisor := getMaxCommonDivisor(k, thisFn)
	if divisor != 1 {
		return thisFn, divisor
	}
	return getFnMCD(k, fn, thisFn)
}

//O(log(min(a,b)))
func getMaxCommonDivisor(n1 int, n2 int) int {
	a := n1
	b := n2
	if n2 > n1 {
		a = n2
		b = n1
	}
	for b != 0 {
		aux := b
		b = a % b
		a = aux
	}
	return a
}
