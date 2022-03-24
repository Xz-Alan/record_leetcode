#include <iostream>
using namespace std;
#include <vector>
#include <algorithm>
class Solution
{
public:
    vector<vector<int>> imageSmoother(vector<vector<int>> &img)
    {
        int h = img.size(), w = img[0].size();
        vector<vector<int>> new_img(h, vector<int>(w));
        for (int i = 0; i < h; i++)
        {
            for (int j = 0; j < w; j++)
            {
                int total = 0, count = 0;
                for (int x = max(i - 1, 0); x < min(i + 2, h); x++)
                {
                    for (int y = max(j - 1, 0); y < min(j + 2, w); y++)
                    {
                        total += img[x][y];
                        count++;
                    }
                }
                new_img[i][j] = total / count;
            }
        }
        return new_img;
    }
};