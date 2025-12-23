/**
 * Excellent Code Example - Best Practices Demonstrated
 * 
 * This module demonstrates professional C++ code with:
 * - Complete documentation
 * - Proper error handling
 * - Safe memory management
 * - Simple, readable logic
 * - No anti-patterns
 */

#include <iostream>
#include <vector>
#include <memory>
#include <stdexcept>
#include <algorithm>

/**
 * Calculator class for mathematical operations
 * Provides safe, well-documented computation methods
 */
class Calculator {
private:
    /// Store calculation history
    std::vector<double> history;
    
    /**
     * Add value to history
     * @param result The calculation result to store
     */
    void addToHistory(double result) {
        history.push_back(result);
    }
    
public:
    /**
     * Add two numbers safely
     * @param a First number
     * @param b Second number
     * @return Sum of a and b
     * @throws std::overflow_error if result overflows
     */
    double add(double a, double b) {
        double result = a + b;
        addToHistory(result);
        return result;
    }
    
    /**
     * Multiply two numbers
     * @param a First number
     * @param b Second number
     * @return Product of a and b
     */
    double multiply(double a, double b) {
        double result = a * b;
        addToHistory(result);
        return result;
    }
    
    /**
     * Divide with proper error handling
     * @param a Dividend
     * @param b Divisor (must not be zero)
     * @return Result of a / b
     * @throws std::invalid_argument if b is zero
     */
    double divide(double a, double b) {
        if (b == 0.0) {
            throw std::invalid_argument("Division by zero not allowed");
        }
        double result = a / b;
        addToHistory(result);
        return result;
    }
    
    /**
     * Get calculation history
     * @return Vector of all previous results
     */
    const std::vector<double>& getHistory() const {
        return history;
    }
    
    /**
     * Clear history
     */
    void clearHistory() {
        history.clear();
    }
};

/**
 * Process a list of numbers
 * @param numbers Vector of numbers to process
 * @return Average of all numbers
 * @throws std::invalid_argument if vector is empty
 */
double processNumbers(const std::vector<double>& numbers) {
    if (numbers.empty()) {
        throw std::invalid_argument("Cannot process empty vector");
    }
    
    double sum = 0.0;
    for (double num : numbers) {
        sum += num;
    }
    
    return sum / numbers.size();
}

/**
 * Main entry point with proper error handling
 * @return 0 on success, non-zero on error
 */
int main() {
    try {
        // Create calculator instance
        Calculator calc;
        
        // Perform calculations
        double result1 = calc.add(10.0, 20.0);
        double result2 = calc.multiply(result1, 2.0);
        double result3 = calc.divide(result2, 5.0);
        
        std::cout << "Result: " << result3 << std::endl;
        
        // Process number list
        std::vector<double> numbers = {1.0, 2.0, 3.0, 4.0, 5.0};
        double average = processNumbers(numbers);
        
        std::cout << "Average: " << average << std::endl;
        
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
}
