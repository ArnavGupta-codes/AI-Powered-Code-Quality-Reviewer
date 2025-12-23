"""
Professional Data Processing Module
================================

This module provides well-designed, thoroughly documented, and secure
data processing functionality following Python best practices.

Author: Code Quality Team
Version: 1.0
"""

import logging
from typing import List, Optional
from dataclasses import dataclass
from enum import Enum

# Configure logging properly
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DataProcessor:
    """
    Processes numerical data with comprehensive error handling.
    
    This class provides safe, well-documented methods for data manipulation
    and statistics calculation with proper exception handling.
    """
    
    def __init__(self, name: str = "DefaultProcessor") -> None:
        """
        Initialize the data processor.
        
        Args:
            name: Descriptive name for this processor instance
            
        Raises:
            ValueError: If name is empty
        """
        if not name:
            raise ValueError("Processor name cannot be empty")
        self.name = name
        self.data: List[float] = []
        logger.info(f"Initialized {self.name}")
    
    def add_value(self, value: float) -> None:
        """
        Add a single value to the dataset.
        
        Args:
            value: The numerical value to add
            
        Raises:
            TypeError: If value is not a number
        """
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected number, got {type(value)}")
        self.data.append(float(value))
    
    def add_values(self, values: List[float]) -> None:
        """
        Add multiple values to the dataset.
        
        Args:
            values: List of numerical values to add
            
        Raises:
            TypeError: If any value is not a number
            ValueError: If list is empty
        """
        if not values:
            raise ValueError("Cannot add empty value list")
        
        for val in values:
            self.add_value(val)
    
    def calculate_mean(self) -> float:
        """
        Calculate the mean of all values.
        
        Returns:
            The arithmetic mean of stored values
            
        Raises:
            ValueError: If no data has been added
        """
        if not self.data:
            raise ValueError("Cannot calculate mean: no data available")
        
        return sum(self.data) / len(self.data)
    
    def calculate_median(self) -> float:
        """
        Calculate the median of all values.
        
        Returns:
            The median value
            
        Raises:
            ValueError: If no data has been added
        """
        if not self.data:
            raise ValueError("Cannot calculate median: no data available")
        
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        
        if n % 2 == 1:
            return sorted_data[n // 2]
        else:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2.0
    
    def get_statistics(self) -> Optional[dict]:
        """
        Get comprehensive statistics about the data.
        
        Returns:
            Dictionary with mean, median, min, max, and count.
            Returns None if no data available.
        """
        if not self.data:
            logger.warning(f"{self.name}: No data for statistics")
            return None
        
        return {
            'count': len(self.data),
            'mean': self.calculate_mean(),
            'median': self.calculate_median(),
            'min': min(self.data),
            'max': max(self.data),
        }
    
    def clear_data(self) -> None:
        """Clear all stored data."""
        self.data = []
        logger.info(f"{self.name}: Data cleared")


def process_file(filename: str) -> Optional[DataProcessor]:
    """
    Load and process data from a file.
    
    Args:
        filename: Path to the file containing numerical data (one per line)
        
    Returns:
        DataProcessor instance with loaded data, or None if file not found
        
    Raises:
        ValueError: If file contains non-numerical data
    """
    processor = DataProcessor(f"FileProcessor({filename})")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    value = float(line.strip())
                    processor.add_value(value)
                except ValueError:
                    raise ValueError(
                        f"Invalid number at line {line_num}: {line.strip()}"
                    )
        
        logger.info(f"Loaded {len(processor.data)} values from {filename}")
        return processor
        
    except FileNotFoundError:
        logger.error(f"File not found: {filename}")
        return None
    except Exception as e:
        logger.error(f"Error processing file: {e}")
        raise


def main() -> int:
    """
    Main entry point demonstrating proper usage.
    
    Returns:
        0 on success, 1 on failure
    """
    try:
        # Create processor
        processor = DataProcessor("MainProcessor")
        
        # Add sample data
        sample_data = [10.5, 20.3, 15.8, 25.1, 18.9, 22.4]
        processor.add_values(sample_data)
        
        # Get and display statistics
        stats = processor.get_statistics()
        if stats:
            logger.info(f"Statistics: {stats}")
            print(f"Mean: {stats['mean']:.2f}")
            print(f"Median: {stats['median']:.2f}")
            print(f"Range: {stats['min']:.2f} - {stats['max']:.2f}")
        
        return 0
        
    except Exception as e:
        logger.error(f"Application error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
