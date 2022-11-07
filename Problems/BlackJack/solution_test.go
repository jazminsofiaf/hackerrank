package blackjack
import (
	"testing"
)

func Test1(t *testing.T) {
	arguments := make([]string, 0)
	arguments = append(arguments, "four", "ace", "ten")
	res := blackjackHighest(arguments)
	if res != "below ten" {
		t.Fatalf("res %s!= below ten", res)
	}
}
func Test2(t *testing.T) {
	arguments := make([]string, 0)
	arguments = append(arguments, "two", "three", "ace", "king")
	res := blackjackHighest(arguments)
	if res != "below king" {
		t.Fatalf("res %s!= below king", res)
	}
}
func Test3(t *testing.T) {
	arguments := make([]string, 0)
	arguments = append(arguments, "four", "ten", "king")
	res := blackjackHighest(arguments)
	if res != "above king" {
		t.Fatalf("res %s!= above king", res)
	}
}

func Test4(t *testing.T) {
	arguments := make([]string, 0)
	arguments = append(arguments, "ace", "queen")
	res := blackjackHighest(arguments)
	if res != "blackjack ace" {
		t.Fatalf("res %s!=  blackjack ace", res)
	}
}
