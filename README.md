# telco_classification_project

# Project Goals:

- Find out why customers are churning at Telco.
- Construct classification models to predict customer churn.

# Initial questions of the data:
 - Q1: Does contract type affect whether someone churns?
 - Q2: Are high monthly charges causing customers to churn?
 - Q3: Is a customer having fiber optic internet related to a customer churning?
 - Q4: Is a customer having manual payments related to a customer churning?

# Project planning:
- ## Planning:
- ## Aquire data 
  Pull telco data utilizing get_telco_data function from Codeup mySQL database.
- ## Prepare data
  Clean data and split data into train, validate, test, utilizing prep_telco and splitting_data functions.
- ## Explore data
  Explore data by using Univariate, Bivariate/multivariate analysis.
- ## Model data
- Preprocessing to encode our values.
- Establish a baseline.
- Build models.
- Evaluate models.
- Select best models.
- Test models.

## Data Dictionary
| Feature | Definition | 
| :- | :- |
| Monthly Chaerge | Amount a customer is charged monthly |
| Total Charges | Cumulative amount a customer has paid |
| Gender Male | If a customer is male or female, 0 = Female, 1 = Male |
| Has Partner | If a customer has a partner, 0 = No, 1 = Yes |
| Has Dependents | If a customer has dependents, 0 = No, 1 = Yes |
| Has Phone Service | If a customer has phone service, 0 = No, 1 = Yes |
| Has Paperless Billing | If a customer has paperless billing, 0 = No, 1 = Yes |
| Has Tech Support | If a customer has tech support, 0 = No, 1 = Yes |
| Has Online Security | If a customer has online security, 0 = No, 1 = Yes |
| Has Online Backup | If a customer has online backup, 0 = No, 1 = Yes |
| Has Streaming TV | If a customer has streaming tv, 0 = No, 1 = Yes |
| Has Streaming Movies | If a customer has streaming movies, 0 = No, 1 = Yes |
| Has Device Protection | If a customer has device protection, 0 = No, 1 = Yes |
| Has Dependents | If a customer has dependents, 0 = No, 1 = Yes |
| Has Multiple Lines | If a customer has multiple lines, 0 = No, 1 = Yes |
| Contract | Type of contract customer has, 0 = Month-to-month, 1 = One year, 2 = Two year|
| Internet Service | Type of Internet Service customer has, 0 = No internet service, 1 = DSL, 2 = Fiber optic |
| Has Automatic Payment | If a customer has automatic payment, 0 = No, 1 = Yes |
| Churn (Target Variable) | If a customer has churned, False = No, True = Yes |
---

## To Reproduce Findings:
-	Clone this repository (telco-classification-project)
-	Create env file with username, host, password credentials to access Codeup mySQL telco-churn database.


## Key Findings:
-	Month-to-month contract, higher monthly payments, fiber optic internet, and manual payment type were among the biggest causes of churn.
## Recommendations:
-	Push for customers to sign up for one or two year contract as opposed to month-to-month with either a price incentive or including a free perk such as free tech support or online backup.
-	Push for DSL internet instead of fiber optic or include a free perk with fiber optic.
-	Give incentives for signing up for automatic payments instead of manual.

## Next Steps:
-	Dig deeper into the monthly payments to see what point customers are most likely to churn so we can incentivize them to stay prior to that point.
-	Find out what other factors are leading to the high rate of churn with fiber optic internet customers.
