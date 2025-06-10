
import pandas as pd

# --------------------------------------------
# 1. Create Sample Dataset (Only for Testing)
# --------------------------------------------
# If you already have a CSV file, you can skip this part.
sample_data = {
    'Name': ['preethi', 'sai', 'thanvika', 'kutti', 'manu'],
    'Maths': [85, 78, 90, None, 66],
    'Science': [92, 88, 85, 70, None],
    'English': [78, 76, None, 80, 72],
    'Total': [255, 242, 275, 225, 210]
}

sample_df = pd.DataFrame(sample_data)
sample_df.to_csv('student_performance.csv', index=False)
print("📁 Sample student_performance.csv file created.\n")

# --------------------------------------------
# 2. Load the Dataset
# --------------------------------------------
file_path = 'student_performance.csv'  # You can change the filename if needed

try:
    df = pd.read_csv(file_path)
    print("✅ Dataset loaded successfully.\n")
except FileNotFoundError:
    print(f"❌ File not found: {file_path}")
    exit()

# --------------------------------------------
# 3. Display Basic Information
# --------------------------------------------
print("🔎 First 5 Rows of the Data:")
print(df.head(), "\n")

print("📊 Dataset Info:")
print(df.info(), "\n")

print("📈 Summary Statistics:")
print(df.describe(), "\n")

# --------------------------------------------
# 4. Handle Missing Values
# --------------------------------------------
print("🛠️ Handling missing values...")
df_cleaned = df.fillna(df.mean(numeric_only=True))
print("✅ Missing values filled with column means.\n")

# --------------------------------------------
# 5. Save Cleaned Dataset
# --------------------------------------------
output_file = 'cleaned_student_performance.csv'
df_cleaned.to_csv(output_file, index=False)
print(f"💾 Cleaned data saved to: {output_file}")
