import pandas as pd

def read_excel_file(filepath):
  """
  Reads an Excel file (XLS, XLSX) or CSV file and returns a Pandas DataFrame.

  Args:
      filepath (str): Path to the Excel or CSV file.

  Returns:
      pandas.DataFrame: DataFrame containing the data from the file.

  Raises:
      ValueError: If the file format is not supported (e.g., unsupported binary format).
  """

  # Check for file extension (case-insensitive)
  if filepath.lower().endswith(".xls") or filepath.lower().endswith(".xlsx"):
    try:
      # Use pandas.read_excel for XLS and XLSX files
      return pd.read_excel(filepath)
    except pd.errors.ParserError:
      raise ValueError("Error parsing Excel file. Check file format.")
  elif filepath.lower().endswith(".csv"):
    # Use pandas.read_csv for CSV files
    return pd.read_csv(filepath)
  else:
    raise ValueError("Unsupported file format. Please provide XLS, XLSX, or CSV file.")

# Example usage
filepath = "your_file.xlsx"  # Replace with your actual file path
try:
  data = read_excel_file(filepath)
  print(data)
except ValueError as e:
  print(f"Error: {e}")
