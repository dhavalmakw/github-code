#include <bits/stdc++.h>

using namespace std;

int mtrx[60][60], ms, sm, p;
bool r_f[60][60], c_f[60][60], resulted;

void solver(int rR, int cC, int m) {
    if (rR == ms && cC == ms + 1 && m == sm && !resulted) {
        resulted = true;
        cout << "Case #" << p << ": " << "POSSIBLE\n";
        for (int i = 1; i <= ms; ++i) {
            for (int j = 1; j <= ms; ++j) {
                cout << mtrx[i][j] << " ";
            }
            cout << "\n";
        }
        return;
    } else if (rR > ms) {
        return;
    } else if (cC > ms) {
        solver(rR + 1, 1, m);
    }
    for (int i = 1; i <= ms && !resulted; ++i) 
    {
        if (!r_f[rR][i] && !c_f[cC][i]) 
        {
            r_f[rR][i] = c_f[cC][i] = true;
            if (rR == cC) {
                m += i;
        }
        mtrx[rR][cC] = i;

        solver(rR, cC + 1, m);

        r_f[rR][i] = c_f[cC][i] = false;
        if (rR == cC) 
        {
            m -= i;
        }
        int sqr[rR][cC] = {0};
        }
    }
}

int main() {
    int TS;
    scanf(" %d", &TS);
    for (p = 1; p <= TS; ++p) {
        scanf(" %d %d", &ms, &sm);
        solver(1, 1, 0);
        if (!resulted) {
            cout << "Case #" << p << ": " << "IMPOSSIBLE\n";
        }
        resulted = false;
    }
    return 0;
}