#include <bits/stdc++.h>
using namespace std;
void print_vector(vector<auto> v){
   cout << "[";
   for(int i = 0; i<v.size(); i++){
      cout << v[i] << ", ";
   }
   cout << "]"<<endl;
}
class Solution {
   public:
   vector<int> numOfBurgers(int t, int c) {
      vector <int> ans;
      if(t % 2 != 0 || c > t/2 || t > c*4)return ans;
      int x = (4 * c - t) / 2;
      int y = ( t - (2 * x) )/ 4;
      ans.push_back(y);
      ans.push_back(x);
      return ans;
   }
};
main(){
   Solution ob;
   print_vector(ob.numOfBurgers(16,7));
}