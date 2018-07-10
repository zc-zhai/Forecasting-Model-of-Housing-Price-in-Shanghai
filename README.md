# Forecasting Model of Housing Price in Shanghai
The project aims at collecting as comprehensive data as possible of housing in Shanghai and forecasting the price by building a reliable model.<br>
Mainly using knowledge in Data Mining and Machine Learning.<br>
Implemented by Python.<br>
Supported by `Anaconda`.
## Main Steps
1. Internet data crawling: Crawl the information and data of housing in Shanghai area from [Chain Home Website](https://sh.lianjia.com/ershoufang/ "Chain Home, Shanghai, China");<br>
2. Chinese word segmentation and preprocessing: Convert the word segmentation data into structured data for the natural language contained in the crawled content, and perform operations such as missing value filling and data cleaning;<br>
3. Data modeling, tuning, and testing: Establish a house price forecasting model, tune the parameters, and test the model performance;<br>
4. Report Writing: Write the main process into a document and upload the code and the crawled data set.
## File Description
* house_info.xlsx: dataset
* Data Crawling: Step 1
* Data Pretreatment: Step 2
* Data Visualization: Step 3
* Building Models: Step 4
* report: describe the whole process and summarize the project
## Summary
In this experimental project, a total of 39,416 data volumes were crawled, as well as 28 preliminary feature fields, including text descriptions, data, keywords, and more. After data processing, 38,498 effective structured data is formed, which is effective enough. There are 14 feature attributes, including numerical and text analysis extraction features. Established with 6 kinds and 3 types of regression algorithms, these models were compared with each other. We mainly selected the integrated model `random forest` and `neural network multi-layer perceptron algorithm` to make type tuning and evaluation. Finally, a well-performing house price forecasting model was implemented.