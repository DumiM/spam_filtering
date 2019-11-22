# Improving Spam Classification performance in real-life situations
### Please read the [report](report.pdf) for an indepth explanation and discsuion about this research and implementation.

### How to use:
- Download all ham data from Enron dataset and extract into `ham` folder
- Download all 2019 spam from Untroubled Software and extract into `spam` folder
- Download all 2000 spam from Untroubled software and extract into `oldspam` folder
- Run the `read_*` python files to read all these downloaded files into lists
- Run the `Initial_pre_processing_Data` jupyter file to get the intial pandas dataframes
- Run the other jupyter files to see the results of different feature extraction methods
- Run the `V2_pre_processing_Data` jupyter file to re-process using relvant features
- Then run the `Re_processed_Real_life_scenario` to see the improved results
