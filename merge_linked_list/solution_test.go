package merge_lists

import (
	"testing"
)

func Test1(t *testing.T) {
	arguments := make([]string, 0)
	arguments = append(arguments, "1", "3", "1", "2", "3", "2", "3", "4")
	res := solution(arguments)
	if res == nil {
		t.Fatalf("len(res) < 1")
	}

	if res.Value != 1 {
		t.Errorf("next: %d != 1 ", res.Value)
	}
	if res.Next == nil {
		t.Fatalf("len(res) < 2")
	}

	if res.Next.Value != 2 {
		t.Errorf("next: %d != 2 ", res.Next.Value)
	}

}
