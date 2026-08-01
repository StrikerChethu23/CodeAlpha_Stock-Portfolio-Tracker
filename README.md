STOCK PORTFOLIO TRACKER - PROJECT REPORT


 1. INTRODUCTION
A simple stock portfolio tracking system that allows users to:
- Input stock holdings manually
- Calculate total investment and current value
- Track profit/loss in both amount and percentage
- Export data to CSV or text files

 2. OBJECTIVES
- ✅ Accept user input for stock symbols, shares, and buy prices
- ✅ Use hardcoded dictionary for current stock prices
- ✅ Calculate total investment value
- ✅ Display detailed portfolio summary
- ✅ Optionally save results to CSV or text files

 3. TECHNOLOGIES USED
- **Language:** Python 3.x
- **Libraries:** 
  - csv (built-in)
  - os (built-in)
  - datetime (built-in)
- **Concepts:** Dictionaries, Functions, File I/O, Exception Handling

 4. KEY FEATURES

 4.1 Hardcoded Stock Prices
- 10 predefined stocks with current prices
- Easy to modify or expand

 4.2 Input Validation
- Validates stock symbols exist
- Ensures positive numbers for shares and prices
- Handles invalid input gracefully

 4.3 Portfolio Summary
- Individual stock breakdown
- Totals for investment, current value, profit/loss
- Color-coded indicators (🟢/🔴/⚪)

 4.4 File Export
- CSV format for spreadsheet software
- Text format for easy reading
- Timestamp-based file naming

 5. CODE EXPLANATION (Key Functions)
 `input_stock_portfolio()`
**Purpose:** Interactive portfolio building
- Displays available stocks
- Takes user input for symbol, shares, buy price
- Allows adding multiple stocks
 `calculate_portfolio_summary()`
**Purpose:** Computes portfolio statistics
- Calculates individual stock metrics
- Aggregates totals
- Returns structured summary dictionary
 `display_portfolio_summary()`
**Purpose:** Formats and displays results
- Table format with aligned columns
- Color indicators for profit/loss
- Clear totals section
-  `export_to_csv()` / `export_to_text()`
**Purpose:** Save portfolio data
- Uses timestamp for unique filenames
- Handles formatting for readability
- Includes error handling

 6. DATA FLOW
User Input → Input Validation → Portfolio Dictionary →
Calculate Summary → Display Results → Export Option (CSV/Text)


 7. TEST CASES

| Test Case | Input | Expected Output |
|-----------|-------|-----------------|
| Valid stock | AAPL, 10, $170 | Added successfully |
| Invalid symbol | XYZ | Error message |
| Negative shares | -5 | Error message |
| Zero buy price | 0 | Error message |
| Export CSV | Choice 1 | portfolio_YYYYMMDD_HHMMSS.csv |
| Export Text | Choice 2 | portfolio_YYYYMMDD_HHMMSS.txt |

 8. CHALLENGES FACED & SOLUTIONS

**Challenge:** Handling different purchase prices vs current prices
**Solution:** Separate buy_price and current_price fields

**Challenge:** CSV formatting with currency symbols
**Solution:** Use string formatting before writing to CSV

**Challenge:** Making output visually appealing
**Solution:** Added emojis, color indicators, and formatted tables

9. LEARNING OUTCOMES
- ✅ Mastered dictionary operations
- ✅ Learned CSV file handling in Python
- ✅ Applied input validation techniques
- ✅ Used datetime for file versioning
- ✅ Implemented proper error handling

 10. FUTURE IMPROVEMENTS (Optional)
- Add real-time stock price API integration
- Add buy/sell transaction tracking
- Create GUI version using Tkinter or Flask web app
- Add portfolio performance charts
- Support for multiple currencies

 11. CONCLUSION
Successfully created a functional Stock Portfolio Tracker that meets all requirements. The application is user-friendly, handles errors gracefully, and provides clear portfolio insights with file export capabilities.

12. REFERENCES
- Python CSV Documentation: docs.python.org/3/library/csv.html
- Python datetime: docs.python.org/3/library/datetime.html
- CodeAlpha Internship Guidelines
