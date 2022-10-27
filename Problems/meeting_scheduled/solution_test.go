package meeting_scheduled

import (
	"testing"
)

func Test1(t *testing.T) {
	arguments := make([]string, 0)
	arguments = append(arguments, "5 120", "16 00 17 00", "10 30 14 30", "20 45 22 15", "10 00 13 15", "09 00 11 00")
	res := solution(arguments)
	if len(res) < 2 {
		t.Fatalf("len(res) < 2")
	}
	if res[0][0] != 0 || res[0][1] != 0 || res[0][2] != 9 || res[0][3] != 0 {
		t.Errorf("slot 00 00 09 00 != %d %d %d %d", res[0][0], res[0][1], res[0][2], res[0][3])
	}
	if res[1][0] != 17 || res[1][1] != 0 || res[1][2] != 20 || res[1][3] != 45 {
		t.Errorf("slot 17 00 20 45 != %d %d %d %d", res[0][0], res[0][1], res[0][2], res[0][3])
	}
}

func Test2(t *testing.T) {
	arguments := make([]string, 0)
	arguments = append(arguments, "8 60", "08 00 10 15", "22 00 23 15", "17 00 19 00", "07 00 09 45", "09 00 13 00", "16 00 17 45", "12 00 13 30", "11 30 12 30")
	res := solution(arguments)
	if len(res) < 3 {
		t.Fatalf("len(res) < 3")
	}
	if res[0][0] != 0 || res[0][1] != 0 || res[0][2] != 7 || res[0][3] != 0 {
		t.Errorf("slot 00 00 07 00 != %d %d %d %d", res[0][0], res[0][1], res[0][2], res[0][3])
	}
}

func Test3(t *testing.T) {
	arguments := make([]string, 0)
	arguments = append(arguments, "1 1", "00 00 23 58")
	res := solution(arguments)
	if len(res) < 1 {
		t.Fatalf("len(res) < 1")
	}
	if res[0][0] != 23 || res[0][1] != 58 || res[0][2] != 23 || res[0][3] != 59 {
		t.Errorf("slot 23 58 23 59 != %d %d %d %d", res[0][0], res[0][1], res[0][2], res[0][3])
	}
}

func Test4(t *testing.T) {
	arguments := make([]string, 0)
	arguments = append(arguments, "1 1", "00 01 23 59")
	res := solution(arguments)
	if len(res) < 1 {
		t.Fatalf("len(res) < 1")
	}
	if res[0][0] != 0 || res[0][1] != 0 || res[0][2] != 0 || res[0][3] != 1 {
		t.Errorf("slot 00 00 00 001!= %d %d %d %d", res[0][0], res[0][1], res[0][2], res[0][3])
	}
}

func Test5(t *testing.T) {
	arguments := make([]string, 0)
	arguments = append(arguments, "5 45", "12 15 15 15", "16 00 18 00", "22 00 23 00", "20 15 22 15", "21 00 23 00")
	res := solution(arguments)
	if len(res) < 4 {
		t.Fatalf("len(res) < 1")
	}
	//00 00 12 15
	//15 15 16 00
	//18 00 20 15
	//23 00 00 00
	if res[0][0] != 0 || res[0][1] != 0 || res[0][2] != 12 || res[0][3] != 15 {
		t.Errorf("slot 00 00 12 15!= %d %d %d %d", res[0][0], res[0][1], res[0][2], res[0][3])
	}
}
