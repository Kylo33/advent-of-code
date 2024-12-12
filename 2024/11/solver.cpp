#include <iostream>
#include <unordered_map>
#include <fstream>

using namespace std;

unordered_map<long, long> parse_input(string filename);
unordered_map<long, long> blink(unordered_map<long, long> &stones);

int main()
{
    unordered_map<long, long> stones = parse_input("input");
    for (short i = 0; i < 75; i++)
    {
        stones = blink(stones);
    }

    long total = 0;
    for (auto const [_, count] : stones)
    {
        total += count;
    }
    cout << total << endl;
}

unordered_map<long, long> parse_input(string filename)
{
    unordered_map<long, long> result;

    ifstream ifs(filename);
    long num;
    while (ifs >> num)
    {
        result[num]++;
    }

    return result;
}

unordered_map<long, long> blink(unordered_map<long, long> &stones)
{
    unordered_map<long, long> new_stones;
    for (auto const [value, count] : stones)
    {
        if (value == 0)
        {
            new_stones[1] += count;
            continue;
        }

        string val_str = to_string(value);
        size_t slen = val_str.length();
        if (slen % 2 == 0)
        {
            new_stones[stol(val_str.substr(0, slen / 2))] += count;
            new_stones[stol(val_str.substr(slen / 2, slen / 2))] += count;
        }
        else
        {
            new_stones[value * 2024] += count;
        }
    }
    return new_stones;
}