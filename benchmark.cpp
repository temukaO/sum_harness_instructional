//
// (C) 2022-2023, E. Wes Bethel
// benchmark-* harness for running different versions of the sum study
//    over different problem sizes
//
// usage: no command line arguments
// set problem sizes, block sizes in the code below

#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>

#include "sums.h"

/* The benchmarking program */
int main(int argc, char** argv) 
{
   std::cout << std::fixed << std::setprecision(2);

#define MAX_PROBLEM_SIZE 1 << 28  //  256M
   std::vector<int64_t> problem_sizes{ MAX_PROBLEM_SIZE >> 5, MAX_PROBLEM_SIZE >> 4, MAX_PROBLEM_SIZE >> 3, MAX_PROBLEM_SIZE >> 2, MAX_PROBLEM_SIZE >> 1, MAX_PROBLEM_SIZE};
   
   int64_t *A = (int64_t *)malloc(sizeof(int64_t) * MAX_PROBLEM_SIZE);

   int n_problems = problem_sizes.size();

   /* For each test size */
   for (int64_t n : problem_sizes) 
   {
      int64_t t;
      printf("Working on problem size N=%ld \n", n);

      // invoke user code to set up the problem
      setup(n, &A[0]);

      // insert your timer code here
      auto start_time = std::chrono::high_resolution_clock::now();
      // invoke method to perform the sum
      t = sum(n, &A[0]);

      // insert your end timer code here, and print out elapsed time for this problem size
      auto end_time = std::chrono::high_resolution_clock::now();
      auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);
      double elapsed_time_seconds = duration.count() / 1000000.0;
      printf(" Elapsed time = %.6f seconds\n", elapsed_time_seconds);

      printf(" Sum result = %ld \n",t);

   } // end loop over problem sizes
}

// EOF
