import sys
import pyperclip as pc

def pr(s):
    print(s)
    pc.copy(s)

def count_patterns(grid):
    p1 = 0  # Linear patterns ("XMAS" and "SAMX")
    p2 = 0  # X-MAS patterns

    R = len(grid)
    C = len(grid[0])

    for r in range(R):
        for c in range(C):
            # Linear patterns: Horizontal, vertical, and diagonal
            if c + 3 < C and grid[r][c] == 'X' and grid[r][c+1] == 'M' and grid[r][c+2] == 'A' and grid[r][c+3] == 'S':
                p1 += 1
            if r + 3 < R and grid[r][c] == 'X' and grid[r+1][c] == 'M' and grid[r+2][c] == 'A' and grid[r+3][c] == 'S':
                p1 += 1
            if r + 3 < R and c + 3 < C and grid[r][c] == 'X' and grid[r+1][c+1] == 'M' and grid[r+2][c+2] == 'A' and grid[r+3][c+3] == 'S':
                p1 += 1
            if c + 3 < C and grid[r][c] == 'S' and grid[r][c+1] == 'A' and grid[r][c+2] == 'M' and grid[r][c+3] == 'X':
                p1 += 1
            if r + 3 < R and grid[r][c] == 'S' and grid[r+1][c] == 'A' and grid[r+2][c] == 'M' and grid[r+3][c] == 'X':
                p1 += 1
            if r + 3 < R and c + 3 < C and grid[r][c] == 'S' and grid[r+1][c+1] == 'A' and grid[r+2][c+2] == 'M' and grid[r+3][c+3] == 'X':
                p1 += 1
            if r - 3 >= 0 and c + 3 < C and grid[r][c] == 'S' and grid[r-1][c+1] == 'A' and grid[r-2][c+2] == 'M' and grid[r-3][c+3] == 'X':
                p1 += 1
            if r - 3 >= 0 and c + 3 < C and grid[r][c] == 'X' and grid[r-1][c+1] == 'M' and grid[r-2][c+2] == 'A' and grid[r-3][c+3] == 'S':
                p1 += 1

            # X-MAS patterns
            if r + 2 < R and c + 2 < C:
                if (
                    grid[r][c] == 'M' and grid[r+1][c+1] == 'A' and grid[r+2][c+2] == 'S' and
                    grid[r+2][c] == 'M' and grid[r][c+2] == 'S'
                ):
                    p2 += 1
                if (
                    grid[r][c] == 'M' and grid[r+1][c+1] == 'A' and grid[r+2][c+2] == 'S' and
                    grid[r+2][c] == 'S' and grid[r][c+2] == 'M'
                ):
                    p2 += 1
                if (
                    grid[r][c] == 'S' and grid[r+1][c+1] == 'A' and grid[r+2][c+2] == 'M' and
                    grid[r+2][c] == 'M' and grid[r][c+2] == 'S'
                ):
                    p2 += 1
                if (
                    grid[r][c] == 'S' and grid[r+1][c+1] == 'A' and grid[r+2][c+2] == 'M' and
                    grid[r+2][c] == 'S' and grid[r][c+2] == 'M'
                ):
                    p2 += 1

    return p1, p2


def main():
    infile = sys.argv[1] if len(sys.argv) >= 2 else 'day4.txt'
    try:
        with open(infile, "r") as file:
            grid = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Error: Input file not found.")
        return

    p1, p2 = count_patterns(grid)
    pr(f"Linear patterns (p1): {p1}")
    pr(f"X-MAS patterns (p2): {p2}")


if __name__ == "__main__":
    main()
