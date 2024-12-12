import std.stdio;
import std.file;
import std.functional;
import std.array;
import std.algorithm;
import std.conv;
import std.math;

void main() {
    ulong[] data = readText("input").split(' ').map!(to!ulong).array();
    
    writefln("25: %s", data.map!(stone => memoize!countStones(stone, 25)).sum());
    writefln("75: %s", data.map!(stone => memoize!countStones(stone, 75)).sum());
}

ulong countStones(ulong stone, ulong blinks) {
    if(blinks == 0) {
        return 1;
    }

    if(stone == 0) {
        return memoize!countStones(1, blinks - 1);
    }

    ulong digitCount = to!string(stone).length;

    if(digitCount % 2 == 0) {
        ulong eDigitCount = 10.pow(digitCount / 2);
        ulong firstHalf = stone / eDigitCount;
        ulong secondHalf = stone % eDigitCount;
        return memoize!countStones(firstHalf, blinks - 1) + memoize!countStones(secondHalf, blinks - 1);
    }

    return memoize!countStones(stone * 2024, blinks - 1);
}