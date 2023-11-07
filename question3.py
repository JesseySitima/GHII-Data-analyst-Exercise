import pandas as pd

# task a: Read the CSV file
input_file = "client_purchases.csv"
df = pd.read_csv(input_file)

# task b: Find and identify duplicate records
duplicates = df[df.duplicated(subset=['First Name', 'Last Name', 'Email', 'Phone', 'Address', 'Zip Code', 'Gender', 'Date of Birth', 'Product', 'Quantity', 'Cost'])]

# task c: Remove the duplicate records
df = df.drop_duplicates(subset=['First Name', 'Last Name', 'Email', 'Phone', 'Address', 'Zip Code', 'Gender', 'Date of Birth', 'Product', 'Quantity', 'Cost'], keep='first')

# task d: Export the cleaned CSV file
cleaned_output_file = "client_purchases_deduplicated.csv"
df.to_csv(cleaned_output_file, index=False)

# task e: Identify unique clients and assign unique IDs
unique_clients = df[['First Name', 'Last Name', 'Email', 'Phone', 'Address', 'Zip Code', 'Gender', 'Date of Birth']].drop_duplicates().reset_index(drop=True).reset_index()
unique_clients.rename(columns={'index': 'Client ID', 'First Name': 'First Name', 'Last Name': 'Last Name', 'Email': 'Email', 'Phone': 'Phone', 'Address': 'Address', 'Zip Code': 'Zip Code', 'Gender': 'Gender', 'Date of Birth': 'Date of Birth'}, inplace=True)

# Export the unique clients to a CSV file
unique_clients_output_file = "clients_unique.csv"
unique_clients.to_csv(unique_clients_output_file, index=False)
