// File: diverse_good.cpp
// Author: Code Quality Reviewer
// Description: Well-structured, well-documented code with clear naming
// Date: 2025-12-18

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/// Calculate the sum of array elements
/// @param arr Vector of integers to sum
/// @return Sum of all elements
int calculateSum(const vector<int>& arr) {
    int total = 0;
    for (int value : arr) {
        total += value;
    }
    return total;
}

/// Find the maximum element in array
/// @param arr Vector of integers
/// @return Maximum value
int findMax(const vector<int>& arr) {
    if (arr.empty()) {
        return 0;  // Handle empty array
    }
    return *max_element(arr.begin(), arr.end());
}

/// Sort array in ascending order
/// @param arr Reference to vector to sort
void sortArray(vector<int>& arr) {
    sort(arr.begin(), arr.end());
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    vector<int> numbers = {5, 2, 8, 1, 9};
    
    cout << "Sum: " << calculateSum(numbers) << endl;
    cout << "Max: " << findMax(numbers) << endl;
    
    sortArray(numbers);
    cout << "Sorted: ";
    for (int num : numbers) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}
