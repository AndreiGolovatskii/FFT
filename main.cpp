#include <bits/stdc++.h>
#include "fast_fourier_transform.cpp"

using namespace std;

int main() {
  vector<long long> a, b;
  a = {1, 2, 3, 4, 5};
  b = {1, 2, 3, 4, 5};

  vector<long long> res = multiply_polynomials(a, b);
  for(auto i : res) {
    cout << i << " ";
  }
}