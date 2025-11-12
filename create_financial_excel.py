import pandas as pd
import os

# Create comprehensive financial health data
def create_ea_financial_health_excel():
    """Create a comprehensive Excel file for EA Aura Financial Health"""
    
    # Create Excel writer object
    excel_file = 'EA_Aura_Financial_Health.xlsx'
    
    try:
        with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
            
            # Sheet 1: Income Tracking
            income_data = {
                'Income Category': ['Base Salary', 'Bonus/Incentives', 'Side Projects', 'Investment Returns', 'Other Income', 'TOTAL INCOME'],
                'Monthly Amount': [7500, 1000, 500, 300, 200, '=SUM(B2:B6)'],
                'Annual Amount': [90000, 12000, 6000, 3600, 2400, '=SUM(C2:C6)'],
                'Notes': ['Primary employment income', 'Performance-based rewards', 'Freelance or consulting', 'Dividends and interest', 'Miscellaneous sources', 'Total income streams']
            }
            income_df = pd.DataFrame(income_data)
            income_df.to_excel(writer, sheet_name='Income Tracking', index=False)
            
            # Sheet 2: Expense Analysis  
            expense_data = {
                'Expense Category': ['Housing (Rent/EMI)', 'Utilities & Bills', 'Transportation', 'Food & Groceries', 'Healthcare', 'Entertainment', 'Clothing', 'Education', 'Emergency Fund', 'Miscellaneous', 'TOTAL EXPENSES'],
                'Monthly Amount': [3800, 400, 600, 1200, 300, 400, 200, 300, 500, 300, '=SUM(B2:B11)'],
                'Annual Amount': [45600, 4800, 7200, 14400, 3600, 4800, 2400, 3600, 6000, 3600, '=SUM(C2:C11)'],
                'Budget %': ['40.0%', '4.2%', '6.3%', '12.6%', '3.2%', '4.2%', '2.1%', '3.2%', '5.3%', '3.2%', '84.2%'],
                'Notes': ['Rent or mortgage payments', 'Electricity, water, internet, phone', 'Fuel, public transport, maintenance', 'Daily meals and household items', 'Medical insurance, checkups', 'Movies, dining out, hobbies', 'Apparel and accessories', 'Courses, books, training', 'Monthly emergency savings', 'Other unexpected expenses', 'Total monthly/annual expenses']
            }
            expense_df = pd.DataFrame(expense_data)
            expense_df.to_excel(writer, sheet_name='Expense Analysis', index=False)
            
            # Sheet 3: Investment Portfolio
            investment_data = {
                'Investment Type': ['PPF/EPF', 'Mutual Funds SIP', 'Stocks/Equity', 'Fixed Deposits', 'Gold/Commodities', 'TOTAL INVESTMENTS'],
                'Monthly Amount': [1000, 800, 400, 200, 100, '=SUM(B2:B6)'],
                'Annual Amount': [12000, 9600, 4800, 2400, 1200, '=SUM(C2:C6)'],
                'Risk Level': ['Low', 'Medium', 'High', 'Low', 'Medium', 'Mixed'],
                'Expected Return': ['7-8%', '10-12%', '12-15%', '5-6%', '6-8%', '8-10%']
            }
            investment_df = pd.DataFrame(investment_data)
            investment_df.to_excel(writer, sheet_name='Investment Portfolio', index=False)
            
            # Sheet 4: Financial Goals
            goals_data = {
                'Financial Goal': ['Emergency Fund', 'Home Down Payment', 'Vacation Fund', 'Retirement Corpus', 'Child Education'],
                'Target Amount': [50000, 500000, 100000, 5000000, 1000000],
                'Time Frame (months)': [12, 60, 24, 360, 180],
                'Monthly Saving Required': [4167, 8333, 4167, 2778, 5556],
                'Current Progress %': ['25%', '10%', '15%', '5%', '8%']
            }
            goals_df = pd.DataFrame(goals_data)
            goals_df.to_excel(writer, sheet_name='Financial Goals', index=False)
            
            # Sheet 5: Financial Health Ratios
            ratios_data = {
                'Financial Ratio': ['Savings Rate', 'Debt-to-Income', 'Emergency Fund Ratio', 'Investment Rate'],
                'Current Value': ['15.8%', '40.0%', '1.5 months', '26.3%'],
                'Ideal Range': ['20-30%', '<30%', '3-6 months', '20-30%'],
                'Status': ['Needs Improvement', 'High', 'Low', 'Good'],
                'Action Required': ['Increase savings by 5%', 'Reduce debt payments', 'Build emergency fund faster', 'Maintain current rate']
            }
            ratios_df = pd.DataFrame(ratios_data)
            ratios_df.to_excel(writer, sheet_name='Health Ratios', index=False)
            
            # Sheet 6: Budget Allocation (50/20/20/10 Rule)
            budget_data = {
                'Category': ['Needs (Essential)', 'Wants (Lifestyle)', 'Savings', 'Investments'],
                'Recommended %': ['50%', '20%', '20%', '10%'],
                'Recommended Amount': [4750, 1900, 1900, 950],
                'Current Amount': [5400, 1400, 1500, 1200],
                'Variance': [-650, 500, 400, -250],
                'Status': ['Over Budget', 'Under Budget', 'Under Budget', 'Over Budget']
            }
            budget_df = pd.DataFrame(budget_data)
            budget_df.to_excel(writer, sheet_name='Budget Allocation', index=False)
            
            # Sheet 7: Financial Tips
            tips_data = {
                'Category': ['Data Entry', 'Validation', 'Organization', 'Chart Updates', 'Insights', 'Dashboard', 'Version Control', 'Protection', 'Backup'],
                'Tip': [
                    'Keep data consistent',
                    'Add drop-downs for categories', 
                    'One purpose per sheet',
                    'Charts update automatically',
                    'Use conditional formatting',
                    'Create summary dashboard',
                    'Keep dated copies',
                    'Lock formula cells',
                    'Save to cloud storage'
                ],
                'Action Required': [
                    'Use standard category names',
                    'Prevent typos in data entry',
                    'Separate income, expenses, investments',
                    'Stay within existing data ranges',
                    'Green for positive, red for negative',
                    'Combine key metrics in one view',
                    'Track progress over time',
                    'Prevent accidental changes',
                    'Ensure data safety and accessibility'
                ]
            }
            tips_df = pd.DataFrame(tips_data)
            tips_df.to_excel(writer, sheet_name='Financial Tips', index=False)
            
        print(f"✅ Successfully created {excel_file}")
        return True
        
    except Exception as e:
        print(f"❌ Error creating Excel file: {e}")
        return False

if __name__ == "__main__":
    print("🏦 Creating EA Aura Financial Health Excel File...")
    success = create_ea_financial_health_excel()
    
    if success:
        print("📊 Excel file created successfully!")
        print("📁 File location: EA_Aura_Financial_Health.xlsx")
        print("📋 Contains 7 comprehensive sheets for financial wellness tracking")
    else:
        print("❌ Failed to create Excel file")