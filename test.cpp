#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

const vector<pair<int, int>> directions = {
    {1, 1}, {1, -1}, {-1, 1}, {-1, -1}}; // Diagonal directions for the "X" pattern

bool searchXMAS(const vector<string> &grid, int x, int y, int dx, int dy)
{
    int n = grid.size();
    int m = grid[0].size();

    // Ensure we don't go out of bounds
    if (x - dx >= 0 && x + 2 * dx < n && y - dy >= 0 && y + 2 * dy < m)
    {
        // Check the forward "M.A.S" pattern
        if (grid[x][y] == 'M' &&
            grid[x + dx][y + dy] == 'A' &&
            grid[x + 2 * dx][y + 2 * dy] == 'S' &&
            grid[x - dx][y - dy] == 'S' &&
            grid[x - 2 * dx][y - 2 * dy] == 'M')
        {
            return true;
        }

        // Check the reverse "S.A.M" pattern
        if (grid[x][y] == 'S' &&
            grid[x + dx][y + dy] == 'A' &&
            grid[x + 2 * dx][y + 2 * dy] == 'M' &&
            grid[x - dx][y - dy] == 'M' &&
            grid[x - 2 * dx][y - 2 * dy] == 'S')
        {
            return true;
        }
    }

    return false;
}

int countXMAS(const vector<string> &grid)
{
    int count = 0;
    int n = grid.size();
    int m = grid[0].size();

    // Iterate through every cell in the grid
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            // Check all four diagonal directions for the X-MAS pattern
            for (const auto &dir : directions)
            {
                if (searchXMAS(grid, i, j, dir.first, dir.second))
                {
                    count++;
                }
            }
        }
    }

    return count;
}

int main()
{
    ifstream inputFile("D:/Advent of Code/day4.txt");
    string line;
    vector<string> grid;
    if (!inputFile)
    {
        cerr << "Error: Unable to open input file." << endl;
        return 1;
    }

    // Read the grid from the input file
    while (getline(inputFile, line))
    {
        grid.push_back(line);
    }

    inputFile.close();

    // Count the occurrences of "X-MAS" and print the result
    int totalOccurrences = countXMAS(grid);

    cout << "Total occurrences of X-MAS: " << totalOccurrences << endl;

    return 0;
}
