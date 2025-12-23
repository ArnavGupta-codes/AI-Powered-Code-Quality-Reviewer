/**
 * Professional Data Analysis Module
 * 
 * This class provides comprehensive statistical analysis with proper
 * error handling, complete documentation, and follows Java best practices.
 * 
 * @author Code Quality Team
 * @version 1.0
 */

import java.util.*;
import java.util.stream.Collectors;

/**
 * Statistical calculator for numerical data analysis.
 * 
 * Provides safe, well-documented methods for computing statistics
 * with comprehensive error handling and input validation.
 */
public class ProfessionalDataAnalyzer {
    
    private final String name;
    private final List<Double> data;
    
    /**
     * Initialize the analyzer with a descriptive name.
     * 
     * @param name The name of this analyzer instance
     * @throws IllegalArgumentException if name is null or empty
     */
    public ProfessionalDataAnalyzer(String name) {
        if (name == null || name.trim().isEmpty()) {
            throw new IllegalArgumentException("Analyzer name cannot be null or empty");
        }
        this.name = name;
        this.data = new ArrayList<>();
    }
    
    /**
     * Add a single value to the dataset.
     * 
     * @param value The numerical value to add
     */
    public void addValue(double value) {
        data.add(value);
    }
    
    /**
     * Add multiple values to the dataset.
     * 
     * @param values Collection of values to add
     * @throws IllegalArgumentException if values is null or empty
     */
    public void addValues(Collection<Double> values) {
        if (values == null || values.isEmpty()) {
            throw new IllegalArgumentException("Values collection cannot be null or empty");
        }
        data.addAll(values);
    }
    
    /**
     * Calculate the mean (average) of all values.
     * 
     * @return The arithmetic mean
     * @throws IllegalStateException if no data has been added
     */
    public double calculateMean() {
        if (data.isEmpty()) {
            throw new IllegalStateException("Cannot calculate mean: no data available");
        }
        return data.stream()
            .mapToDouble(Double::doubleValue)
            .average()
            .orElse(0.0);
    }
    
    /**
     * Calculate the median value.
     * 
     * @return The median of all values
     * @throws IllegalStateException if no data has been added
     */
    public double calculateMedian() {
        if (data.isEmpty()) {
            throw new IllegalStateException("Cannot calculate median: no data available");
        }
        
        List<Double> sorted = data.stream()
            .sorted()
            .collect(Collectors.toList());
        
        int n = sorted.size();
        if (n % 2 == 1) {
            return sorted.get(n / 2);
        } else {
            return (sorted.get(n / 2 - 1) + sorted.get(n / 2)) / 2.0;
        }
    }
    
    /**
     * Calculate standard deviation.
     * 
     * @return The standard deviation of all values
     * @throws IllegalStateException if no data has been added
     */
    public double calculateStdDev() {
        if (data.isEmpty()) {
            throw new IllegalStateException("Cannot calculate standard deviation: no data available");
        }
        
        double mean = calculateMean();
        double variance = data.stream()
            .mapToDouble(v -> Math.pow(v - mean, 2))
            .average()
            .orElse(0.0);
        
        return Math.sqrt(variance);
    }
    
    /**
     * Get comprehensive statistics about the dataset.
     * 
     * @return Map containing count, min, max, mean, median, and stdDev
     * @throws IllegalStateException if no data has been added
     */
    public Map<String, Double> getStatistics() {
        if (data.isEmpty()) {
            throw new IllegalStateException("Cannot generate statistics: no data available");
        }
        
        Map<String, Double> stats = new LinkedHashMap<>();
        stats.put("count", (double) data.size());
        stats.put("min", Collections.min(data));
        stats.put("max", Collections.max(data));
        stats.put("mean", calculateMean());
        stats.put("median", calculateMedian());
        stats.put("stdDev", calculateStdDev());
        
        return stats;
    }
    
    /**
     * Get the name of this analyzer.
     * 
     * @return The analyzer name
     */
    public String getName() {
        return name;
    }
    
    /**
     * Clear all stored data.
     */
    public void clearData() {
        data.clear();
    }
    
    /**
     * Main method demonstrating proper usage.
     * 
     * @param args Command line arguments (unused)
     */
    public static void main(String[] args) {
        try {
            // Create analyzer instance
            ProfessionalDataAnalyzer analyzer = 
                new ProfessionalDataAnalyzer("MainAnalyzer");
            
            // Add sample data
            List<Double> sampleData = Arrays.asList(
                10.5, 20.3, 15.8, 25.1, 18.9, 22.4
            );
            analyzer.addValues(sampleData);
            
            // Display statistics
            Map<String, Double> stats = analyzer.getStatistics();
            System.out.println("Statistics for " + analyzer.getName() + ":");
            stats.forEach((key, value) -> 
                System.out.printf("%s: %.2f%n", key, value)
            );
            
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
            System.exit(1);
        }
    }
}
