import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class FinSight:
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)
        self.df['Date'] = pd.to_datetime(self.df['Date'])

    def generate_summary(self):
        summary = self.df.groupby('Category')['Amount'].sum().reset_index()
        print("\n--- [FinSight] Spending Summary ---")
        print(summary.to_string(index=False))
        return summary

    def plot_expenses(self):
        plt.figure(figsize=(10, 6))
        sns.set_theme(style="whitegrid")
        data = self.df.groupby('Category')['Amount'].sum()
        
        plt.pie(data, labels=data.index, autopct='%1.1f%%', 
                startangle=140, colors=sns.color_palette('pastel'))
        plt.title('Expense Distribution Analysis', fontsize=14)
        plt.tight_layout()
        plt.savefig('expense_report.png')
        print("\n[Success] Visualization saved as 'expense_report.png'")

if __name__ == "__main__":
    if not os.path.exists('expenses.csv'):
        data = {
            'Date': ['2024-01-01', '2024-01-02', '2024-01-05', '2024-01-10', '2024-01-15'],
            'Category': ['Rent', 'Groceries', 'Dining', 'Transport', 'Utilities'],
            'Amount': [1200, 350, 150, 80, 120]
        }
        pd.DataFrame(data).to_csv('expenses.csv', index=False)

    analyzer = FinSight('expenses.csv')
    analyzer.generate_summary()
    analyzer.plot_expenses()
  
