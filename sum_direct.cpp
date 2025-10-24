#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>

#include "sums.h"

void 
setup(int64_t N, int64_t A[])
{
   printf(" inside direct_sum problem_setup, N=%lld \n", N);
}

int64_t
sum(int64_t N, int64_t A[])
{
   printf(" inside direct_sum perform_sum, N=%lld \n", N);
   int64_t total = 0;
   for(int64_t i =0; i< N;i++){
      total += i;
   }
   return total;
}

