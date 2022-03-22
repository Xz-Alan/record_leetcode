#include <iostream>
using namespace std;
#include <string>

class Solution
{
public:
    bool winnerOfGame(string colors)
    {
        int count_a = 0, count_b = 0, num_a = 0, num_b = 0;
        for (char ch : colors)
        {
            if (ch == 'A')
            {
                count_b = 0;
                count_a++;
                if (count_a >= 3)
                    num_a++;
            }
            else
            {
                count_a = 0;
                count_b++;
                if (count_b >= 3)
                    num_b++;
            }
        }
        return num_a > num_b;
    }
};