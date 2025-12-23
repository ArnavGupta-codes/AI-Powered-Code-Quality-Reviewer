#include <iostream>
#include <vector>
#include <algorithm>

/**
 * Calculate the sum of elements in a vector
 * @param numbers Vector containing numbers to sum
 * @return Sum of all elements
 */
int calculateSum(const std::vector<int>& numbers) {
    int sum = 0;
    for (int num : numbers) {
        sum += num;
    }
    return sum;
}

/**
 * Find the maximum element in a vector
 * @param numbers Vector to search
 * @return Maximum element value
 */
int findMaximum(const std::vector<int>& numbers) {
    if (numbers.empty()) {
        return 0;
    }
    return *std::max_element(numbers.begin(), numbers.end());
}

/**
 * Calculate average of vector elements
 * @param numbers Vector containing numbers
 * @return Average value
 */
double calculateAverage(const std::vector<int>& numbers) {
    if (numbers.empty()) {
        return 0.0;
    }
    return calculateSum(numbers) / static_cast<double>(numbers.size());
}

int main() {
    // Create sample data
    std::vector<int> data = {10, 20, 30, 40, 50};
    
    // Calculate statistics
    int sum = calculateSum(data);
    int maximum = findMaximum(data);
    double average = calculateAverage(data);
    
    // Display results
    std::cout << "Sum: " << sum << std::endl;
    std::cout << "Maximum: " << maximum << std::endl;
    std::cout << "Average: " << average << std::endl;
    
    return 0;
}
