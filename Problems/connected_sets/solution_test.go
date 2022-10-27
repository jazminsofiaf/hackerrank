
import (
    "bufio"
    "fmt"
    "log"
    "os"
    "strconv"
    "strings"
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
func solution(arguments []string) []int {
    result := make([]int, 0)
    if len(arguments) < 1 {
        log.Println("error args len < 1")
        return result
    }

    _, err := strconv.Atoi(arguments[0])
    if err != nil {
        log.Println("error parsing pattern size")
        return result
    }
    i := 1
    for i < len(arguments) {
        n, err := strconv.Atoi(arguments[i])
        if err != nil {
            log.Println("error parsing pattern n")
            return result
        }
        matrix := make(map[int]map[int]int)
        visited := make(map[int]map[int]bool)
        j := i + 1
        r := 0
        for r < n {
            rowValues := make(map[int]int)
            rowVisited := make(map[int]bool)
            lineList := strings.Split(arguments[j], " ")
            for c := 0; c < n; c++ {
                val, err := strconv.Atoi(lineList[c])
                if err != nil {
                    log.Println("error parsing matrix val")
                    continue
                }
                rowValues[c] = val
                rowVisited[c] = false
            }
            matrix[r] = rowValues
            visited[r] = rowVisited
            r++
            j++
        }
        total := getNeighborsHoods(n, matrix, visited)
        result = append(result, total)
        fmt.Println(total)
        i = j
    }
    return result
}

func getNeighborsHoods(n int, matrix map[int]map[int]int, visited map[int]map[int]bool) int {
    neighborhoods := 0
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if visited[i][j] {
                continue
            }
            if matrix[i][j] == 1 {
                neighborhoods += 1
                visited = getNeighbors(n, matrix, visited, i, j)
            }
            log.Printf(" visited %d %d\n", i, j)
            visited[i][j] = true
        }
    }
    return neighborhoods
}

func getNeighbors(n int, matrix map[int]map[int]int, visited map[int]map[int]bool, i int, j int) map[int]map[int]bool {
    if visited[i][j] {
        return visited
    }
    log.Printf(" --> visited %d %d\n", i, j)
    visited[i][j] = true
    if matrix[i][j] == 0 {
        return visited
    }
    if i-1 >= 0 {
        log.Printf("NORTE(%d %d) %d %d", i, j, i-1, j)
        visited = getNeighbors(n, matrix, visited, i-1, j)
    }
    if i+1 < n {
        log.Printf("SUR(%d %d) %d %d", i, j, i+1, j)
        visited = getNeighbors(n, matrix, visited, i+1, j)
    }
    if j+1 < n {
        log.Printf("ESTE(%d %d) %d %d", i, j, i, j+1)
        visited = getNeighbors(n, matrix, visited, i, j+1)
    }
    if j-1 >= 0 {
        log.Printf("OESTE(%d %d) %d %d", i, j, i, j-1)
        visited = getNeighbors(n, matrix, visited, i, j-1)
    }

    if i+1 < n && j+1 < n {
        //SE
        log.Printf("SE(%d %d) %d %d", i, j, i+1, j+1)
        visited = getNeighbors(n, matrix, visited, i+1, j+1)
    }

    if i+1 < n && j-1 >= 0 {
        //NE
        log.Printf("NE(%d %d) %d %d", i, j, i+1, j-1)
        visited = getNeighbors(n, matrix, visited, i+1, j-1)
    }

    if i-1 >= 0 && j+1 < n {
        //S0
        log.Printf("SO(%d %d) %d %d", i, j, i-1, j+1)
        visited = getNeighbors(n, matrix, visited, i-1, j+1)
    }

    if i-1 >= 0 && j-1 >= 0 {
        //N0
        log.Printf("NO(%d %d) %d %d", i, j, i-1, j-1)
        visited = getNeighbors(n, matrix, visited, i-1, j-1)
    }
    return visited
}