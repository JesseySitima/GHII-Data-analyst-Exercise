import pandas as pd
from faker import Faker

# Initialize the Faker generator
fake = Faker()

# Read the CSV file with PII
input_file = "client_purchases_deduplicated.csv"
df = pd.read_csv(input_file)

# Anonymize sensitive data
df['First Name'] = [fake.first_name() for _ in range(len(df))]
df['Last Name'] = [fake.last_name() for _ in range(len(df))]
df['Email'] = [fake.email() for _ in range(len(df))]
df['Phone'] = [fake.phone_number() for _ in range(len(df))]
df['Address'] = [fake.street_address() for _ in range(len(df))]
df['Zip Code'] = [fake.zipcode() for _ in range(len(df))]
df['Gender'] = [fake.random_element(elements=('Male', 'Female')) for _ in range(len(df))]
df['Date of Birth'] = [fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%m/%d/%Y') for _ in range(len(df))]

# Saving the anonymized data to a new CSV file
anonymized_output_file = "clients_deidentified.csv"
df.to_csv(anonymized_output_file, index=False)

print("Anonymized data saved to", anonymized_output_file)
