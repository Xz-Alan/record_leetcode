#include <iostream>
using namespace std;
class Solution
{
public:
    bool reachingPoints(int sx, int sy, int tx, int ty)
    {
        while (tx > sx && ty > sy && tx != ty)
        {
            if (sx == tx && sy == ty)
                return true;
            if (tx < ty)
                ty %= tx;
            else
                tx %= ty;
        }
        if (sx == tx && sy == ty)
            return true;
        else if (sx == tx)
            return ty > sy && (ty - sy) % tx == 0;
        else if (sy == ty)
            return tx > sx && (tx - sx) % ty == 0;
        return false;
    }
};