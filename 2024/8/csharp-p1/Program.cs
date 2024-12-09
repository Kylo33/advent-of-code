
using System.Dynamic;

public class Program
{
    public static void Main()
    {
        string[] lines = File.ReadAllLines("input");
        Dictionary<char, IList<Tuple<int, int>>> frequencies = [];
        for(var y = 0; y < lines.Length; y++)
        {
            var line = lines[y];
            for(var x = 0; x < line.Length; x++)
            {
                var c = line[x];
                if (c != '.')
                {
                    IList<Tuple<int, int>> list;
                    if (!frequencies.ContainsKey(c))
                    {
                        list = [];
                    }
                    else
                    {
                        list = frequencies[c];
                    }
                    list.Add(new Tuple<int, int>(x, y));
                    frequencies[c] = list;
                }
            }
        }

        ISet<Tuple<int, int>> antinodes = new HashSet<Tuple<int, int>>();
        foreach (var frequency in frequencies)
        {
            foreach (var nodeA in frequency.Value)
            {
                foreach (var nodeB in frequency.Value)
                {
                    if (nodeA == nodeB)
                    {
                        continue;
                    }
                    int dx = nodeB.Item1 - nodeA.Item1;
                    int dy = nodeB.Item2 - nodeA.Item2;
                    antinodes.Add(new Tuple<int, int>(nodeB.Item1 + dx, nodeB.Item2 + dy));
                    antinodes.Add(new Tuple<int, int>(nodeA.Item1 - dx, nodeA.Item2 - dy));
                }
            }
        }
        int count = 0;
        foreach (var antinode in antinodes)
        {
            if (0 <= antinode.Item2 && antinode.Item2 < lines.Length && 0 <= antinode.Item1 && antinode.Item1 < lines[0].Length)
            {
                count++;
            }
        }
        Console.WriteLine(count);
    }
}