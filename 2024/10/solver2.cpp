#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

vector<vector<int>> parse_input(string filename);
vector<pair<size_t, size_t>> find_trailheads(vector<vector<int>> &grid);
int calculate_score(pair<size_t, size_t> &head, vector<vector<int>> &grid);

int main()
{
    vector<vector<int>> grid = parse_input("input");
    vector<pair<size_t, size_t>> trailheads = find_trailheads(grid);
    int score = 0;
    for (pair<size_t, size_t> trailhead : trailheads)
    {
        score += calculate_score(trailhead, grid);
    }
    cout << score << endl;
}

vector<vector<int>> parse_input(string filename)
{
    vector<vector<int>> grid;
    ifstream ifs(filename);
    string line;

    while (getline(ifs, line))
    {
        vector<int> row;
        for (size_t j = 0, n = line.length(); j < n; j++)
        {
            row.push_back(line[j] - '0');
        }
        grid.push_back(row);
    }
    ifs.close();
    return grid;
}

vector<pair<size_t, size_t>> find_trailheads(vector<vector<int>> &grid)
{
    vector<pair<size_t, size_t>> trailheads;
    for (size_t y = 0, n = grid.size(); y < n; y++)
    {
        for (size_t x = 0, m = grid[0].size(); x < m; x++)
        {
            if (grid[y][x] == 0)
            {
                trailheads.push_back(pair(x, y));
            }
        }
    }
    return trailheads;
}

int calculate_score(pair<size_t, size_t> &head, vector<vector<int>> &grid)
{
    size_t x = head.first;
    size_t y = head.second;
    if (grid[y][x] == 9)
    {
        return 1;
    }
    pair<size_t, size_t> ds[4] = {
        pair(x + 1, y),
        pair(x - 1, y),
        pair(x, y + 1),
        pair(x, y - 1),
    };

    int sum = 0;

    for (pair<size_t, size_t> coords: ds)
    {
        size_t nx = coords.first;
        size_t ny = coords.second;
        if (0 <= nx && nx < grid[0].size() && 0 <= ny && ny < grid.size() && grid[ny][nx] == grid[y][x] + 1)
        {
            sum += calculate_score(coords, grid);
        }
    }

    return sum;
}